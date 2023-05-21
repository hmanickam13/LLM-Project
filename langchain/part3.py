from os import getenv
from dotenv import load_dotenv
import sqlite3
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

load_dotenv()

DB_URL = getenv("DB_URL")

conn = sqlite3.connect(DB_URL)

db = SQLDatabase.from_uri(f"sqlite:///{DB_URL}")

toolkit = SQLDatabaseToolkit(db=db)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

# agent_executor.run("Describe what the tables represent.")

# agent_executor.run("Did spy outperform tlt last year")

# This gets stuck when it queries for min and max dates in each table's date column
# agent_executor.run("What is the starting and ending dates of the different etfs")