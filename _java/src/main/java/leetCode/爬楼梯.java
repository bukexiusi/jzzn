package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 14:41
 * @description
 */
public class 爬楼梯 {

    public int climbStairs(int n) {
        int first = 1, second = 1;
        for (int i = 2; i < n + 1; i++) {
            int temp = second;
            second = first + second;
            first = temp;
        }
        return second;
    }

    public static void main(String[] args) {
        爬楼梯 obj = new 爬楼梯();
        System.out.println(obj.climbStairs(4));
    }
}
