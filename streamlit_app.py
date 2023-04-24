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
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

#Picking an item from the drop down list
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
