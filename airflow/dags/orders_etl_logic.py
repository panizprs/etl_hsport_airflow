import pandas as pd
import duckdb

def main():
    input_data_dir = 'input_data/'
    orders = pd.read_excel(f'{input_data_dir}H+ Sport Orders.xlsx', sheet_name='data')
    columns = ['OrderID', 'Date', 'TotalDue', 'Status', 'CustomerID', 'SalespersonID']
    orders = orders[columns]
    with duckdb.connect('transformed_data/hsport.db') as con:
        con.sql("CREATE or replace TABLE orders AS SELECT * FROM orders")
