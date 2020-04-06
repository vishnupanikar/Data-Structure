#include<iostream>

#define SIZE 10

//----------------------------------------------------------
class Hash{
	private : 
		int hashset[SIZE];
	public :
		Hash(){
			for(int i=0 ; i<SIZE ; i++){
				this->hashset[i] = -1;
			}
		}
		void map(int data);
		void display();
		int find_location(int index);
		void search(int data);
};

//----------------------------------------------------------
//both recursive and iterative approach
void Hash::map(int data){
	int index = data % 10;
	index = find_location(index);
	this->hashset[index] = data;
	//Iterative
	/*while(1){
		if(this->hashset[index] == -1){
			this->hashset[index] = data;
			break;
		}
		else{
			index++;
			if(index >= SIZE){
				index = 0;
			}
		    }	
	}
	*/
	
}

//----------------------------------------------------------

int Hash::find_location(int index){
	if(this->hashset[index] == -1){
		return index;
	}
	else{
		if(index < SIZE-1){
			return find_location(index + 1);
		}
		else{
			return find_location(0);
		}	
	}
}
//----------------------------------------------------------

void Hash::search(int data){
	int flag = 0;
	int index = data % 10;
	while(this->hashset[index] != -1){
		if(this->hashset[index] == data){
			flag = 1;
			break;
		}
		else{
			if(index < SIZE-1){
				index ++;
			}
			else{
				index = 0;
			}
		}
	}
	
	if(flag == 1){
		std::cout<<"\nElement Found..!\n";
	}
	else{
		std::cout<<"\nElement Not In Hash Table\n";
	}
}

//----------------------------------------------------------
void Hash::display(){
	for(int i=0 ; i<SIZE ; i++){
		std::cout<<i<<" :: "<<this->hashset[i]<<"\n";
	}
}

//----------------------------------------------------------
int main(){
	
	int n;
	int data;
	Hash myhash = Hash();
	std::cout<<"Enter number of elements :: ";
	std::cin>>n;
	
	//----------------------------------------------------------
	for(int i = 0 ; i<n ; i++){
		std::cout<<"Enter Data :: ";
		std::cin>>data;
		myhash.map(data);
	}
	
	myhash.display();
	
	//----------------------------------------------------------
	std::cout<<"Enter Data to be Found :: ";
	std::cin>>data;
	myhash.search(data);
	return 0;
}
