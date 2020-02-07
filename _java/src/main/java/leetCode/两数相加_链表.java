package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/31 12:57
 * @description
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 示例：
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 0 -> 8
 * 原因：342 + 465 = 807
 *
 */
public class 两数相加_链表 {

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     * int val;
     * ListNode next;
     * ListNode(int x) { val = x; }
     * }
     */
    public ListNode addTwoNumbers_优化前(ListNode l1, ListNode l2) {
        if (null == l1 && null == l2) {
            throw new IllegalArgumentException("参数错误");
        }
        ListNode head = new ListNode(0);
        ListNode current = head;
        int carry = 0;
        while (true) {
            int add1 = null == l1 ? 0: l1.val;
            int add2 = null == l2 ? 0: l2.val;
            int sum = add1 + add2 + carry;

            int digit;
            if (sum > 9) {
                carry = 1;
                digit = sum - 10;
            } else {
                digit = sum;
                carry = 0;
            }
            ListNode next = new ListNode(digit);
            current.next = next;
            current = next;

            l1 = null == l1 ? null: l1.next;
            l2 = null == l2 ? null: l2.next;
            if (null == l1 && null == l2) {
                if (carry == 1) {
                    next = new ListNode(1);
                    current.next = next;
                }
                break;
            }
        }
        return head.next;
    }


    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (null == l1 && null == l2) {
            throw new IllegalArgumentException("参数错误");
        }
        ListNode head = new ListNode(0);
        ListNode current = head;
        int carry = 0;
        while (true) {
            int add1 = null == l1 ? 0: l1.val;
            int add2 = null == l2 ? 0: l2.val;
            int sum = add1 + add2 + carry;

            carry = sum / 10;
            ListNode next = new ListNode(sum % 10);
            current.next = next;
            current = next;

            l1 = null == l1 ? null: l1.next;
            l2 = null == l2 ? null: l2.next;
            if (null == l1 && null == l2) {
                break;
            }
        }

        if (carry == 1) {
            current.next = new ListNode(1);
        }

        return head.next;
    }

    public ListNode addTwoNumbers_2ms(ListNode l1, ListNode l2) {
        ListNode t1 = l1;
        ListNode t2 = l2;
        ListNode l, s;
        int i, j, sum, carry = 0;
        while (null != t1 && null != t2) {
            t1 = t1.next;
            t2 = t2.next;
        }

        // 以长链表为头
        if (null == t1) {
            l = l2;
            s = l1;
        } else {
            l = l1;
            s = l2;
        }

        while (null != l) {
            i = l.val;
            j = null == s ? 0: s.val;

            sum = i + j + carry;

            if (sum > 9) {
                carry = 1;
                sum = sum -10;
            } else {
                carry = 0;
            }

            l.val = sum;
            if (null == l.next && carry == 1) {
                ListNode node = new ListNode(0);
                l.next = node;
            }

            l = l.next;
            if (null != s) {
                s = s.next;
            }
        }
        return l;
    }

    public static void main(String[] args) {
        两数相加_链表 obj = new 两数相加_链表();

        ListNode a1 = new ListNode(2);
        ListNode a2 = new ListNode(4);
        ListNode a3 = new ListNode(3);
        a1.next = a2;
        a2.next = a3;

        ListNode b1 = new ListNode(5);
        ListNode b2 = new ListNode(6);
        ListNode b3 = new ListNode(4);
        b1.next = b2;
        b2.next = b3;
        ListNode c1 = new ListNode(5);
        ListNode d1 = new ListNode(5);

        ListNode result = obj.addTwoNumbers(a1, b1);
        System.out.println("运行完毕");
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}