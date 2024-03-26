import pandas as pd

input_data_dir = 'input_data/'
customers = pd.read_excel(f'{input_data_dir}H+ Sport Customers.xlsx', sheet_name='data')
print(customers.head())
print(len(customers))
unique_columns = ['FirstName', 'LastName', 'Email', 'Phone']
customers = customers.drop_duplicates(unique_columns, keep = 'first')
print(len(customers))
print(customers.info())

employees = pd.read_excel(f'{input_data_dir}H+ Sport Employees.xlsx', sheet_name='data')