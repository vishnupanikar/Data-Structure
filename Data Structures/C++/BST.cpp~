//BST

#include<iostream>

//---------------------------------------------------------------------------------
class Node{
	public:
		int data;
		Node *leftchild = NULL;
		Node *rightchild = NULL;
};

//---------------------------------------------------------------------------------
Node* insert(Node *root , int data){
	if(root == NULL){
		Node *node = new Node();
		node->data = data;
		return node;
	}
	else{
		if(data > root->data){
			root->rightchild = insert(root->rightchild , data);
			return root;
		}
		else{
			root->leftchild = insert(root->leftchild , data);
			return root;
		}
	}
}

//---------------------------------------------------------------------------------
void inorder(Node *root){
	if(root == NULL){
		return;
	}
	else{
		inorder(root->leftchild);
		std::cout<<root->data<<"-->";
		inorder(root->rightchild);
		return;
	}
}


//---------------------------------------------------------------------------------
void preorder(Node *root){
	if(root == NULL){
		return;
	}
	else{
		std::cout<<root->data<<"-->";
		preorder(root->leftchild);
		preorder(root->rightchild);
		return;
	}
}

//---------------------------------------------------------------------------------
void postorder(Node *root){
	if(root == NULL){
		return;
	}
	else{
		postorder(root->leftchild);
		postorder(root->rightchild);
		std::cout<<root->data<<"-->";
		return;
	}
}

//---------------------------------------------------------------------------------
void find(Node *root , int element){
	if(root == NULL){
		std::cout<<"No Such Element\n";
		return; 
	}
	if(element == root->data){
		std::cout<<"Element Found\n";
		return;
	}
	else{
	
		if(element > root->data){
			find(root->rightchild , element);
			return;
		}
		else{
			find(root->leftchild , element);
			return;
		}
		
	}
}


//---------------------------------------------------------------------------------
int main(){
	
	int total_node;
	int data;
	Node *root = NULL;
	std::cout<<"Enter total node :: ";
	std::cin>>total_node;
	for(int i = 0 ; i<total_node ; i++){
		std::cout<<"Enter Node Value :: ";
		std::cin>>data;
		root = insert(root , data);
	}
	
	std::cout<<"\nInorder :: ";
	inorder(root);
	std::cout<<"\nPreorder :: ";
	preorder(root);
	std::cout<<"\nPostorder :: ";
	postorder(root);
	std::cout<<"\n";
	
	int element;
	std::cout<<"Enter Element to be Searched :: ";
	std::cin>>element;
	find(root,element);
	
}

