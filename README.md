# Custom SQL Query Generator

## Overview

The Custom SQL Query Generator leverages machine learning and generative AI to automatically generate SQL queries based on natural language input. It uses GooglePalm and GeminiAI for natural language processing and ChromaDB as the vector database. The web interface is built using Streamlit.

## Tech Stack

- **Machine Learning**: Jupyter Notebook
- **Libraries**: TensorFlow
- **Generative-AI**: GooglePalm and GeminiAI
- **Vector Database**: ChromaDB
- **Web Interface**: Streamlit

## Features

- Generate SQL queries from natural language input.
- Interactive web interface for ease of use.
- Supports semantic search and similarity matching with ChromaDB.

## Installation

### Prerequisites

Ensure you have Python 3.9+ installed on your machine.

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ArkaChakraborty2804/CustomDB-SQL_Qery_Generator.git
    cd CustomDB-SQL_Qery_Generator
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root and add your API keys:
    ```dotenv
    GOOGLE_API_KEY=your_google_api_key
    GEMINI_API_KEY=your_gemini_api_key
    ```

## Usage

1. **Run the Jupyter Notebook**:
    - Start Jupyter Notebook:
      ```sh
      jupyter notebook
      ```
    - Open the relevant notebook and execute the cells to perform machine learning tasks and model training.

2. **Run the Streamlit Web Interface**:
    - Start the Streamlit server:
      ```sh
      streamlit run main.py
      ```
    - Open the provided URL in your web browser to access the application.

3. **Example Query**:
    - In the Streamlit web interface, enter a natural language query such as "How many white color Levi's shirts do I have?" and receive the corresponding SQL query.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
