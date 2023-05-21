import sys
from os import getenv
from dotenv import load_dotenv
from io import StringIO

import openai
import sqlite3
import streamlit as st
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

# Load env variables from .env into the env
load_dotenv()

# Get value from .env file
DB_URL = getenv("DB_URL")
# Set up the SQLite database connection
db = SQLDatabase.from_uri(f"sqlite:///{DB_URL}")

# Get value from .env file
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
# Load openai key
openai.api_key = OPENAI_API_KEY
# Set up the OpenAI LLM model
llm = OpenAI(temperature=0)

# Set up the SQLDatabaseToolkit
toolkit = SQLDatabaseToolkit(db=db)
# Create the AgentExecutor
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

# Streamlit app configuration
st.header("Streamlit web app to query ETF SQLite database using Langchain")

# Prompt for user
user_question = st.text_area("Enter your natural language query to the ETF Dataset")

# If there is a question
if len(user_question) > 0:
    # If user presses button,
    if st.button("Send query"):
        # Redirect stdout to a variable
        sys.stdout = mystdout = StringIO()
        # Show steps of agent
        agent_executor.verbose = True
        # Telling agent to execute user's query
        agent_executor.run(user_question)
        # Capture output which would normally be printed to the terminal
        sys.stdout = sys.__stdout__  # Reset stdout to its default value
        output = mystdout.getvalue()

        # Extract the final result from the output
        # final_result = output.split("FINAL RESULT: ")[-1]
        
        # Extract the last 30 lines from the output
        # not sure if this works or not
        lines = output.strip().split("\n")
        last_5_lines = "\n".join(lines[-5:])

        # Add prompt to summarize the last 30 lines of output
        prompt = f"Only give me the final answer from the last 30 lines of output below:\n\n{last_5_lines}"
        
        # Summarize the output using OpenAI Davinci API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=30,
        )
        # Extract the summarized reponse from the API reponse
        summarized_result = response.choices[0].text.strip()
        
        # Display the final summarized result
        st.text(summarized_result)
        
        # Provide an option to expand the detailed output we captured earlier
        with st.expander("Expand answer"):
            st.code(output, language="text")


