#Round Robin program using array


print("how many process you want to enter")

x=int(input())
final=[]
at=[0]*x
bt=[0]*x
rt=[0]*x
cpu_cycle=0
total_waiting=0
flag=False
count=0
remain=x
quantum=int(input("time slice for round robin"))
turn_around=0
total_waiting=0
for i in range(0,x):
	at[i]=int(input("enter arival time for p["+str(i)+"]"))
	bt[i]=int(input("enter burst time for p["+str(i)+"]"))
	rt[i]=bt[i]
print('\n\n gannt chart')

while remain!=0:
	#print(cpu_cycle,count)
	if at[count]<=cpu_cycle and rt[count]>0 and rt[count]<=quantum :
		cpu_cycle=cpu_cycle+rt[count];
		rt[count]=0;
		flag=True;
		print('p['+str(count)+']|'+str(cpu_cycle)+'|',end='')
	elif rt[count]>quantum and at[count]<=cpu_cycle:
		rt[count]=rt[count]-quantum
		cpu_cycle=cpu_cycle+quantum
		print('p['+str(count)+']|'+str(cpu_cycle)+'|',end='')
	
	if flag is True:
		final.append('P['+str(count)+']\t'+str(cpu_cycle-at[count])+'\t'+str(cpu_cycle-at[count]-bt[count])+'\t')
		turn_around=turn_around+cpu_cycle-at[count]
		total_waiting=total_waiting+cpu_cycle-at[count]-bt[count]
		remain=remain-1
		flag=False
	count=count+1
	if count==x :
		count=0

print('',end='\n')
final.append('\navg:\t'+str(turn_around/x)+'\t'+str(total_waiting/x)+'\t')

for i in final:
	print(i)

