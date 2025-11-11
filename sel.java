class sel{
    public static void main(String[] args) {
        int a[]={12,4,6,13,8};
        int p,s,inn,temp,min;
        for(p=0;p<4;p++){
            min=a[p];
            inn=p;
            for(s=p+1;s<5;s++){
                if(min>a[s]){
                    min=a[s];
                    inn=s;

                }
            }
            temp=a[p];
            a[p]=a[inn];
            a[inn]=temp;
        }
        for(int i=0;i<5;i++){
            System.out.println(a[i]);

        }

    }
}