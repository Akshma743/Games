import java.util.Scanner;

import javax.xml.stream.events.NotationDeclaration;
class Node{
    int data;
    Node next;


    Node(int data){
        this.data=data;
        this.next=null;
    }
}

class linkedlist{
    Node start;

    linkedlist(){
        this.start=null;
    }

    private Node createNode(int data){
        return new Node(data);
    }

    void insertstart(int data){
        Node newNode=createNode(data);
        if(start==null){
            start=newNode;
        }
        else{
            newNode.next=start;
            start=newNode;
        }
    }

    void insertEnd(int data){
        Node newNode=createNode(data);
        if(start==null){
            start= newNode;
            return;
        }
        Node temp=start;
        while(temp.next!=null){
            temp=temp.next;
        }
        temp.next=newNode;
        }

    void insertMiddle(int data,int pos){
        if(pos==1){
            insertstart(data);
            return;
        }
        Node newNode=createNode(data);
        Node temp=start;
        for(int i=1;temp!=null&&i<pos-1;i++){
            temp=temp.next;

        }
        if(temp==null){
            System.out.println("Position out of range");
        }
        newNode.next=temp.next;
        temp.next=newNode;


    }
    
    
    void deleteStart(){
        if(start==null){
            System.out.println("List is Empty");
            return;
        }
        start=start.next;
    }

    void deleteEnd(){
        if(start==null){
            System.out.println("List is Empty");
            return;
        }
        if(start.next==null){
            start=null;
            return;
        }
        Node temp=start;
        while(temp.next.next!=null){
            temp=temp.next;
        }
        temp.next=null;
    }

    void deleteMiddle(int position){
        if(start==null){
            System.out.println("List is Empty");
            return;
        }
        if(position==1){
            deleteStart();
            return;
        }
        Node temp=start;


    }


     void display(){
        if(start==null){
            System.out.println("List Empty");
            return;
        }
        Node temp=start;
        while(temp!=null){
            System.out.println(temp.data+"->");

        }
        System.out.println("Null");
     }   
    
}


public class lin{
    public static void main(String[] args) {
        linkedlist list=new linkedlist();
        Scanner sc=new Scanner(System.in);
        int choice=sc.nextInt();
        switch(choice){
            case 1:
                System.out.println("Enter data");
                list.insertstart(sc.nextInt());
                break;

            case 2:
               System.out.println("Enter data");
               list.insertEnd(sc.nextInt());
               break;
            
            case 3:
                System.out.println("Enter data and Position:");
                list.insertMiddle(sc.nextInt(),sc.nextInt());
                break;   

            case 7:
                list.display();
           } 
            }
        
    } 
