list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
l=[]
for i in range(len(list1)):
	try:
		l.append(list1[i]+""+list2[-1-i])
	except:
		if(list1[i]!=None):
			l.append(list1[i])
		else:
			l.append(list2[i])

print(" ".join(l))
