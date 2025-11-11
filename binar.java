import java.util.Scanner;
class binar{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in); 
        int temp,i,j,key=6;
        int l,h,p=0;
        int n=5;
        int[] arrr=new int[n];
        
        System.out.println("Enter array values:");
        for(i=0;i<n;i++){
            arrr[i]=sc.nextInt();
        }

        System.out.println("Binary Search begin");
        l=0;
        h=n-1;
        while(l<=h){
           int mid=((l+h)/2);
           if(arrr[mid]==key){
            System.out.println("Element fount at inder"+mid);
            p++;
            break;
           }
           else if(arrr[mid]<key){
            l=mid+1;
           }
           else if(arrr[mid]>key){
            h=mid-1;
           }
           
        }
        if(p==0){
            System.out.println("Elemint not found");
            
        }

    }
}