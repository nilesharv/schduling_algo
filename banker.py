#banker's algorithm

def isunder(a1,a2):
	for i in range(1,len(a1)):
		if a1[i]>a2[i-1]:
			return False
		
	return True


n=int(input("Enter number of process : "))

allocated=[]
for i in range(0,n):
	inpu=[int(z) for z in input().split()]
	allocated.append(inpu);

input();
maximum=[]
for i in range(0,n):
	inpu=[int(z) for z in input().split()]
	maximum.append(inpu)
need=[]
for i in range(0,n):
	need.append(maximum[i])
	for j in range(1,len(allocated[i])):
		need[i][j]=need[i][j]-allocated[i][j]
	
print('\nallocation  ,maximum\np\tA\tB\tC\t p\tA\tB\tC');
for i in range(0,n):
	print(allocated[i],maximum[i],need[i])
input();

avail=[int(x) for x in input().split()]

print(avail)

remain=n
finish=[False]*n
flag=False
i=0
while remain!=0:
	#print(need[i],avail)
	if isunder(need[i],avail) and finish[i]==False:
		for j in range(0,len(avail)):
			avail[j]=avail[j]+allocated[i][j+1]
		print('P['+str(i)+']-->',end='')
		finish[i]=True
		remain=remain-1
		flag=True
	
	i=i+1
	if i==n:
		i=0
		if flag==False:
			print('System is in deadlock condition')
			break;
		flag=False

	#print(remain)



