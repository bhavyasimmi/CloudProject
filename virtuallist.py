#!/usr/bin/python2
import commands,cgi


print("Content-type:text/html\n")
print(" ")


#print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")

list = commands.getoutput("sudo virsh list --all")

flist = list.split("\n")

print("<table align='center' width='90%' border='1'>")

print("""
<tr>
<th>State</th>
<th>Name</th>
<th>start</th>
<th>stop</th>
</tr>
""")

for i in flist[2:]:
	j = i.split()
	print("<tr>")
	
	print("<td>")
	if "shut" in i:
		print("down")
	elif "running" in i:
		print("up")
	else:
		print("unknown")
	print("</td>")
	
	print("<td>")
	print(j[1])
	print("</td>")
	'''
	print("<td>")
	print(j[2])
	print("</td>")
	'''
	
	print("<td>")
	print("<a href='virtualstart.py?x={}'>start</a>".format(j[1]))
	print("</td>")

	print("<td>")
	print("<a href='virtualoff.py?x={}'>stop</a>".format(j[-1]))
	print("</td>")
	print("</tr>")
	


print("</table>")

