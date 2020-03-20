from my_sqlite import MySqlite

instance = MySqlite('todo')

instance.create_table()

instance.insert_data('Buy milk')

data = instance.read_data()

for d in data:
    print(d)