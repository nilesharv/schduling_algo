class PCB:
	x=0

	def __init__(self,at,bt,p):
		self.at=at
		self.bt=bt
		self.rt=bt
		self.p=p
		self.tt=0
		self.wt=0
		self.name='p['+str(PCB.x)+']'
		PCB.x=PCB.x+1
	def cal(self,cpu):
		self.tt=cpu-self.at
		self.wt=self.tt-self.bt
		return

	def __str__ (self):
		return self.name+'\t|'+str(self.tt)+'\t|'+str(self.wt)+'\t|';


x=int(input('number of process : '))

process=[]
final=[]
remain=x
wt=0
tt=0
flag=False

for i in range(0,x):
	print('p['+str(i)+']')
	at=int(input('AT: ')) 
	bt=int(input('BT: ')) 
	p=int(input('P: ')) 
	process.append(PCB(at,bt,p))
final.append('\n\nP name\t| TT\t| WT\t|')
p=-1;
print('\n\n------gannt chart----\n\n')
cpu_cycle=process[0].at;
while remain!=0:
	current=-1
	i=0
	while i < x and process[i].at<=cpu_cycle:
		if current==-1 and process[i].rt!=0:
			current=i
		elif process[i].p<process[current].p and process[i].rt!=0:
			current=i  		
	
		i=i+1
	if current==-1:
		cpu_cycle=cpu_cycle+1
		print('|i-'+str(cpu_cycle)+'|',end='')
		continue

	process[current].rt=process[current].rt-1
	cpu_cycle=cpu_cycle+1

	
	if process[current].rt==0 and p!=current:
		print(process[p].name+'|'+str(cpu_cycle-1)+'|',end='')
		print(process[current].name+'|'+str(cpu_cycle)+'|',end='')
		p=-1
	elif process[current].rt==0 :
		print(process[current].name+'|'+str(cpu_cycle)+'|',end='')
		p=-1
	elif p!=current:
		print(process[p].name+'|'+str(cpu_cycle-1)+'|',end='')
		p=current
	elif p==-1:
		p=current

	if process[current].rt==0:
		remain=remain-1
		process[current].cal(cpu_cycle)
		final.append(process[current])
		wt=wt+process[current].wt
		tt=tt+process[current].tt
	

final.append('-------------------------------------')
final.append('avg:\t'+str(tt/x)+'\t'+str(wt/x)+'\t')

for i in final:
	print(i)





	
	
