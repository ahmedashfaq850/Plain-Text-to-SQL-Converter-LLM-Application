import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
import sqlite3

load_dotenv()

my_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = my_api_key)

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question, prompt):
    response = model.generate_content([prompt[0], question])
    return response.text


## Function to retrieve the data from the database
def get_sql_response(query, db):
    conn = sqlite3.connect(db)
    curr = conn.cursor()
    curr.execute(query)
    data = curr.fetchall() 
    conn.commit()
    conn.close()
    
    for record in data:
        print(record)
    return data

prompt = ["""
          you are an expert in converting english question into sql query,
          The sql database is about employees,
            The table name is employees,
            The columns are NAME, AGE, POSITION, SALARY
            for example if anyone can ask the question like
            "List all the employees who are software engineers"
            then the sql query should be
            "SELECT * FROM employees WHERE POSITION = 'Software Engineer'"
            example 2:
            "List all the employees who are under 30"
            then the sql query should be
            "SELECT * FROM employees WHERE AGE < 30"
            and so on
            you are only expert in converting english questions into sql queries
            and create a query for the given question based on the given database only 
            if anyone asks a question that is not related to the given database
            then you will not be able to answer that question
            and just say "I am sorry, I am not able to answer this question"
            also the sql code should not have ``` at the start and end sql word in output
          """]


## streamlit App Code

st.set_page_config(page_title="Text to SQL Converter Application")
st.header("Text to SQL Converter Application")

question = st.text_input("Enter your question here:")

submit = st.button("Generate SQL")

if input and submit:
    query = get_gemini_response(question, prompt)
    st.subheader('The Response is: ')
    data = get_sql_response(query, 'employees.db')
    for record in data:
        st.write(record)