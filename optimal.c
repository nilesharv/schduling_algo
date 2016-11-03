#include<stdio.h>
#include<stdlib.h>


void display(int frame[],int f)
{
int i;
for(i=0;i<f;i++)
printf("%d ",frame[i]);
printf("\n");

}

int search(int frame_table[],int k,int n)
{
int i=0;
for(i=0;i<n;i++)
if(frame_table[i]==k)
	return i;

return -1;
}

void makeframe(int ref[],int frame[],int i,int n,int f)
{
int t_f=f,k,j;
for(;i<n&&t_f;i++)
{

for(j=0;j<t_f;j++)
{
if(ref[i]==frame[j])
{
for(k=j;k<t_f-1;k++)
frame[k]=frame[k+1];
frame[t_f-1]=ref[i];
t_f--;
}
}

}


}

int optimal(int ref[],int n,int f)
{
int *frame_table=(int*)malloc(sizeof(int)*f);
int t=0,i,j;
int fault=0;
int temp;
for(i=0;i<n;i++)
{
display(frame_table,t);
if(search(frame_table,ref[i],t)==-1)
{
if(t<f)
{
fault++;
frame_table[t]=ref[i];
t++;
}
else
{
fault++;
makeframe(ref,frame_table,i,n,t);
frame_table[0]=ref[i];
}
}

}
return fault;
}


int *input(int n)
{
int *ref;
int i;
ref=(int*)malloc(sizeof(int)*n);
if(ref==NULL)
return NULL;
for(i=0;i<n;i++)
scanf("%d",ref+i);
return ref;
}

int main()
{
int fault;
int n,f,i;
int *ref;
int t;
scanf("%d",&t);
while(t--)
{printf("enter number of reference string and frame number: ");
scanf("%d%d",&n,&f);
ref=input(n);
if(ref==NULL)
{
printf("memory error");
break;
}
fault=optimal(ref,n,f);
printf("number of page fault %d\n",fault);

}
return 0;
}
