package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 21:23
 * @description
 */
public class 整数反转 {

    public int reverse(int x) {
        int temp = Math.abs(x);
        if (temp < 0) {
            return 0;
        }
        String str = String.valueOf(temp);
        String resultStr = new StringBuilder(str).reverse().toString();
        try {
            temp = Integer.parseInt(resultStr);
        } catch (Exception e) {
            temp = 0;
        }
        temp = x < 0 ? -1 * temp : temp;
        return temp;
    }

    public static void main(String[] args) {
        整数反转 obj = new 整数反转();
        obj.reverse(Integer.MAX_VALUE);
    }
}
