# Custom SQL Query Generator

## Overview

Custom SQL Query Generator is an AI-powered application that converts natural language questions into executable SQL queries. Built using Google Gemini, LangChain, and ChromaDB, the application understands user intent, retrieves semantically similar examples using Few-Shot Learning, generates optimized MySQL queries, executes them on the connected database, and displays the results through an interactive Streamlit interface.

---

## Features

- Convert natural language into executable MySQL queries.
- AI-powered SQL generation using Google Gemini and LangChain.
- Semantic Few-Shot Learning using ChromaDB and Sentence Transformers.
- Automatic execution of generated SQL queries.
- Interactive Streamlit web interface.
- Real-time query results and database interaction.
- Context-aware SQL generation with semantic similarity search.

---

## Tech Stack

- **Programming Language:** Python
- **LLM:** Google Gemini
- **Framework:** LangChain
- **Vector Database:** ChromaDB
- **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- **Database:** MySQL
- **Frontend:** Streamlit
- **Environment Management:** Python Dotenv

---

## Project Structure

```
.
├── main.py                 # Streamlit frontend
├── langchain_helper.py     # LangChain pipeline and SQL chain
├── few_shots.py            # Few-shot prompt examples
├── CustomSQLQueryGen.ipynb # Development notebook
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/CustomDB-SQL_Query_Generator.git
cd CustomDB-SQL_Query_Generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project directory.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## Database Configuration

Update the MySQL credentials inside `langchain_helper.py`.

```python
db_user = "root"
db_password = "your_password"
db_host = "localhost:3306"
db_name = "your_database"
```

Make sure your MySQL server is running before launching the application.

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run main.py
```

Open the generated local URL in your browser.

---

## Example Queries

- How many white Levi's T-shirts are available?
- What is the total inventory value for Nike products?
- Show the revenue generated after discounts.
- How many XL T-shirts are currently in stock?
- Which brand has the highest inventory value?

---

## How It Works

1. User enters a natural language question.
2. ChromaDB retrieves the most semantically similar examples.
3. LangChain constructs a Few-Shot prompt.
4. Google Gemini generates an optimized SQL query.
5. The query executes on the MySQL database.
6. Results are returned and displayed in the Streamlit interface.

---

## Future Improvements

- Support PostgreSQL and SQLite
- Query history
- Authentication and user management
- SQL query explanation
- Export query results to CSV/Excel
- Interactive database schema visualization

---

## License

This project is licensed under the MIT License.
