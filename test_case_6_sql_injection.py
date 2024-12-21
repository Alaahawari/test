# SQL Injection Example
import sqlite3

def get_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(query)
    # Not secure, vulnerable to SQL Injection

get_user("admin'; DROP TABLE users; --")
