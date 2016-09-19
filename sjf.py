#sjf

x=int(input("enter number of process: "))

final=[]
at=[0]*x
bt=[0]*x
rt=[0]*x
cpu_cycle=0
waiting_time=0
flag=False
count=0
remain=x
turn_around=0
total_waiting=0
for i in range(0,x):
	at[i]=int(input("enter arival time for p["+str(i)+"]"))
	bt[i]=int(input("enter burst time for p["+str(i)+"]"))
	rt[i]=bt[i]
print('\n\n gannt chart')


for i in range(1,x):
	if bt[i]<bt[i-1]:
		bt[i],bt[i-1]=bt[i-1],bt[i]
		at[i],at[i-1]=at[i-1],at[i]
		rt[i],rt[i-1]=rt[i-1],rt[i]


final.append('P..\tTT\tWT\t')
while remain!=0:
		
	if at[count]<=cpu_cycle and rt[count]>0:
		cpu_cycle=cpu_cycle+rt[count]
		rt[count]=0
		count=0
		flag=True

	if flag is True:
		remain=remain-1
		final.append('p['+str(count)+']\t'+str(cpu_cycle-at[count])+'\t'+str(cpu_cycle-at[count]-bt[count])+'\t')
		turn_around=turn_around+cpu_cycle-at[count]
		waiting_time=waiting_time+cpu_cycle-at[count]-bt[count]
		flag=False
	count=count+1
	if count==x:
		count=0
	
	
final.append('\navg:\t'+str(turn_around/x)+'\t'+str(waiting_time/x)+'\t')

for i in final:
	print(i)





		
