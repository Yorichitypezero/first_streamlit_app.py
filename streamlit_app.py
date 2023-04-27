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

#Displaying fruit-list in the picker
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

#Picking an item from the drop down list
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Displaying the output
streamlit.dataframe(fruits_to_show)

#Importing Requests to display FruitVice API using User choice
streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.write("The user entered",)

#normalise the json file format
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

#output to be displayed on the screen
streamlit.dataframe(fruityvice_normalized)
