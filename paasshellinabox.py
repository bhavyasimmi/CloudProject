#!/usr/bin/python2
import cgi,commands,os
print "Content-type:text/html\n"
print ""
web=cgi.FieldStorage()
p=web.getvalue('p')
if p=='python' :
	commands.getoutput('sudo systemctl restart shellinaboxd')
	print "<a href='https://192.168.43.142:4200'>"
	print "UserNname is deeksha and password is redhat to start coding"
	print "</a>"
elif p=='perl' :
        commands.getoutput('sudo systemctl restart shellinaboxd')
        print "<a href='https://192.168.43.142:4200'>"
        print "UserNname is deeksha and password is redhat to start coding"
        print "</a>"
elif p=='ruby' :
        commands.getoutput('sudo systemctl restart shellinaboxd')
        print "<a href='https://192.168.43.142:4200'>"
        print "UserNname is deeksha and password is redhat to start coding"
        print "</a>"

