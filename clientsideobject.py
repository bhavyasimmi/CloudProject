#!/usr/bin/python2
import os,commands,cgi,sys
print "Content-type:text/html\n"
print ""

web=cgi.FieldStorage()
drive_name=web.getvalue('dn')
drive_size=web.getvalue('dz')
button_name=web.getvalue('submit')


fh = open("/var/www/demo/demo1.txt","r")
	#fh.write(vg_name)

dd=fh.read()
#print dd
fh.close()
fh1 = open("/var/www/demo/demo2.txt","r")
ddl=fh1.read()
#print ddl

fh1.close()

button_name1=web.getvalue('DeleteStorage')


x=commands.getoutput('hostname -I')
ip=x.split(' ')
commands.getoutput('sudo lvcreate  --name  '+drive_name+'  -V'+drive_size+'M   --thin  '+dd+'/'+ddl)
#commands.getoutput('sudo lvcreate  --name  '+drive_name+'  -V'+drive_size+'M     '+dd)
commands.getoutput('sudo mkfs.xfs    /dev/'+dd+'/'+drive_name )
commands.getoutput('sudo mkdir  /mnt/'+drive_name)
commands.getoutput('sudo mount  /dev/'+dd+'/'+drive_name+'       /mnt/'+drive_name)

nfs="/mnt/"+drive_name+"  *{rw,no_root_squash}\n"
x=open('/etc/exports','a')
x.write(nfs)
x.close()

commands.getoutput('sudo exportfs -r')
#commands.getoutput('sudo touch /mnt/'+drive_name+' >/'+drive_name+'.sh')
#commands.getoutput('sudo cd  /mnt/'+drive_name+' && sudo touch '+drive_name+'.sh')

commands.getoutput('sudo touch /mnt/'+drive_name+'/'+drive_name+'.sh')

#n=drive_name+'.sh'
commands.getoutput('sudo chmod o+w /mnt/'+drive_name+'/'+drive_name+'.sh')
commands.getoutput('sudo chmod +x /mnt/'+drive_name+'/'+drive_name+'.sh')
commands.getoutput('sudo chmod 777 /mnt/'+drive_name+'/'+drive_name+'.sh')
commands.getoutput('sudo echo "mkdir /mnt/{}" > /mnt/{}/{}.sh'.format(drive_name,drive_name,drive_name))
commands.getoutput('sudo echo mount {}:/mnt/{}  /mnt/{} >> /mnt/{}/{}.sh'.format(ip[0],drive_name,drive_name,drive_name,drive_name))




print commands.getoutput('sudo tar cfv /var/www/html/{}.tar /mnt/{}/{}.sh'.format(drive_name,drive_name,drive_name))
commands.getoutput('sudo chmod 777  /var/www/html/{}.tar'.format(drive_name))





#m1="<meta HTTP-EQUIV='refresh' content='0;url=/var/www/html/{}.tar'/>".format(drive_name)
#print m1
 
print """Content-type:text/html\n
<html>
<body>
<p>Your Storage Is Sucessfully Generated</p>"""

print "<a href='http://192.168.122.227/"+drive_name+".tar'>GO TO Your Storage</a>"
"""
</body>
</html>
      """


