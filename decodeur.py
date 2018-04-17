f=open("catalogue.sql","r")

# ~ f=f.readlines()
L=[]
ml=r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,:;*@()-\'`. éèëê°öôœÉîçà–äü+/\\'
print(ml)
for i in f:
	k=i.replace(r"Ã©",r"é")
	# ~ k=i.replace(r"à¢",r"â")
	k=k.replace(r"\'","''")
	k=k.replace(r"Ã¨",r"è")
	k=k.replace(r"Â°",r"°")
	k=k.replace(r"Ã¶",r"ö")
	k=k.replace(r"Ãª",r"ê")
	k=k.replace(r"Ã¤",r"ä")
	k=k.replace(r"â€“",r"–")
	k=k.replace(r"Ã¼",r"ü")
	k=k.replace(r"Ã§",r"ç")
	k=k.replace(r"Ã´",r"ô")
	k=k.replace(r"Å“",r"œ")
	k=k.replace(r"Ã‰",r"É")
	k=k.replace(r"Ã«",r"ë")
	k=k.replace(r"Ã®",r"î")
	k=k.replace(r"Ã",r"à")
	L.append(k)

print(L[54])
g=open("newcatalogue.py","w")

for i in L:
	for p in i:
		if p not in ml:
			print(p)
	g.write(f"{i}")


