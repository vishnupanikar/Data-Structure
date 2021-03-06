#include<iostream>

//----------------------Max Queue size----------------------------
#define n 10

//------------------------Queue Class--------------------------
class Queue{
	private:
		int front = -1;
		int rear = -1;
		int queue[n];
	public:

		bool isEmpty();
		bool isFull();
		int enqueue(int data);
		void display();
		int dequeue();
};

//--------------------------------------------------
bool Queue::isEmpty(){
	
	if(this->front == this->rear){
		return true;
	}
	else{ return false ;}
}

//--------------------------------------------------
bool Queue::isFull(){
	
	if(this->rear == n - 1){
		return true;
	}
	else{ return false ;}
}

//-----------------------enqueue---------------------------
int Queue::enqueue(int data){
	
	if(this->isFull()){
		return -1;
	}
	else{
		if(this->front == -1){
			this->front += 1;
			this->rear += 1;
			
		}
		else{
			this->rear += 1;
		}
		this->queue[rear] = data;
		return 1;
	}
}

//--------------------------------------------------
void Queue::display(){
	
	int index = this->front;
	while(index <= this->rear){
		std::cout<<this->queue[index]<<" ";
		index++;
	}
	std::cout<<"\n";
}

//-----------------------dequeue---------------------------
//removing the first element and shifting other elements in queue and decrementing rear
int Queue::dequeue(){
	
	if(this->isEmpty()){
		return -1;
	}
	else{
		int value = this->queue[front];
		int index = this->front;
		while(index < this->rear){
			this->queue[index] = this->queue[index+1];
			index++;
		}
		this->queue[rear] = 0;
		if(this->front == this->rear){
			this->front -= 1;
			this->rear -= 1;			
		}
		else{
			this->rear -= 1;
		}
		
		return value;
		
	}
}

//----------------------MAIN----------------------------
int main(){
	
	int size;
	std::cout<<"Enter size of queue :: ";
	std::cin>>size;
	Queue myqueue = Queue();
	
	int data;
	int status;
	
	//--------------------------------------------------
	for(int i=0 ; i<size ; i++){
		std::cout<<"\nEnter the data :: ";
		std::cin>>data;
		status = myqueue.enqueue(data);
		if(status == 1){
			std::cout<<"Element entered successfully\n";
		}
		else{
			std::cout<<"Queue is Full\n";
		}
		
	}
	myqueue.display();
	
	//--------------------------------------------------
	status = myqueue.dequeue();
		if(status != -1){
			std::cout<<"\nDequeued Element :: "<<status<<std::endl;
		}
		else{
			std::cout<<"\nQueue is Empty\n";
		}	
	myqueue.display();
		
	
	return 0;
}
