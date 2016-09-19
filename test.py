class pcb:
	x=0
	def __init__(self,at,bt):
		self.bt=bt
		self.at=at
		self.rt=bt
		self.wt=0
		self.tt=0
		self.name='P['+str(pcb.x)+']'
		pcb.x=pcb.x+1
	def __str__ (self):
		return self.name+'\t'+str(self.bt)+'\t'+str(self.at)+'\t'

	def final(self,cpu):
		self.wt=cpu-self.bt-self.at
		self.tt=cpu-self.at
		return


process=[]
process.append(pcb(2,10))
process.append(pcb(0,5))
process.append(pcb(1,7))
process.append(pcb(5,8))



for i in range(1,4):
	if process[i].bt<process[i-1].bt:
		process[i],process[i-1]=process[i-1],process[i]


for i in process:
	print(i)
