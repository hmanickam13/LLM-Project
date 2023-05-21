from os import getenv
from dotenv import load_dotenv
import sqlite3
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv()

DB_URL = getenv("DB_URL")

conn = sqlite3.connect(DB_URL)

db = SQLDatabase.from_uri(f"sqlite:///{DB_URL}")

llm = OpenAI(temperature=0) # 0 more deterministric, 1 more random/creative

db_chain =SQLDatabaseChain(llm=llm, database=db, verbose=True)

# db_chain.run("How many ETF's does the database contain? What are they?")

db_chain.run("How many tables are there in this db?")

# db_chain.run("How many tables are there in this db?")
db_chain.run("What is the top performing ETF from 2010?")

# db_chain.run("Did spy outperform tlt in the last year? By how much did it outperform?")

# db_chain.run("What is the starting and ending dates of the different etfs: 'spy', 'tlt', 'hyg', 'lqd', 'vnq'")