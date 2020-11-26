import csv
import sys
state = input("What is the state :")
state=state.capitalize()
s=[]
imp=open('hotels.csv' , 'r')
out = open('hotels.csv' , 'w')

writer = csv.writer(out)

for row in csv.reader(imp):

    if row[0] =="1000":

        writer.writerow(row)
imp.close()

out.close()




'''

	for i in csv_reader:
		if i[2]==state:
			t.append(i[1])
			s.append(i[2])
			c.append(int(i[3]))
			r.append(float(i[4]))
		elif state=="India" and x!=0:
			t.append(i[1])
			s.append(i[2])
			c.append(int(i[3]))
			r.append(float(i[4]))
		x=x+1

print()
if len(s)==0 and state!="India":
  print("Sorry "+ state+" state not in database try once again.")
  print()
  sys.exit()

d=[]

if cost_rating=="cost":
	if operation=="highest":
		h=0
		for i in range(len(c)):
			if h<c[i]:
				h=c[i]
		for i in range(len(c)):
			if h==c[i]:
				d.append(i)
		for i in d:
			print("Hotel with highest price in "+s[i]+" is "+t[i]+" with price "+str(h))
	elif operation=="cheapest":
		l=c[0]
		for i in range(len(c)):
			if l>c[i]:
				l=c[i]
		for i in range(len(c)):
			if l==c[i]:
				d.append(i)
		for i in d:
			print("Hotel with cheapest price in "+s[i]+" is "+t[i]+" with price "+str(l))
	elif operation=="average":
		a=0
		for i in c:
			a=a+i
		a=round(a/len(c))
		a=c[min(range(len(c)), key = lambda i: abs(c[i]-a))]
		for i in range(len(c)):
			if a==c[i]:
				d.append(i)
		for i in d:
			print("Hotel with Average price in "+s[i]+" is "+t[i]+" with price "+str(a))
	else:
		print("You have typed wrong Operation value, try to spell one of like (cheapest,average,highest).")

elif cost_rating=="rating":
	if operation=="highest":
		h=0
		for i in range(len(r)):
			if h<r[i]:
				h=r[i]
		for i in range(len(r)):
			if h==r[i]:
				d.append(i)
		for i in d:
			print("Highest rating of Hotel in "+s[i]+" is "+t[i]+" with rating "+str(h))
	elif operation=="cheapest":
		l=r[0]
		for i in range(len(r)):
			if l>r[i]:
				l=r[i]
		for i in range(len(r)):
			if l==r[i]:
				d.append(i)
		for i in d:
			print("Cheapest rating of Hotel in "+s[i]+" is "+t[i]+" with rating "+str(l))
	elif operation=="average":
		a=0
		for i in r:
			a=a+i
		a=round(a/len(r),1)
		a=r[min(range(len(r)), key = lambda i: abs(r[i]-a))]
		for i in range(len(r)):
			if a==r[i]:
				d.append(i)
		for i in d:
			print("Average rating of Hotel in "+s[i]+" is "+t[i]+" with rating "+str(a))
	else:
		print("You have typed wrong Operation value, try to spell one of like (cheapest,average,highest).")
else:
	print("You have typed wrong Cost or Rating value, try to spell one of like (cost,rating).")
print()
'''
