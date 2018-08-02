#!/usr/bin/python2
import os,commands,cgi
print "Content-type:text/html\n"
print ""
web=cgi.FieldStorage()
drive_name=web.getvalue('drivename')
button=web.getvalue('submit')
commands.getoutput('sudo lvchange -an cloud')
commands.getoutput('sudo lvremove /dev/cloud/'+drive_name)
commands.getoutput('sudo cd /var/www/html/storage/'+'sudo rmdir'+drive_name)
