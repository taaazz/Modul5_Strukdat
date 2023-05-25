package Latihan;

public class Main {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();

        tree.NewNode(20);
        tree.NewNode(2);
        tree.NewNode(25);
        tree.NewNode(37);
        tree.NewNode(16);

        System.out.println("\npre Order : ");
        tree.preOrder(tree.root);
        System.out.println("\nIn Order : ");
        tree.inOrder(tree.root);
        System.out.println("\nPOst Order : ");
        tree.postOrder(tree.root);
    }
}
