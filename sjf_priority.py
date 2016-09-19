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
	if process[i].bt<process[i-1].bt:
		process[i],process[i-1]=process[i-1],process[i]

final.append('P..\tTT\tWT\t')
while remain!=0:
	#print(cpu_cycle)
	if process[count].at<=cpu_cycle and process[count].rt==1:
		process[count].rt=0;
		cpu_cycle=cpu_cycle+1
		flag=True
		process[count].tt=cpu_cycle-process[count].at
		process[count].wt=process[count].tt-process[count].bt
		
	elif process[count].at<=cpu_cycle and process[count].rt>0:
		
		process[count].rt=process[count].rt-1
		cpu_cycle=cpu_cycle+1
		count=0
		continue
		
	if flag is True:
		final.append( process[count].name+'\t'+str(process[count].tt)+'\t'+str(process[count].wt)+'\t')
		count=0
		waiting_time=waiting_time+process[count].wt
		turn_around=turn_around+process[count].tt
		remain=remain-1
		flag=False
		continue
		
	count=count+1
	
	if count is x:
		count=0

final.append('avg\t'+str(turn_around/x)+'\t'+str(waiting_time/x)+'\t')
for i in final:
	print(i)



	


		
