import streamlit
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.title('My parents new healthy diner')
streamlit.header('🥣 🥗 🐔 🥑🍞Breakfast Menu')
streamlit.text('Omega3')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.multiselect("pick fruits here:" list(my_fruit_list))
streamlit.dataframe(my_fruit_list)
