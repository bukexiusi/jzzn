package 算法4.栈;

import java.util.Iterator;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/5 18:43
 * @description
 */
public class 栈_链表实现<E> implements Iterable<E> {

    // 大小
    private int SIZE;

    // 链表存储
    private Node node;

    private class Node {
        E val;
        Node node;

        Node(E val, Node node) {
            this.val = val;
            this.node = node;
        }
    }

    public E push(E element) {
        /**
         Node _node = new Node(element);
         if (SIZE > 0) {
         node.next = _node;
         }
         node = _node;
         SIZE ++;
         这段设计，出栈时，无法让指针指回上一个元素，
         */
        node = new Node(element, node);
        SIZE ++;
        return element;
    }

    public E pop() {
        Node _node = node;
        node = node.node;
        SIZE--;
        return _node.val;
    }

    public int size() {
        return SIZE;
    }

    public boolean isEmpty() {
        return SIZE == 0;
    }

    @Override
    public Iterator<E> iterator() {
        return null;
    }
}
