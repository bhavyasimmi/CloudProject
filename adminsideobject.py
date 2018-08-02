#!/usr/bin/python2
import os,commands,cgi,sys
print "Content-type:text/html\n"
print ""
web=cgi.FieldStorage()
disk_name=web.getvalue('diskname')
vg_name=web.getvalue('vgname')
lv_size=web.getvalue('lvsize')
lv_name=web.getvalue('lvname')


commands.getoutput('sudo pvcreate '+disk_name)
commands.getoutput('sudo vgcreate '+vg_name+' '+disk_name)
commands.getoutput('sudo lvcreate --size '+lv_size+'M --thin '+vg_name+'/'+lv_name)
commands.getoutput('sudo cd /var/www/'+'sudo mkdir demo')
os.system('sudo  touch /var/www/demo/demo1.txt')
os.system('sudo chmod 777 /var/www/demo/demo1.txt')
os.system('sudo  touch /var/www/demo/demo2.txt')
os.system('sudo chmod 777 /var/www/demo/demo2.txt')
fh = open("/var/www/demo/demo1.txt","w")
fh.write(vg_name)
fh1 = open("/var/www/demo/demo2.txt","w")
fh1.write(lv_name)
fh.close()
fh1.close()

#print "<form  action='http://192.168.124.1/cgi-bin/clientsideobject.cgi' method='POST'>"
#print '<input type="hidden" name="vg_name1" value="%s">' % (cgi.escape(vg_name),)
#print '<input type="hidden" name="lv_name1" value="%s">' % (cgi.escape(lv_name),)
#print "</form>"

