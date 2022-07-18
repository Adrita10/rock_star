
import streamlit
import pandas
import requests

streamlit.title('My Mom''s New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞Banana sandwich')
streamlit.text('🥗green salad')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#put a pick list
fruits_selected = streamlit.multiselect("Choose: ",list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the dataframe
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())

# normalizes the json output
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# put into a table format
streamlit.dataframe(fruityvice_normalized)



