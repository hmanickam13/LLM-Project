import os
from os import getenv # to retrieve env variable values
import openai
import sqlite3
from dotenv import load_dotenv # to load env variables
# from streamlit_app_config import launch_streamlit_app
# from sqlalchemy import create_engine

# Load env variables from .env into the env
load_dotenv()

# Values of env variables
DB_URL = getenv("DB_URL")
OPENAI_KEY = getenv("OPENAI_KEY")

# Load openai key
openai.api_key = OPENAI_KEY

# Define a class for the streamlit app
class StreamlitAppConfig:

    # This value needs to be set according to our use case.
    # We don't use it yet.
    # CORS_HEADERS = "Content-Type"

    # If DB exists,
    if DB_URL:
        
        # Connect to db
        conn = sqlite3.connect(DB_URL)

        command = f"streamlit run streamlit_app_config.py --server.enableCORS=false --server.enableXsrfProtection=false --server.maxUploadSize=1028"
        # Additional arguments explained:
            # --server.enableCORS=false:
                # Disables Cross-Origin Resource Sharing (CORS) support in the Streamlit server.
                # CORS allows web browsers to make requests to a different domain, but in this case, it is disabled by setting it to false.
            # --server.enableXsrfProtection=false:
                # Disables Cross-Site Request Forgery (CSRF) protection in the Streamlit server.
                # CSRF protection helps prevent unauthorized requests, but it is disabled in this case by setting it to false.
            # --server.maxUploadSize=1028:
                # Sets the maximum upload size limit for file uploads in the Streamlit server to 1028 MB.

        # Execute the command string in os.system()
        os.system(command)

        # Call the function to launch the custom Streamlit app with the connected database
        # launch_streamlit_app(conn)
        # streamlit run 

    # If DB does not exist,
    else:
        print('DB_URL not found, please check your environment')
        exit(1)