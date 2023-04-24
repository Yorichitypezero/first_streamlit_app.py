#Importing the library Streamlit
import streamlit
#Title
streamlit.title('My Parents Healthy Dinner')
#Header of the file
streamlit.header('Breakfast Menu')
#Text/Menu card
streamlit.text('🥣 Omega 3 and blueberry oatmeal')
streamlit.text('🥗 Kale,Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Egg Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
#Another Header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#Importing Pandas
import pandas
#Reading the CSV files from the Amazon AWS S3 bucket
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
