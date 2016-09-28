#include<stdio.h>
#define MAX 15
#define p(a) printf("%d ",a)
#define NL printf("\n")
#define INPUT(a) scanf("%d",&a)
#define msg(a) ;//printf("%d break point\n",a);
struct PCB
{
int pid;
int Allocation[MAX];
int Need[MAX];
int Max[MAX];
};
int x=1;
typedef struct PCB PCB;

PCB process[MAX];
int Avialable[MAX];
void input(int,int);
void display(int,int);

									int isLess(int a[],int b[],int n)
									{
									int i;
			msg(444);
									for(i=0;i<n;i++)
									{
									msg(i);
				
									if(a[i]>b[i])
									return 0;
									}
									return 1;
									}	

									int copy(int a[],int b[],int n)
									{
									int i;
									for(i=0;i<n;i++)
									{
									a[i]=b[i];
									}
									}	
											void sum(int a[],int b[],int n)
											{int i;
											for(i=0;i<n;i++)
											{
											a[i]+=b[i];
											}
											}
										void subtract(int a[],int b[],int n)
											{int i;
											for(i=0;i<n;i++)
											{
											a[i]-=b[i];
											}
											}
											void show(int m[],int n)
											{int i;
											for(i=0;i<n;i++)
											p(m[i]);
											NL;
											}
	
int safetyAlgo(int n,int m)
{
int i=0;
int remain=n;
int finish[MAX]={0};
int work[MAX];
copy(work,Avialable,m);
//show(work,m);
int flag=0;
while(remain!=0)
{
msg(111);
	/*step 2 if no then goto 3*/
//show(process[i].Need,m);
		if(isLess(process[i].Need,process[i].Need,m))
		{	
			finish[i]=1;
			sum(Avialable,process[i].Allocation,m);
			remain--;
			flag=1;
		}
		i++;
		if(i==n)
		{
			i=0;
			if(flag==0)
			return 0;
		flag=0;			
		}
}
return 1;
}
void banker(int n,int m)
{
int request[MAX];
int i=0;
int op=1;
int p;
//freopen("/dev/stdin", "r", stdin);
while(op)
{
printf("enter process number ");
INPUT(p);
printf("enter resource");
for(i=0;i<m;i++)
INPUT(request[i]);
if(isLess(request,process[p].Need,m))
{
		if(isLess(request,Avialable,m))
		{
		subtract(process[p].Need,request,m);
		subtract(Avialable,request,m);
		sum(process[p].Allocation,request,m);
		if(safetyAlgo(n,m))
		{printf("\nno dead lock\n");}
		else
		{
		printf("\nrequest rollback\n");
		sum(process[p].Need,request,m);
		sum(Avialable,request,m);
		subtract(process[p].Allocation,request,m);
		}
		}

			
}
printf("request more ..\n1 Yes ,0 No\ninput: ");
INPUT(op);
}




}

							int main()
							{
					freopen("input.txt","r",stdin);
							int n,m;
							INPUT(n);
							INPUT(m);
							input(n,m);
							display(n,m);
 banker(n,m);
							/*if(safetyAlgo(n,m))
							printf("no dead lock");*/
							return 0;
							}
						






/** input function **/

			void input(int n,int m)
			{
			int i,j;

					/*allocation matrix*/
					for(i=0;i<n;i++)
					{
					process[i].pid=i;
					for(j=0;j<m;j++)
					scanf("%d",&process[i].Allocation[j]);
					}

						/*maximum and need calulation*/

						for(i=0;i<n;i++)
						{
						    for(j=0;j<m;j++)
						    {	scanf("%d",&process[i].Max[j]);

							process[i].Need[j]=process[i].Max[j]-process[i].Allocation[j];
						    }
						}
					/*avilable matrix*/

				for(i=0;i<m;i++)
				{
				scanf("%d",&Avialable[i]);
				}

			}




/*display function*/
void display(int n,int m)
{
int i,j;
printf("\nAllocation table\n");
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
p(process[i].Allocation[j]);
NL;
}
printf("\nneed table \n");
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
p(process[i].Need[j]);
NL;
}
printf("\nmaximum table\n");
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
p(process[i].Max[j]);
NL;
}

printf("\navialable\n");
for(i=0;i<m;i++)
p(Avialable[i]);

NL;
}

