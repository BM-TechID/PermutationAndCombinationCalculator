# BM-TECHID

import streamlit as st
import codecs
import streamlit.components.v1 as components
from itertools import permutations, combinations
import openai

st.title('Permutation & Combination Calculator')

st.markdown('''
<hr style="height:2px;width:100%;border-width:0;color:gray;background-color:gray">
            ''',
            unsafe_allow_html=True)

# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = "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"

menu = ['Permutation', 'Combination', 'About', 'Developer', 'AingBotz']
choice = st.sidebar.selectbox("Menu", menu)

if choice == 'Permutation':
  st.header("""Permutation""")
  st.header("")
  st.latex(r""" ^nP_r = \frac{n!}{(n-r)!} """)
  st.header("")

  iterable = st.text_input(label="Enter Iterable separated by a space")

  if iterable:
    iterable = list(int(n) for n in iterable.split(' '))

  try:

    num2 = int(st.number_input("Enter number for **r**"))
    calc = permutations(iterable, num2)

    calc = [i for i in calc]
    result = str(calc).strip('[]')

    if iterable:
      st.success(f"""Result : \n\n{result}\n\nThere are **{len(calc)}** 
                    ways to permute the iterable""")

  except ValueError as err:
    st.warning(f"{err}")

elif choice == 'Combination':
  st.header("""Combination""")
  st.header("")
  st.latex(r""" ^nC_k = \frac{n!}{k!(n-r)!} """)
  st.header("")

  iterable = st.text_input(label="Enter Iterable separated by a space")

  if iterable:
    iterable = list(int(n) for n in iterable.split(' '))

  try:

    num2 = int(st.number_input("Enter number for **k**"))
    calc = combinations(iterable, num2)

    calc = [i for i in calc]
    result = str(calc).strip('[]')

    if iterable:
      st.success(f"""Result : \n\n{result}\n\nThere are **{len(calc)}** 
                    ways to combine the iterable""")

  # chatGPT mnjelaskan langkah perhitungan combination
  ChatGPT = openai.Completion.create(
    engine=model_engine,
    prompt="Combination",
    max_tokens=1024,
    n=1,
    temperature=0.5,
  )
  response = ChatGPT.choices[0].text
  st.write(response)

  



  except ValueError as err:
    st.warning(f"{err}")

elif choice == 'About':
  st.subheader('About')

elif choice == 'Developer':
  pass

elif choice ==  'AingBotz':
  def ChatGPT(user_query):
    ''' 
      This function uses the OpenAI API to generate a response to the given 
      user_query using the ChatGPT model
      '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
      engine=model_engine,
      prompt=user_query,
      max_tokens=1024,
      n=1,
      temperature=0.5,
    )
    response = completion.choices[0].text
    return response

  st.title("Chatting with ChatGPT")
  st.sidebar.header("Instructions")
  st.sidebar.info('''This is a web application that allows you to interact with
          the OpenAI API's implementation of the ChatGPT model.
          Enter a **query** in the **text box** and **press enter** to receive
          a **response** from the ChatGPT
          ''')

  # Get user input
  user_query = st.text_input("Enter query here, to exit enter :q",
                              "what is Python?")
  if user_query:
    # Generate response
    response = ChatGPT(user_query)
    # Display response
    st.success(response)
