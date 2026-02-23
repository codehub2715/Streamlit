#database

import sqlite3
import streamlit as st

con = sqlite3.connect('data.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(name TEXT, age INT)')

name = st.text_input('Name')
age = st.number_input('Age', 1, 100)
if st.button('Save'):
    cursor.execute('INSERT INTO users VALUES(?,?)', (name, age))
    con.commit()
    st.write('Data Saved')