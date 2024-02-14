#include <stdio.h>
#include <stdlib.h>

// Define the TreeNode structure
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

// Function to create a new TreeNode
TreeNode* createTreeNode(int val) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->val = val;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to perform inorder traversal and store the result in an array
void inorderTraversal(TreeNode* node, int* arr, int* index) {
    if (node == NULL) {
        return;
    }
    inorderTraversal(node->left, arr, index);
    arr[(*index)++] = node->val;
    inorderTraversal(node->right, arr, index);
}

// Function to find the kth smallest element in the BST
int kthSmallest(TreeNode* root, int k) {
    int* arr = (int*)malloc(100 * sizeof(int)); // Assuming the tree has less than 100 elements
    int index = 0;
    inorderTraversal(root, arr, &index);
    
    int result = arr[k - 1]; // k-1 because array indices start at 0
    free(arr);
    return result;
}

int main() {
    // Create the binary tree
    TreeNode* root = createTreeNode(20);
    root->left = createTreeNode(10);
    root->left->left = createTreeNode(9);
    root->left->right = createTreeNode(11);
    root->right = createTreeNode(30);
    root->right->left = createTreeNode(22);
    root->right->right = createTreeNode(40);

    // Find the 3rd smallest element
    printf("The 3rd smallest element is: %d\n", kthSmallest(root, 3));

    // Ideally, here you would also have code to free the memory of the tree nodes
    return 0;
}
