# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: C:\Users\diana_aimbetova\PycharmProjects\tagcounter\venv\Scripts\db_worker.py
# Compiled at: 2020-11-08 18:27:11
# Size of source mod 2**32: 2036 bytes
import sqlite3
from datetime import date

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        print('Get connected to SQLite...')
        return conn
    except sqlite3.Error as e:
        try:
            print(e)
        finally:
            e = None
            del e

    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS tags\n                          (site_name,url,date,tags)\n                       ')
        print('Getting cursor...')
    except sqlite3.Error as e:
        try:
            print(e)
        finally:
            e = None
            del e

    return cursor


def insert_tags(site_name, url, tags):
    try:
        try:
            conn = create_connection()
            cursor = create_table(conn)
            sqlite_insert_with_param = 'INSERT INTO tags\n                                 (site_name, url, date, tags) \n                                 VALUES (?, ?, ?, ?);'
            data_tuple = (site_name, url, str(date.today()), str(tags))
            cursor.execute(sqlite_insert_with_param, data_tuple)
            conn.commit()
            print('Data is successfully inserted into table...')
        except sqlite3.Error as e:
            try:
                print(e)
            finally:
                e = None
                del e

    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def select_tags(url):
    try:
        try:
            conn = create_connection()
            cursor = create_table(conn)
            sqlite_select_query = 'SELECT * from tags WHERE url = ?'
            cursor.execute(sqlite_select_query, (url,))
            records = cursor.fetchall()
            print('Total rows are:  ', len(records))
            print('Printing each row')
            for row in records:
                print('Site_name: ', row[0])
                print('URL: ', row[1])
                print('Date: ', row[2])
                print('Tags: ', row[3])
                print('\n')

            cursor.close()
        except sqlite3.Error as e:
            try:
                print(e)
            finally:
                e = None
                del e

    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')