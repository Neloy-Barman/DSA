class Node{
    constructor(value){
        this.left = null;
        this.value = value;
        this.right = null;
    }
}

class BinarySearchTree{
    constructor(){
        this.root = null;
    }

    insert(value){
        const newNode = new Node(value);
        if(!this.root){
            this.root = newNode;
            return this;
        }
        else{
            let currentNode = this.root;
            while(true){
                if(value <= currentNode.value){
                    if(!currentNode.left){
                        currentNode.left = newNode;
                        return this;
                    }
                    currentNode = currentNode.left;
                }
                else{
                    if(!currentNode.right){
                        currentNode.right = newNode;
                        return this;
                    }
                    currentNode = currentNode.right;
                }
            }
        }
    }

    lookup(value){
        if(!this.root){
            return false;
        }
        let currentNode = this.root;
        if(value == currentNode.value){
            return "Value found";
            // return currentNode;
        }
        while(true){
            if(value < currentNode.value){
                currentNode = currentNode.left;
            }
            else{
                currentNode = currentNode.right;
            }
            if(currentNode!= null && value == currentNode.value){
                // return currentNode;
                return "Value found";
            }
            if(!currentNode){
                // return null;
                // return "Not found";
                return false;
            }
        }

    }

    remove(value){

    }
}

function traverse(node){
    const tree = {value: node.value};
    tree.left = node.left === null ? null:
    traverse(node.left);
    tree.right = node.right === null ? null:
    traverse(node.right);
    return tree;
};



const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);

// console.log(JSON.stringify(traverse(tree.root)));


// let val = tree.lookup(9);
// let val = tree.lookup(6);
// let val = tree.lookup(200);
// let val = tree.lookup(200);
tree.lookup(500);



// console.log("Lookup: "+JSON.stringify(val));







