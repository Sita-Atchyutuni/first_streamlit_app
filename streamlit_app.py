import streamlit
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.title('My parents new healthy diner')
streamlit.header('🥣 🥗 🐔 🥑🍞Breakfast Menu')
streamlit.text('Omega3')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
Fruits_selected=streamlit.multiselect("pick fruits here:", list(my_fruit_list.index),['Avocado','Strawberries'])
Fruits_to_show=my_fruit_list.loc[Fruit_selected]
streamlit.dataframe(Fruits_to_show)
