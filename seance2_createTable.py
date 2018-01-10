# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:35:25 2018

@author: segom
"""

import psycopg2
from config import config

def createTable ():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE followers (
            followers_id SERIAL PRIMARY KEY,
            followers_numbers BIGINT(),
            followers_date DATETIME() NOT NULL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        # create table one by one
        for command in commands:
            cur.execute(command)
            
        # close communication with the PostgreSQL database server
        cur.close()
        
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
if __name__ == '__main__':
    createTable()