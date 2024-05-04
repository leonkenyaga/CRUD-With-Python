# app.py
from flask import Flask, request, jsonify
import user

app = Flask(__name__)

@app.get("/getUser")
def get_countries():
    print("getting 🚀")
    user.PrintUser(newUser)
    return account

@app.post("/postUser")
def add_country():
    print("posting 🚀")
    if request.is_json:
        global newUser, account
        account = request.get_json()    
        newUser = user.User(account["name"], account["password"], account["email"], account["friends"])
        user.PrintUser(newUser)
        return account, 201
    return {"error": "Request must be JSON"}, 415

