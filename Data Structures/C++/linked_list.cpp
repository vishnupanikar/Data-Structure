#include<iostream>

//The Node class is a skeleton of Node which we will be using in the linked list
//data is used to store the actual data you can have many other variables to store other kinds of data also
//next will be pointing to the next node
class Node{
      public:
            int data;
            Node *next;
};


//-----------------------------------------------------------------------------------------------------------------------
//1. Function for creating

//Now this syntax seems to be terrifying but its easy and understandable
//Starting with the parameters 
      //as we are passing a pointer of type Node to insert() we need to declare one to accept it.
      //head here will contain the address of the head node passed from the main()
      //data will contain the data to be inserted
//return type
      //after the insertion of data the head pointer must be returned 
      //if not then the entry point for the list will be lost and will lead to memory leak
      //as we return the head we write Node* as return type
      //Node represents that the type is of class Node and * represents that the value is a pointer
Node* insert(Node *head , int data){

      //A new node is to be created in memory for storage of data
      Node *node = new Node();

      //assigning values
      //can also use :: (*node).data = data; (*node).next = NULL;
      //but tideous...
      node->data = data;
      node->next = NULL;

      if(head == NULL){
                 head = node;          //initially check if the head is NULL if yes then assign the newly created pointer
                                       //as head
      }
      else{
            Node *temp = head;         //Notice a new temp pointer , but why?
                                       // if we use the head directly to traverse the list we will be inserting
                                          //newly entered data but we will loose the starting address of the list
                                          //to prevent that we are declaring temp
  
            while(temp->next != NULL){
                  temp = temp->next;      //traversing till the end of the list and then adding the element
            }

            temp->next = node;

      }

      return head;
}

//---------------------------------------------------------------------------------------------------------

//2. Function for inserting at head
Node* insert_head(Node* head , int data){

      Node *node = new Node();
      node->data = data;
      node->next = head;
      head = node;
      return head;
}
//------------------------------------------------------------------------------------------------------------------------
//Function to insert at specified position
void insert_pos(Node *head , int pos , int data){
      int i = 0;
      Node *temp = head;
      while(i < (pos-2)){
            temp = temp->next;
            i++;
      }

      Node *node = new Node();
      node->data = data;
      node->next = temp->next;
      temp->next = node;
}
//------------------------------------------------------------------------------------------------------------------------
//Function to delete from head
Node* delete_head(Node *head){
      Node *temp = head;
      head = temp->next;
      free(temp);
      return head;
}
//------------------------------------------------------------------------------------------------------------------------
//Function to delete from tail
void delete_tail(Node *head){
      Node *temp;
      while(head->next->next != NULL){
            head = head->next;
      }
      temp = head->next;
      head->next = NULL;
      free(temp);
}
//------------------------------------------------------------------------------------------------------------------------
//Function to delete from middle
void delete_pos(Node *head , int pos){
      Node *temp;
      int i = 0;
      while(i < (pos-2)){
            head = head->next;
            i++;
      }
      temp = head->next;
      head->next = head->next->next;
      free(temp);
}
//------------------------------------------------------------------------------------------------------------------------
//Function for displaying
void display(Node *head)
{
      std::cout<<"\n";
      while(head != NULL){
            std::cout<<head->data<<"-->";
            head = head->next;
      }
      std::cout<<"\n";

}


//-----------------------------------------------------------------------------------------------------------------------
int main(){

      //head is a pointer to the class Node which is assigned as null initially
      Node *head = NULL;

//---------------1. Create-------------------- 
      int node_count;
      int data;
      std::cout<<"\nEnter The Number of nodes :: ";
      std::cin>>node_count;
      for(int i=0 ; i<node_count ; i++){
            std::cout<<"\nEnter the number :: ";
            std::cin>>data;

            head = insert(head , data); //actually what we are passing here is the address of the head which is just an
                                          //identifier used to indentify the newly created object

      }  

//---------------2. Displaying-------------------
      std::cout<<"\nLinked List";    
      display(head);

//--------------3. Inserting at head----------------
      int head_data;
      std::cout<<"\nEnter value of new head :: ";
      std::cin>>head_data;
      head = insert_head(head,head_data);
      std::cout<<"\nLL with new head";    
      display(head);

//--------------4. Inserting at middle--------------
      int middle_data;
      int pos;
      std::cout<<"\nEnter the position at which data is to be entered :: ";
      std::cin>>pos;
      std::cout<<"\nEnter the data :: ";
      std::cin>>middle_data;
      insert_pos(head,pos,middle_data);// no return value as the head is not changed
      std::cout<<"\nUpdated Linked List";    
      display(head);

//-------------5. Delete from head-------------------
      head = delete_head(head);
      std::cout<<"\nUpdated Linked List";    
      display(head);

//--------------6. Delete from last-------------------
      delete_tail(head);// no return value as the head is not changed
      display(head);

//----------7.Delete from random position------------------
      int pos;
      std::cout<<"\nEnter the position at which data is to be removed :: ";
      std::cin>>pos;
      delete_pos(head , pos);// no return value as the head is not changed
      display(head);


      return 0;
}