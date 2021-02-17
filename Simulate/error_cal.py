z=input('Give the name of Experimental Entity : ')
n=int(input('No of Set : '))
Y=[]
for i in range(n):
    y=float(input('{}[{}] -- Value : '.format(z,i)))
    Y.append(y)
s=0.0
for i in range(n):
    s=s+Y[i]
s=s/n
print('Avg. Value of Data of {} : '.format(z),s)
#Calculation for maximum percentage error: 
#ds=?
#( Empty  for More Information )
#max_error= (ds/s)*100