import pandas as pd
import duckdb

def main():
    input_data_dir = 'input_data/'
    products = pd.read_excel(f'{input_data_dir}H+ Sport Products.xlsx', sheet_name='Sheet1')
    products['price_euro'] = products['Price'] * 0.92

    with duckdb.connect('transformed_data/hsport.db') as con:
        con.sql("CREATE or replace TABLE products AS SELECT * FROM products")

