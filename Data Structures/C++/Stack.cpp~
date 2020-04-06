#include<iostream>

//--------------------Defining Stack of size 10------------------
#define SIZE 10

//-------------------------ADT for stack------------------
class mystack{
      private:
            int stack[SIZE] = {0};
            int top = -1;
      public:
            bool isEmpty();
            bool isFull();
            int push(int data);
            void display();
            void pop();
            int peek(int index);
            int stack_top();
};

//------------------------isEmpty()---------------------------
bool mystack::isEmpty(){
	if (this->top == -1){
		return true;
	}
	else{
		return false;
	}
}

//-------------------------------isFull()--------------------------
bool mystack::isFull(){
	if (this->top == SIZE-1){
		return true;
	}
	else{
		return false;
	}
}

//----------------------------------push()--------------------------------
int mystack::push(int data){
	
	if((*this).isFull()){
		return -1;
	}
	else{
		this->top += 1;
		this->stack[top] = data;
		return 1;
	}
}

//-------------------------display()--------------------------
void mystack::display(){
	int count = this->top;
	std::cout<<"\n";
	while(count != -1){
		std::cout<<stack[count]<<" ";
		count--;
	}
	std::cout<<"\n";

}

//--------------------------pop()-----------------------------
void mystack::pop(){
	
	if(this->isEmpty()){
		std::cout<<"\nStack underflow";
	}
	else{
		std::cout<<"\nElement popped :: "<<this->stack[top];
		this->stack[top] = 0;
		this->top -= 1;
	}
}

//-------------------------------peek()-------------------------
int mystack::peek(int index){
	
	if(index > this->top){
		return -1;
	}
	else{
		int count = this->top;
		while(index > 1){
			count--;
			index--;
		}
		return this->stack[count];
	}
}

//----------------------------stack_top()----------------------------
int mystack::stack_top(){
	if(this->isEmpty()){
		return -1;
	}
	else{
		return this->stack[this->top];
	}
}

//-----------------------------Main--------------------------
int main(){

      //-----------------declarations-----------------
      mystack s = mystack();
      int data;
      int state;
     	int n;
     	
     	//------------------push----------------------
     	std::cout<<"\nEnter number of stack elements :: ";
     	std::cin>>n;
      for(int i=0 ; i<n ; i++){
		std::cout<<"Enter the element in stack :: ";
		std::cin>>data;
		state = s.push(data);
		if (state == 1){
			std::cout<<"Element pushed into stack\n";
		}
		else{
			std::cout<<"Stack Overflow\n";
		}
	}
	s.display();
	
	//----------------------pop---------------------
	s.pop();
	s.display();
	
	//---------------------peek----------------------
	std::cout<<"\nPeeked Element :: "<<s.peek(5);
	
	//--------------------stack_top-----------------
	std::cout<<"\nTop Element :: "<<s.stack_top();
}
