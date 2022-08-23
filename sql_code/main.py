import argparse
import sqlalchemy
import pandas as pd


""" parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="テーブル名")
parser.add_argument("csv_path", help="読み込むCSVファイルのパス")
args = parser.parse_args() """
# 引数の設定
connection_config = {
    'user': 'root',
    'password': 'sekigahara',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'test_database',
    'database_type': 'mysql'
}

engine = sqlalchemy.create_engine('mysql+pymysql://root:sekigahara@127.0.0.1/test_database'.format(**connection_config), encoding='utf-8')

tables = ['users', 'usergroups', 'devices', 'devicegroups', 'users_devices', 'users_usergroups', 'devices_devicegroups', 'usergroups_devicegroups']

for table in tables:
    df = pd.read_csv('data/' + table + '_data.csv')
    print(df)
    # PostgreSQLに書き込む
    df.to_sql(table, con=engine, if_exists='append', index=False)