p = open("c_program.ps1","r")
x=p.read()
p.close()
lol=""
for poo in x.splitlines():
	if "Write-Progress" not in poo and "eb" not in poo:
		lol+=poo
		lol+="\n"

f=open("ps2.ps1","w")
f.write(lol)
f.close()
