import streamlit as st
import os
import openai

openai.api_key = 'YOUR API KEY'


st.title('Grammar correction app')
st.subheader('EX:- She no went to the market.')
txt = st.text_area('Enter text to correct')
if st.button('Correct'):
    response = openai.Completion.create(
  model="text-davinci-002",
  prompt=f"Correct this to standard English:\n\n{txt}",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
    
    st.write(response.choices[0].text)
    print(response.choices[0].text)
