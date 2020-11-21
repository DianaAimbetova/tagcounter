import sqlite3
from datetime import datetime
import logging

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        logging.info(str(datetime.now()) + ' Get connected to SQLite...')
        return conn
    except sqlite3.Error as e:
        try:
            logging.error(str(datetime.now()()) + e)
        finally:
            e = None
            del e

    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS tags\n                          '
                       '(site_name,url,date,tags)\n                       ')
        logging.info(str(datetime.now()) + ' Getting cursor...')
    except sqlite3.Error as e:
        try:
            logging.error(str(datetime.now()) + e)
        finally:
            e = None
            del e

    return cursor


def insert_tags(site_name, url, tags):
    code = 200
    try:
        try:
            conn = create_connection()
            cursor = create_table(conn)
            sqlite_insert_with_param = 'INSERT INTO tags\n                                 ' \
                                       '(site_name, url, date, tags) \n                                 ' \
                                       'VALUES (?, ?, ?, ?);'
            data_tuple = (site_name, url, str(datetime.now()), str(tags))
            cursor.execute(sqlite_insert_with_param, data_tuple)
            conn.commit()
            logging.info(str(datetime.now()) + ' Data is successfully inserted into table...')
            return code
        except sqlite3.Error as e:
            try:
                logging.error(str(datetime.now()) +'\n'+ e)
                return 500
            finally:
                e = None
                del e

    finally:
        if conn:
            conn.close()
            logging.info(str(datetime.now()) + ' The SQLite connection is closed')


def select_tags(url):
    result = ''
    try:
        try:
            conn = create_connection()
            cursor = create_table(conn)
            sqlite_select_query = 'SELECT * from tags WHERE url = ?'
            cursor.execute(sqlite_select_query, (url,))
            records = cursor.fetchall()
            result += 'Total rows are:  ' + str(len(records)) + '\n'
            for row in records:
                result += 'Site_name: '+ str(row[0]) + '\n'
                result += 'URL: '+ str(row[1]) + '\n'
                result += 'Date: ' + str(row[2]) + '\n'
                result += 'Tags: ' + str(row[3]) + '\n'


            cursor.close()
            return result
        except sqlite3.Error as e:
            try:
                logging.error(str(datetime.now()) + '\n' + e)
                return e
            finally:
                e = None
                del e

    finally:
        if conn:
            conn.close()
            logging.info(str(datetime.now()) + ' The SQLite connection is closed')
            return str(result)