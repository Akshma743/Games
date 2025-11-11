import java.util.Scanner;
class buble{
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int temp,i,j;
        int size=4;
        int arr[] = new int[size];
        System.out.println("Enter array values:");
        
        for(i=0;i<size;i++){
            arr[i]=sc.nextInt();
            
        } 
        System.out.println(" Bubble sorting begin");
        for(i=0;i<size;i++){
            for(j=i+1;j<size;j++){
                if(arr[i]>arr[j]){
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
        System.out.println(" Sorted Array is :");
        for(int num:arr){
        System.out.println(num);
        }
    }
}