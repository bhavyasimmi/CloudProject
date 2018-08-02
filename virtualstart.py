#!/usr/bin/python2
import cgi
import commands

print("Content-type:text/html\n")
print(" ")

form  =  cgi.FieldStorage()
cname =  form.getvalue('x')

o = commands.getstatusoutput("sudo virsh start {}".format(cname))

if o[0] == 0:
	print("location: docker-manage.py")
	print("")


else:
	print("location: docker-manage.py")
	print("")
