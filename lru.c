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

void priotrize(int frame_table[],int k,int n)
{
int i=0;
for(i=0;i<n-1;i++)
frame_table[i]=frame_table[i+1];
frame_table[n-1]=k;
}

int lru(int ref[],int n,int f)
{
int *frame_table=(int*)malloc(sizeof(int)*f);
int t=0,i,j;
int fault=0;
int temp;
for(i=0;i<n;i++)
{
display(frame_table,t);
if(t<f)
{
fault++;
frame_table[t]=ref[i];
t++;
}
else
{
if(search(frame_table,ref[i],f)==-1)
{
fault++;
for(j=0;j<f-1;j++)
frame_table[j]=frame_table[j+1];
frame_table[f-1]=ref[i];
}
else
{
temp=search(frame_table,ref[i],f);
for(j=temp;j<n-1;j++)
frame_table[j]=frame_table[j+1];
frame_table[f-1]=ref[i];
}

}
}
return fault;
}


int optimal(int ref[],int n,int f)
{
int i=0,temp	;
n--;
while(i<n)
{
temp=ref[i];
ref[i]=ref[n];
ref[n]=temp;
i++;
n--;
}
return lru(ref,n,f);
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
fault=lru(ref,n,f);
printf("number of page fault %d\n",fault);

}
return 0;
}
