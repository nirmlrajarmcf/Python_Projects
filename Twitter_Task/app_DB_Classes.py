# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 01:16:54 2021

@author: Nirmalkumar Rajendran
"""

import psycopg2

class db_operation:
    
    def __init__(self):
        
        self.conn=psycopg2.connect('dbname=learn user=postgres password=root port=5432 application_name=python')
        self.cur=self.conn.cursor()
        
    def close(self):
        self.cur.close()
        self.conn.close()
    def commit(self):
        self.conn.commit()
    def run_query(self,qry):
        self.cur.execute(qry)
    def fetchall(self):
        return self.cur.fetchall()
    
    def check_tweet_id(self,id):
        
        new = False
        slct_qry = '''SELECT COUNT(*) FROM public.tweet_timeline
                        WHERE tweet_id_str='{}'
                        '''.format(id)
        self.run_query(slct_qry) 
        out = self.fetchall()[0][0]    
        #self.close()
        if( out== 0):
            new = True            
        return new

               
    def insert_tweet(self,vls):
        
        if( self.check_tweet_id(vls[0]) ):
            inrt_qry = '''INSERT INTO public.tweet_timeline(
                	tweet_id_str,created_date,auth_location, tweet_lang,author,tweet_text)
                	VALUES ('{}', {}, '{}', '{}', '{}', '{}');
                '''.format(vls[0],vls[1],vls[2],vls[3],vls[4],vls[5])                
                        
            self.run_query(inrt_qry)    
            self.commit()        
            #self.close()
            print('tweet is new')
            
        else:
            print('tweet already in DB')
            
    def get_tweet_by_date(self,fromDate,toDate,ascnd):
        out = None
        if( ascnd ):
            slct_qry = '''SELECT created_date,author,tweet_text FROM public.tweet_timeline
                            WHERE created_date>={} and created_date<={}
                            ORDER BY created_date
                            '''.format(fromDate,toDate)
        else:
            slct_qry = '''SELECT created_date,author,tweet_text FROM public.tweet_timeline
                            WHERE created_date>={} and created_date<={}
                            ORDER BY created_date DESC
                            '''.format(fromDate,toDate)
        
        self.run_query(slct_qry) 
        out = self.fetchall()
        #self.close()
        
        return out
        
            