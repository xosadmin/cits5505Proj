from flask import *
import sqlite3
import datetime as dt
from sqlmodels import *
import randomprofile as rp

app = Flask(__name__)

DATABASE = 'database/main.db'

def get_db():
    dbconnect = getattr(g, '_database', None)
    if dbconnect is None:
        dbconnect = g._database = sqlite3.connect(DATABASE)
    return dbconnect

def checkEmail(email):
    getdb = get_db()
    cursor = getdb.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?",(email,))
    result = cursor.fetchone()
    if result is not None: # If email is exists in the system
        return -1
    else:
        return 0

def getThreadTitle(id):
        getdb = get_db()  # Create an object to connect to the database
        cursor = getdb.cursor()  # Create a cursor to interact with the DB
        cursor.execute("SELECT title FROM community WHERE threadID=?",(id,))
        result = cursor.fetchone()
        return result[0] # Remove ('')

def getCoins(id):
        try:
            getdb = get_db()  # Create an object to connect to the database
            cursor = getdb.cursor()  # Create a cursor to interact with the DB
            cursor.execute("SELECT coins FROM users WHERE userID=?",(id,))
            result = cursor.fetchone()
            return result[0] # Remove ('')
        except Exception as e:
            print("[ERROR] getCoins: " + str(e))
            return -1
    
def setCoins(id,amount,act):
        try:
            currentCoins = getCoins(id)
            if act == "plus":
                newCoinAmount = int(currentCoins) + int(amount)
            elif act == "minus":
                newCoinAmount = int(currentCoins) - int(amount)
            else:
                newCoinAmount = int(currentCoins) # Unknown action
            getdb = get_db()  # Create an object to connect to the database
            cursor = getdb.cursor()  # Create a cursor to interact with the DB
            cursor.execute("UPDATE users SET coins=? WHERE userID=?",(newCoinAmount,id))
            getdb.commit()
        except Exception as e:
            print("[ERROR] setCoins: " + str(e))
        
def getRequestInfo(requestID,action):
        getdb = get_db()  # Create an object to connect to the database
        cursor = getdb.cursor()  # Create a cursor to interact with the DB
        if action == "userID":
            cursor.execute("SELECT userID FROM requests WHERE requestID=?",(requestID,))
        elif action == "state":
            cursor.execute("SELECT status FROM requests WHERE requestID=?",(requestID,))
        elif action == "rewards":
            cursor.execute("SELECT rewards FROM requests WHERE requestID=?",(requestID,))
        else:
            print("[ERROR] getRequestInfo: Invalid action!")
            return -1
        result = cursor.fetchone()
        return result[0]

def getUserInfo(userID, action):
        print("[Info] getUserInfo: executing action " + action)
        getdb = get_db()  # Create an object to connect to the database
        cursor = getdb.cursor()  # Create a cursor to interact with the DB
        if action == "email":
            cursor.execute("SELECT email FROM users WHERE userID=?", (userID,))
        elif action == "coins":
            cursor.execute("SELECT coins FROM users WHERE userID=?", (userID,))
        elif action == "avatar":
            cursor.execute("SELECT avatar FROM users WHERE userID=?", (userID,))
        else:
            return None
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            print("[ERROR] getUserInfo: Invalid action or Null Value!")
            return None

def setPassword(id,password):
        try:
            getdb = get_db()  # Create an object to connect to the database
            cursor = getdb.cursor()  # Create a cursor to interact with the DB
            cursor.execute("UPDATE users SET password=? WHERE userID=?",(password,id))
            getdb.commit()
        except Exception as e:
            print("[ERROR] setPassword: " + str(e))

def setPinCode(id,pincode):
        try:
            getdb = get_db()  # Create an object to connect to the database
            cursor = getdb.cursor()  # Create a cursor to interact with the DB
            cursor.execute("UPDATE users SET pincode=? WHERE userID=?",(pincode,id))
            getdb.commit()
        except Exception as e:
            print("[ERROR] setPinCode: " + str(e))

def getItemInfo(itemID, action):
        print("[Info] getItemInfo: executing action " + action)
        getdb = get_db()  # Create an object to connect to the database
        cursor = getdb.cursor()  # Create a cursor to interact with the DB
        if action == "name":
            cursor.execute("SELECT itemName FROM shop WHERE itemID=?", (itemID,))
        elif action == "detail":
            cursor.execute("SELECT itemDetail FROM shop WHERE itemID=?", (itemID,))
        elif action == "price":
            cursor.execute("SELECT price FROM shop WHERE itemID=?", (itemID,))
        else:
            return None
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            print("[ERROR] getItemInfo: Invalid action or Null Value!")
            return None