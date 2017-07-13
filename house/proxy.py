#-*-coding=utf-8-*-
import sqlite3
import urllib2

def create_proxy():
    dbname="proxy.db"
    try:
        conn=sqlite3.connect(dbname)
    except:
        print "Error to open database%" %self.dbname
    c = conn.cursor()
    query_cmd='''
    select IP,PORT from PROXY;
    '''
    cursor=c.execute(query_cmd)
    (IP,PORT) = c.fetchone()
    print IP+":"+PORT
    proxy={'http':IP+':'+PORT}
    print proxy
    proxy_support=urllib2.ProxyHandler(proxy)
    opener=urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
