import requests
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

#  Headers required for API
headers = {'x-rapidapi-host': 'covid-193.p.rapidapi.com', 'x-rapidapi-key': os.getenv('API_KEY')}
r = requests.get(url='https://covid-193.p.rapidapi.com/countries', headers=headers)
#  Get response back in json
res = r.json()
#  Normalize json to make a dataframe
df = pd.json_normalize(res, 'response')
#  Connect to local MySQL
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv('PW'),
        database='covid_db'
    )
    print("Connection established")
    cursor = mydb.cursor()
    cursor.execute("create table if not exists countries (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200))")
    print("Table created")
except mysql.connector.Error as err:
    print("An error occurred:", err)

#  Convert df to be inserted in MySQL
engine = create_engine(f"mysql+mysqlconnector://root:{os.getenv('PW')}@localhost/covid_db")
df.to_sql(name='countries', con=engine, index=True, if_exists='replace')