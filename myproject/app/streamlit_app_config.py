import streamlit as st
import openai

st.header("Streamlit web app using OpenAI davinci engine")

user_question = st.text_area("Enter your natural language query to the ETF Dataset")
temp = st.slider("Temperature for davinci engine", 0.0, 1.0, 0.5)

if len(user_question) > 0:
    if st.button("Send query"):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Please translate this text into SQL query for me",
            max_token = 516,
            temperature = temp
            )

        # Print the response

        res = response["choices"][0]["text"]
        st.info(res)
                                     
st.write("We will be connecting our ETF SQlite dataset to this streamlit interface")