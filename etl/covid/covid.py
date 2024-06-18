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
except mysql.connector.Error as err:
    print("An error occurred:", err)

#  Normalize json to make a dataframe
data = pd.json_normalize(res, ["response"])
df = pd.DataFrame(data)
df = df.rename(columns={0:"name"})

#  Convert df to be inserted in MySQL
engine = create_engine(f"mysql+mysqlconnector://root:{os.getenv('PW')}@localhost/covid_db")
df.to_sql(name='countries', con=engine, index=False, if_exists='replace')
