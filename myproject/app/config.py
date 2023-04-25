import os
from os import getenv
import openai
import sqlite3
from dotenv import load_dotenv
# from streamlit_app_config import launch_streamlit_app
# from sqlalchemy import create_engine

load_dotenv()

# For this to work, you need to create a .env file in the same directory which contains
# OPENAI_KEY = <Your secret key>
# DB_URL= <URL>
DB_URL = getenv("DB_URL")
OPENAI_KEY = getenv("OPENAI_KEY")

openai.api_key = OPENAI_KEY

class StreamlitAppConfig:
    CORS_HEADERS = "Content-Type"

if DB_URL:
    conn = sqlite3.connect(DB_URL)
    command = f"streamlit run streamlit_app_config.py --server.enableCORS=false --server.enableXsrfProtection=false --server.maxUploadSize=1028"
    os.system(command)
    # Call the function to launch the custom Streamlit app with the connected database
    # launch_streamlit_app(conn)
    # streamlit run 

else:
    print('DB_URL not found, please check your environment')
    exit(1)