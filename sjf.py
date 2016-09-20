#sjf

class PCB:
	x=0
	def __init__(self,at,bt):
		self.bt=bt
		self.at=at
		self.rt=bt
		self.wt=0
		self.tt=0
		self.name='P['+str(PCB.x)+']'
		PCB.x=PCB.x+1
	def __str__ (self):
		return self.name+'\t'+str(self.tt)+'\t'+str(self.wt)+'\t'

	def final(self,cpu):
		self.wt=cpu-self.bt-self.at
		self.tt=cpu-self.at
		return


x=int(input("enter number of process: "))

final=[]
process=[]
cpu_cycle=0
waiting_time=0
flag=False
count=0
remain=x
turn_around=0
total_waiting=0
for i in range(0,x):
	at=int(input("enter arival time for p["+str(i)+"]"))
	bt=int(input("enter burst time for p["+str(i)+"]"))
	process.append(PCB(at,bt))
print('\n\n gannt chart')


for i in range(0,x):
	for j in range(1,x-i):
		if process[j].bt<process[j-1].bt:
			process[j],process[j-1]=process[j-1],process[j]

#for i in range(0,x):
#	print(process[i].name,process[i].at,' ',process[i].bt)

cpu_cycle=0
final.append('\n\nP..\tTT\tWT\t')
j=0
run=False
while remain!=0:
		
	if process[count].at<=cpu_cycle and process[count].rt>0 :
		cpu_cycle=cpu_cycle+process[count].rt
		process[count].rt=0
		print('p['+str(count)+']|'+str(cpu_cycle)+'|',end='')
		flag=True
		run=True

	if flag==True:
		remain=remain-1
		process[count].final(cpu_cycle)
		final.append(process[count])
		#print(process[count])
		turn_around=turn_around+process[count].tt
		waiting_time=waiting_time+process[count].wt
		count=0
		flag=False
		continue
		
	
		
	count=count+1
	if count==x:
		
		count=0
		if run==False:
			cpu_cycle=cpu_cycle+1
			print('|-|',end='')
		run=False

print('\n\n')
final.append('\navg:\t'+str(turn_around/x)+'\t'+str(waiting_time/x)+'\t')

for i in final:
	print(i)





		
