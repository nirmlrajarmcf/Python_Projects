# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 00:09:03 2021

@author: Nirmalkumar Rajendran
"""

import tweepy
from datetime import datetime as dtm
from app_DB_Classes import db_operation

class timeline:
    
    def __init__(self):

        self.consumer_key="lbe5LAKb04KjiVmxAR5F8ch2d"
        self.consumer_secret="gLEpr6eCElwOmcCg0xqdElWYkmEnJJCXQaGHr718CiF2yERwfc"
        self.access_token="926877021505855488-GuXexCVAC1WFvZzN8ft3fvm0v13MAPu"
        self.access_token_secret="a7x8xD42aBt6XQgr52nzKKv5KMeuAOKrcx4bxAU9atffK"
        
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)       
        
        
    def verify_auth(self):
        try:
            api_o = self.api
            api_o.verify_credentials()
            print("Authentication OK")
        except(Exception) as err:
            print("Error during authentication")
            print(str(err))
            
    def get_user(self,scrn_name):
        
        user=None
        self.user=user
        try:
            api_o = self.api
            user= api_o.get_user(screen_name=scrn_name)            
            print("User Found")
        except(Exception) as err:
            print("User not Found")
            print(str(err))
            
        return user
    
    def insert_tweet(self,scrn_name,count):     
        
        user = self.get_user(scrn_name)
        if( user != None ):            
            timeline = user.timeline(count=count)        
            for tweet in timeline:
                vls=[]
                vls.append(tweet.id_str)
                vls.append(int(dtm.timestamp(tweet.created_at)*1000))
                vls.append(tweet.author.location)
                vls.append(tweet.lang)
                vls.append(tweet.user.name)
                vls.append(tweet.text.replace("'",""))
                
                             
                try:
                    db_O = db_operation()   
                    db_O.insert_tweet(vls)
                    db_O.close()
                except(Exception) as err:
                    print("Insert Failed")
                    print(str(err))
                    
        else:
            print('User Not Found, Can not insert Tweet')

