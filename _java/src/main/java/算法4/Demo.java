package 算法4;

import 算法4.栈.栈_链表实现;

import java.util.Stack;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/5 18:16
 * @description
 */
public class Demo {

    public static void main(String[] args) {
//        Stack<Integer> stack = new Stack<Integer>();
//        System.out.println("入栈顺序");
//        for (int i = 0; i < 3; i++) {
//            System.out.println(stack.push(i));
//        }
//        System.out.println("循环顺序");
//        for (int i: stack) {
//            System.out.println(i);
//        }
//        System.out.println("出栈顺序");
//        for (int i = 0; i < 3; i++) {
//            System.out.println(stack.pop());
//        }


        栈_链表实现<Integer> stack2 = new 栈_链表实现<Integer>();
        System.out.println("入栈顺序");
        for (int i = 0; i < 3; i++) {
            System.out.println(stack2.push(i));
        }
        System.out.println("size为" + stack2.size());
//        System.out.println("循环顺序");
//        for (int i: stack2) {
//            System.out.println(i);
//        }
        System.out.println("出栈顺序");
        for (int i = 0; i < 3; i++) {
            System.out.println(stack2.pop());
        }
        System.out.println("是否为空" + stack2.isEmpty());
    }
}

