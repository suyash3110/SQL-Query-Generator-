import os
from dotenv import load_dotenv

from langchain.prompts import SemanticSimilarityExampleSelector, PromptTemplate, FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from few_shots import few_shots  # Assuming this is correctly defined in another module

load_dotenv()  # Take environment variables from .env (especially Google API key)

def get_few_shot_db_chain():
    db_user = "root"
    db_password = "Arka%40281004"
    db_host = "localhost:3306"
    db_name = "db_tshirts"
    db_uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

    # Create an instance of SQLDatabase
    db = SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=3)

    # Initialize the language model using the factory method
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise ValueError("GOOGLE_API_KEY environment variable not found")

    llm = GoogleGenerativeAI(model="gemini-pro")

    # Initialize embeddings and vectorstore
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    def ensure_strings(example):
        return " ".join([str(value) for value in example.values()])

    to_vectorize = [ensure_strings(example) for example in few_shots]

    def flatten_metadata(metadata):
        return {k: str(v) if isinstance(v, (dict, list)) else v for k, v in metadata.items()}

    metadata = [flatten_metadata(example) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=metadata)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    mysql_prompt = """
    You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],  # These variables are used in the prefix and suffix
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain