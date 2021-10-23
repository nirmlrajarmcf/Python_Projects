# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:05:37 2021

@author: Nirmalkumar Rajendran
"""

from flask import Flask,request,jsonify
import os
port_no=int(os.getenv('PORT',8082))
app = Flask(__name__)
from app_Helper import login_mthd,get_tweets_by_Date
from app_Helper import save_user_tweets

@app.route('/api/hello_world')
def hello():
    return "hello World !"

@app.route('/api/login', methods=['POST'])
def login():
    
    output={"status":"Failed"}
    try:
        
        data = request.get_json()
        lgn_out = login_mthd(data['username'],data['password'],data['mobile_no'])
        
        if( lgn_out == 'Success' ):
            output={"status":"Success"}
            print( 'Login Sucess !!!')
        
    except(Exception) as err:
        print( 'Login Failed !!!')
        print(str(err))
        
    return jsonify(output)

@app.route('/api/get_tweet_by_Date', methods=['POST'])
def get_tweet_by_Date():
    
    output={"status":"Failed"}
    try:
        
        data = request.get_json()          
        twt_out = get_tweets_by_Date(data['fromDate'],data['toDate'],data['ascnd'])

        if( twt_out != None ):
           output=twt_out
        
    except(Exception) as err:
        print( 'get by date Failed !!!')
        print(str(err))
        
    return output

@app.route('/api/save_tweets_user', methods=['POST'])
def save_tweets_user():
    
    output={"status":"Failed"}
    try:
        
        data = request.get_json()        
        save_user_tweets(data['screen_name'],data['count'])
        output={"status":"Success"}
        
    except(Exception) as err:
        print( 'get by date Failed !!!')
        print(str(err))
        
    return output

app.run(host='0.0.0.0',port=port_no, debug=True)