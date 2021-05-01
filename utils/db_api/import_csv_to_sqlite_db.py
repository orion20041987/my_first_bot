# --C:\Users\Олег\PycharmProjects\my_first_bot\data


# -- CREATE TABLE blocks (

# -- 	switchgear_id INTEGER,
# -- 	switchgear_name TEXT,
# -- 	element_id INTEGER,
# -- 	element_name TEXT,
# -- 	component_id INTEGER,
# -- 	component_name TEXT,
# -- 	conditions TEXT

# -- );

# -- SELECT * FROM blocks


import csv
import sqlite3


con = sqlite3.connect("blocking_conditions_db.db")  # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE blocking_conditions (switchgear_id TEXT, switchgear_name TEXT, element_id TEXT, "
            "element_name TEXT, component_id TEXT, component_name TEXT, switchgear_status TEXT, conditions TEXT);")
insert_query = "INSERT INTO blocking_conditions (switchgear_id, switchgear_name, element_id, " \
               "element_name, component_id, component_name, switchgear_status, conditions) VALUES (?, ?, ?, ?, ?, ?," \
               " ?, ?); "


with open('blocking_conditions.csv', 'r') as file:  # `with` statement available in 2.5+
    dr = csv.reader(file, delimiter=';')  # comma is default delimiter

    for raw in dr:
        # print(f'{raw["switchgear_name"]}, {raw["element_name"]}, {raw["component_name"]}')
        print(raw)
        cur.execute(insert_query, raw)

con.commit()
con.close()
