#FCFS

class PCB:
	x=0
	def __init__(self,at,bt):
		self.at=at
		self.bt=bt
		self.rt=bt
		self.tt=0
		self.wt=0
		self.name='P['+str(PCB.x)+']'
		PCB.x=PCB.x+1

	def cal(self,cpu):
		self.tt=cpu-self.bt
		self.wt=self.tt-self.at
		return
	def __str__(self):
		return self.name+'\t|'+str(self.tt)+'\t|'+str(self.wt)+'\t|'
	
x=int(input('number of process: '))
process=[]
final=[]
wt=0
tt=0
cpu_cycle=0

for i in range(0,x):
	at=int(input('P['+str(i)+'].AT: '))
	bt=int(input('P['+str(i)+'].BT: '))
	process.append(PCB(at,bt))

for i in range(0,x):
	for j in range(1,x-i):
		if process[j].at<process[j-1].at:
			process[j],process[j-1]=process[j-1],process[j]

run=False
remain=x
print('gannt chart\n\n')
final.append('\np name\t|TT\t|WT\t|')
final.append('-------------------------')
count=0
while remain!=0:
	
	if process[count].at<=cpu_cycle and process[count].rt>0:
		cpu_cycle=cpu_cycle+process[count].rt
		process[count].rt=0
		process[count].cal(cpu_cycle)
		run=True
		wt=wt+process[count].wt
		tt=tt+process[count].tt
		final.append(process[count])
		print(process[count].name+'|'+str(cpu_cycle)+'|',end='')
		remain=remain-1


	count=count+1
	if count==x:
		count=0
		if run is False:
			cpu_cycle=cpu_cycle+1
			print('|i-'+str(cpu_cycle)+'|',end='')
		run=False
final.append('-------------------------')
final.append('avg:\t|'+str(tt/x)+'\t|'+str(wt/x)+'\t|')
	
print('\n\n')
for i in final:
	print(i)


		

