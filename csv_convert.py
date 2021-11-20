import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///supermarket.db')


crimeDF = pd.read_csv('supermarketdatas.csv')

crimeDF.to_sql('supermarket',engine,index=False, if_exists='append')