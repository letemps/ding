#!/usr/bin/env python
import web
import time
import datetime
import sqlite3
 
count = 0

urls=(
    '/fastcgi/desktop/?', 'desktop',
    '.*', 'index',
)
 
app=web.application(urls, globals())
 
class index:
    def __init__(self):
        self.times = 0
    
    def GET(self):
        return "Hello, world!"

    def POST(self):
        global count
        count += 1
        i = web.input()
        self.times += 1
        time.sleep( 0.1 )
        return "Hello, " + i.get( "a" ) + " --------" + str( self.times )

class desktop:
    def GET(self):
        content="template!"
        render = web.template.render('templates/') 
        return render.main(content)
 
if __name__=="__main__":
    web.wsgi.runwsgi=lambda func,addr=None: web.wsgi.runfcgi(func,addr)
    app.run()

