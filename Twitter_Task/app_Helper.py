# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:27:52 2021

@author: Nirmalkumar Rajendran
"""

from app_login_Classes import twitter
from app_DB_Classes import db_operation
import json
from app_timeline_classes import timeline

def login_mthd(username,password,mobile_no):
    
    status = None
    try:
        
        obj_t = twitter(username,password,mobile_no)
        obj_t.login()
        status = 'Success'
        
    except(Exception) as err:
        print(str(err))
            
    return status
        

def get_tweets_by_Date(fromDate,toDate,ascnd=True):
    
    out = None
    
    try:
        db_O = db_operation()         
        tw_out= db_O.get_tweet_by_date(fromDate, toDate, ascnd)
        db_O.close()
        
        rslt=[]
        for i in range(len(tw_out)):            
            itw = tw_out[i]
            tmp={"Date":itw[0],"Author":itw[1],"Tweet":itw[2]}
            rslt.append(tmp)
        out={"result":json.loads(json.dumps(rslt))}
            
    except(Exception) as err:
        print(str(err))
            
    return out

def save_user_tweets(scrn_name,count):
    
    out = None
    
    try:
        
        api_O = timeline()
        api_O.insert_tweet(scrn_name,count)       
                    
    except(Exception) as err:
        print(str(err))
            
    return out
