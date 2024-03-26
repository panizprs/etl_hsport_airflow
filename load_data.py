import pandas as pd
import duckdb

input_data_dir = 'input_data/'
customers = pd.read_excel(f'{input_data_dir}H+ Sport Customers.xlsx', sheet_name='data')
unique_columns = ['FirstName', 'LastName', 'Email', 'Phone']
customers = customers.drop_duplicates(unique_columns, keep = 'first')

employees = pd.read_excel(f'{input_data_dir}H+ Sport Employees.xlsx', sheet_name='Employees')
columns_to_drop = [0.0291]
employees = employees.drop(columns = columns_to_drop)

with duckdb.connect('transformed_data/hsport.db') as con:
    con.sql('''CREATE or replace TABLE customers AS SELECT * FROM customers''')
    con.sql('''CREATE or replace TABLE employees AS SELECT * FROM employees''')

    print(con.sql('''select * from employees limit 5'''))