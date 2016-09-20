

#priority algorithm 

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
wt=0
tt=0
remain=x
sat=-1
for i in range(0,x):
	print('p['+str(i)+']')
	at=int(input('AT: '))
	bt=int(input('BT: '))
	p=int(input('p: '))
	process.append(PCB(at,bt,p))
	if sat==-1:
		sat=at
	elif sat>at:
		sat=at;


for i in range(0,x):
	for j in range(1,x-i):
		
		if process[j].p<process[j-1].p:
			process[j],process[j-1]=process[j-1],process[j]
#for i in range(0,x):
#	print(process[i].name,process[i].at,process[i].bt,process[i].p)
#print(sat)
cpu_cycle=0
print('\ngannt chart\n\n')
final.append('\n------ Table------------\n')
final.append('p name\t| TT \t| BT \t|')
final.append('=========================')
count=0
run=False
while remain!=0:
	

	if process[count].at<=cpu_cycle and process[count].rt>0:
		cpu_cycle=cpu_cycle+process[count].rt;
		process[count].rt=0
		process[count].cal(cpu_cycle)
		remain=remain-1
		final.append(process[count])
		wt=wt+process[count].wt
		tt=tt+process[count].tt
		print(process[count].name+'|'+str(cpu_cycle)+'|',end='')
		run=True
	
	count =count+1

	if count==x:
		count=0
		if run==False:
			cpu_cycle=cpu_cycle+1
			print('|i-'+str(cpu_cycle)+'|',end='')
		run=False


print('\n\n\n')
final.append('=========================')
final.append('avg: \t|'+str(tt/x)+'\t|'+str(wt/x)+'\t|');

for i in final:
	print(i);




















