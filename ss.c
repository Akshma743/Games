/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int sum(int ,int );
    
    int c=sum(3,5);
    printf("%d",c);
}

    int sum(int a,int b)
     {
    int c=a+b;
    return c;
}    
/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
   int Greater_no(int,int);{
       int r;
        r=Greater_no(34,99);
        printf("%d",r);
   }
    
}
   int Greater_no(int a,int b){
       
       if(a>b){
           return a;
       }
       else{
           return b;
       }
   }
/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include<stdarg.h>
int sum(int count,...)
{
    va_list args;
    va_start(args,count);//Ini...
    
    int total =0;
    for(int i=0;i<count;i++){
        total+=va_arg(args,int);//get next int
    }
    va_end(args);//cleanup
    return total;
   }
  int main(){
      printf("Sum =%d\n",sum(14,56,34,1,34,56,7,21,6,6,67,89,345,678,12));
      printf("Sum =%d\n",sum(2,4,56,78,1));
      return 0;
  }
