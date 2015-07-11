#!/usr/bin/python

import sqlite3
from _config import DATABASE_PATH 

with sqlite3.connect(DATABASE_PATH) as connection : 
	c = connection.cursor()

	c.execute("""CREATE TABLE tasks()"""
		)