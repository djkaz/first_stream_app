import streamlit

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
##streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
      
#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#OLD SECTION
#import requests 
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json()) ##to be removed from the app

#take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)

#snowflake connector
import snowflake.connector

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row) 
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#my_cur.execute("The fruit load list contains:")
#streamlit.text(my_data_row)


###test streamlit

import snowflake.connector

 
print("Connecting...")

con = snowflake.connector.connect(

 user="alextiron",

 password="Ax#l198901",

 account="ie64300.eu-west-1.aws",
 warehouse="COMPUTE_WH",
 database="SNOWFLAKE_SAMPLE_DATA",
 schema="PUBLIC"

)

 

print(con)



con.cursor().execute("USE WAREHOUSE " + WAREHOUSE)
con.cursor().execute("USE DATABASE " + DATABASE)

 

try:

  result = con.cursor().execute("Select * from REGION")

  result_list = result.fetchall()

  print(result_list)

 

finally:

con.cursor().close()
con.cursor().close()

 

GENERAL DISCUSSION
