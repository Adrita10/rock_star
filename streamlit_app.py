
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  #streamlit.text(fruityvice_response.json())
  # normalizes the json output
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # put into a table format
  return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
    #streamlit.write('The user entered ', fruit_choice)
  else:
    back_from_fcn = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_fcn)
except URLError as e:
  streamlit.error()

#my_cur = my_cnx.cursor()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list")
       return my_cur.fetchall()
 
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_row)

def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
       return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('which fruit to add?')

if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_From_fcn = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(back_From_fcn)
streamlit.stop()
fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")


