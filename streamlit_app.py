
import streamlit
import pandas

streamlit.title('My Mom''s New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞Banana sandwich')
streamlit.text('🥗green salad')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_Fruit_list = my_Fruit_list.set_index('Fruit')

#put a pick list
streamlit.multiselect("Choose: ",list(my_fruit_list.index))

#display the dataframe
streamlit.dataframe(my_fruit_list)


