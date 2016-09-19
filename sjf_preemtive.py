#SJF priority

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
		return self.name+'\t'+str(self.bt)+'\t'+str(self.at)+'\t'

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
	#print(at,bt)
	process.append(PCB(at,bt))


for i in range(1,x):
	if process[i].at<process[i-1].at:
		process[i],process[i-1]=process[i-1],process[i]

p=-1;
final.append('P..\tTT\tWT\t')
j=0
print('gannt chart')
while remain!=0:
	#print(cpu_cycle)
	smallest=-1;
	i=0;
	while i < x and process[i].at<=cpu_cycle:
		if smallest==-1 and process[i].rt!=0:
			smallest=i
		elif process[i].rt<process[smallest].rt and process[i].rt!=0:
			smallest=i
		i=i+1
	
	process[smallest].rt=process[smallest].rt-1
	
	cpu_cycle=cpu_cycle+1
	if p==-1:
		p=smallest
	elif process[smallest].rt==0 :
		print(process[smallest].name+'|'+str(cpu_cycle)+'|',end='')
		p=-1
	elif p!=smallest:
		print(process[p].name+'|'+str(cpu_cycle-1)+'|',end='')
		p=smallest

	if process[smallest].rt==0:
		process[smallest].final(cpu_cycle)
		final.append( process[smallest].name+'\t'+str(process[smallest].tt)+'\t'+str(process[smallest].wt)+'\t')
		waiting_time=waiting_time+process[smallest].wt
		turn_around=turn_around+process[smallest].tt
		remain=remain-1

final.append('avg\t'+str(turn_around/x)+'\t'+str(waiting_time/x)+'\t')
print('\n\n\n')
for i in final:
	print(i)



	


		
