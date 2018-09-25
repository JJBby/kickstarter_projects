# This is the script used during lecture as a demo for loading data from CSV to a DB
from sqlalchemy import create_engine
# import chardet
import pandas as pd
import os


path = './assets/ks-projects-201801.csv'

# with open(path, 'rb') as f:
#   contents = f.read()

# with open(path, 'rb') as rawdata:
#     result = chardet.detect(rawdata.read(10000))
# import pdb; pdb.set_trace()
# csv_data = pd.read_csv(contents)
# import pdb; pdb.set_trace()
csv_data = pd.read_csv(path, error_bad_lines=False)
df = pd.DataFrame(csv_data)


# Adjust NaN values in each column, and generally clean data set
# df['ID'] = df['Unnamed: 0'] + 1
# del df['Unnamed: 13']
# del df['Unnamed: 14']
# del df['Unnamed: 15']
# del df['Unnamed: 16']


df['kickstarter_id'] = df['ID'].fillna('unknown')
del df['ID']
df['name'] = df['name'].fillna('unknown')
df['category'] = df['category'].fillna('unknown')
df['main_category'] = df['main_category'].fillna('unknown')
df['currency'] = df['currency'].fillna('unknown')
df['deadline'] = df['deadline'].fillna('unknown')
df['goal'] = df['goal'].fillna(0.0)
df['launched'] = df['launched'].fillna('unknown')
df['pledged'] = df['pledged'].fillna(0.0)
df['state'] = df['state'].fillna('unknown')
df['backers'] = df['backers'].fillna('unknown')
df['country'] = df['country'].fillna('unknown')
df['usd_pledged'] = df['usd_pledged'].fillna(0.0)
df['usd_pledged_real'] = df['usd_pledged_real'].fillna(0.0)
df['usd_goal_real'] = df['usd_goal_real'].fillna(0.0)



db_protocol = 'postgresql'
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')


engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))

df.to_sql("kickstarter_app_project", engine, if_exists='append', index=False)
