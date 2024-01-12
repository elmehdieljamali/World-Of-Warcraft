import sqlite3 

CREATE_TABLE_CHARACTER = "CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, name CHAR, life_score INTEGER, arm, type );"
INSERT_CHARACTER=" INSERT INTO characters (name, life_score, arm, type) VALUES (?, ?, ?, ?);"
CREATE_TABLE_ARM =" CREATE TABLE  IF NOT EXISTS arms (id INTEGER PRIMARY KEY, name CHAR, power INTEGER, length INTEGER, weight INTEGER);"
INSERT_ARM=" INSERT INTO arms (name, power, length, weight) VALUES (?, ?, ?, ?);"
CREATE_TABLE_SHIELD = "CREATE TABLE IF NOT EXISTS shields(id INTEGER PRIMARY KEY, name CHAR, defense_power INTEGER, weight INTEGER );"
INSERT_SHIELD = "INSERT INTO shields (name, defense_power, weight) VALUES (?, ?, ?);"
CREATE_TABLE_FOOD = "CREATE TABLE IF NOT EXISTS food (id INTEGER PRIMARY KEY, name CHAR, energy_points INTEGER, weight INTEGER );"
INSERT_FOOD = "INSERT INTO food (name, life_score, energy_points, weight) VALUES (?, ?, ?, ?);"
SELECT_ALL_ARMS =" SELECT * FROM arms ;"
SELECT_ALL_CHARACTERS =" SELECT * FROM characters;"
SELECT_ALL_SHIELDS = "SELECT * FROM shields;"
SELECT_ALL_FOOD = "SELECT * FROM food;"


def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_CHARACTER)
        connection.execute(CREATE_TABLE_ARM)
        connection.execute(CREATE_TABLE_SHIELD)
        connection.execute(CREATE_TABLE_FOOD)

def add_arm(connection, arm_info):
    with connection:
        connection.execute(INSERT_ARM, arm_info)

def add_character(connection, character_info):
    with connection:
        connection.execute(INSERT_CHARACTER, character_info)
    
def add_shield(connection, shield_info):
    with connection:
        connection.execute(INSERT_SHIELD, shield_info)

def add_food(connection, food_info):
    with connection:
        connection.execute(INSERT_FOOD, food_info)

def select_all_arms(connection):
    with connection:
        return connection.execute(SELECT_ALL_ARMS).fetchall()

def select_all_characters(connection):
    with connection:
        return connection.execute(SELECT_ALL_CHARACTERS).fetchall()

def select_all_shields(connection):
    with connection:
        return connection.execute(SELECT_ALL_SHIELDS).fetchall()

def select_all_food(connection):
    with connection:
        return connection.execute(SELECT_ALL_FOOD).fetchall()





