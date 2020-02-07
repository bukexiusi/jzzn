package 动态规划;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/1 22:51
 * @description
 */
public class Fibonacci {

    /**
     * 有一楼梯共M级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第M级，共有多少种走法
     */
    public static void demo1(int M) {
        int[] opt = new int[M];
        opt[0] = 1;
        opt[1] = 1;
        for (int i = 2; i < M; i++) {
            opt[i] = opt[i - 1] + opt[i - 2];
        }
        System.out.println("走上台阶共有:" + opt[M - 1]);
    }

    /**
     * 数塔问题
     * 给定一个正整数构成的三角形，如下所示：
     * 7
     * 3 8
     * 8 1 0
     * 2 7 4 4
     * 4 5 2 6 5
     * 在上面的数字三角形中寻找一条从顶部到底边的路径，
     * 使得路径上所经过的数字之和最大。
     * 路径上的每一步都只能往左下或者右下走。
     * 只需要求出这个最大和即可，不必给出路径。
     * 三角形的行数大于1小于等于100，整数为0~99
     */
    public static void demo2() throws FileNotFoundException {
        System.setIn(new FileInputStream("D:\\git\\jzzn\\_java\\src\\main\\java\\动态规划\\pyramid of number.txt"));
        Scanner in = new Scanner(System.in);
        int max = 0;
        int n = in.nextInt();
        int[][] opt = new int[n][n];
        opt[0][0] = in.nextInt();
        int i, j;
        for (i = 1; i < n; i++) {
            for (j = 0; j < i + 1; j++) {
                int e = in.nextInt();
                if (j == 0) {
                    opt[i][j] = opt[i - 1][j] + e;
                } else {
                    opt[i][j] = Math.max(
                            opt[i - 1][j] + e,
                            opt[i][j - 1] + e);
                }
            }

            if (i == n - 1) {
                max = Math.max(max, opt[i][j - 1]);
            }
        }

        System.out.println("数塔最大数为:" + max);
    }

    /**
     * 题目描述：
     * 一个N*N矩阵中有不同的正整数，经过这个格子，就能获得相应价值的奖励，从左上走到右下，只能向下向右走，求能够获得的最大价值。
     * 例如：3 * 3的方格。
     * <p>
     * 1 3 3
     * 2 1 3
     * 2 2 1
     */
    public static void demo3() throws FileNotFoundException {
        System.setIn(new FileInputStream("D:\\git\\jzzn\\_java\\src\\main\\java\\动态规划\\matrix of number.txt"));
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] opt = new int[n][n];

        int i, j;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                int e = in.nextInt();
                if (i > 0 && j > 0) {
                    opt[i][j] = Math.max(
                            opt[i][j - 1] + e,
                            opt[i - 1][j] + e);
                } else {
                    if (i == 0 && j == 0) {
                        opt[i][j] = e;
                    } else if (i == 0) {
                        opt[i][j] = opt[i][j - 1] + e;
                    } else {
                        opt[i][j] = opt[i - 1][j] + e;
                    }
                }
            }
        }

        int max = opt[n - 1][n - 1];
        System.out.println("矩阵取数的最大值为:" + max);

    }

    /**
     * 给定数组，求最大子段和。
     * 当（a[1],a[2],a[3],a[4],a[5],a[6]）=(-20,11,-4,13,-5,-2)时，最大子段和为20。
     */
    public static void demo4(int[] array) {
        int max = 0;
        int len = array.length;
        int[] opt = new int[len];
        opt[0] = Math.max(0, array[0]);
        for (int i = 1; i < len; i++) {
            int temp = Math.max(opt[i - 1] + array[i], array[i]);
            temp = Math.max(0, temp);
            opt[i] = temp;
            max = Math.max(max, temp);
        }
        System.out.println("最大子段和为:" + max);

    }

    /**
     * 最长回文串(假设只有一串)
     */
    public static void demo5_错(String s) {
        // 构建正序和逆序数组
        String[] s1 = s.split("");
        String[] s2 = s1.clone();               // 深拷贝
        Collections.reverse(Arrays.asList(s2)); // s2指向数组对象, list对象也指向同一数组对象

        String result = "";
        int n = s1.length;
        String[][] opt = new String[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                boolean flag = s1[i].equals(s2[j]);
                String e = flag ? s1[i] : "";
                if (i == 0 || j == 0) {
                    opt[i][j] = flag ? e : "";
                } else {
                    opt[i][j] = flag ? opt[i - 1][j - 1] + e : "";
                }

                result = result.length() > opt[i][j].length() ? result : opt[i][j];
            }
        }
        // 上述动态规划所求的是最大公共串
        // 校验结果是否为回文串
        boolean b = true;
        int i = 0, j = result.length() - 1;
        char[] chars = result.toCharArray();
        for (; i < j; i++, j--) {
            if (chars[i] != chars[j]) {
                b = false;
                break;
            }
        }

        System.out.println("最长回文串为：" + (b ? result : s1[0]));

    }

    public static void demo5_时间过长(String s) {
        // 构建正序和逆序数组
        String[] s1 = s.split("");
        String[] s2 = s1.clone();               // 深拷贝
        Collections.reverse(Arrays.asList(s2)); // s2指向数组对象, list对象也指向同一数组对象

        List<String> match = new LinkedList<String>();
        int n = s1.length;
        String[][] opt = new String[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                boolean flag = s1[i].equals(s2[j]);
                String e = flag ? s1[i] : "";
                if (i == 0 || j == 0) {
                    opt[i][j] = flag ? e : "";
                } else {
                    opt[i][j] = flag ? opt[i - 1][j - 1] + e : "";
                }

                if (opt[i][j].length() > 1) {
                    match.add(opt[i][j]);
                }
            }
        }
        // 上述动态规划所求的是最大公共串
        // 校验结果是否为回文串
        String result = s1[0];
        Collections.reverse(match);
        for (String temp : match) {
            boolean b = true;
            int i = 0;
            int j = temp.length() - 1;
            char[] chars = temp.toCharArray();
            for (; i < j; i++, j--) {
                if (chars[i] != chars[j]) {
                    b = false;
                    break;
                }
            }

            if (b) {
                result = result.length() > temp.length() ? result : temp;
            }
        }


        System.out.println("最长回文串为：" + result);

    }

    public static void demo5(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            int len1 = palindromic(s, i, i);
            int len2 = palindromic(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len < result.length() + 1) {
                continue;
            }
            int start = i - ((len - 1) / 2);
            int end = i + len / 2;
            result = s.substring(start, end + 1);

        }
        System.out.println("最长回文串为:" + result);
    }

    public static int palindromic(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    public static String longestPalindrome(String s) {
        if (s.equals(""))
            return "";
        String origin = s;
        String reverse = new StringBuffer(s).reverse().toString(); //字符串倒置
        int length = s.length();
        int[][] arr = new int[length][length];
        int maxLen = 0;
        int maxEnd = 0;
        for (int i = 0; i < length; i++)
            for (int j = 0; j < length; j++) {
                if (origin.charAt(i) == reverse.charAt(j)) {
                    if (i == 0 || j == 0) {
                        arr[i][j] = 1;
                    } else {
                        arr[i][j] = arr[i - 1][j - 1] + 1;
                    }
                }
                if (arr[i][j] > maxLen) {
                    maxLen = arr[i][j];
                    maxEnd = i; //以 i 位置结尾的字符
                }

            }

        return s.substring(maxEnd - maxLen + 1, maxEnd + 1);
    }


    public static void main(String[] args) throws Throwable {
        int m = 100;
        long[] fibonacciArray = new long[m];
        for (int i = 0; i < m; i++) {
            if (i == 0 || i == 1) {
                fibonacciArray[i] = 1;
            } else {
                fibonacciArray[i] = fibonacciArray[i - 1] + fibonacciArray[i - 2];
            }
        }
        System.out.println("fibonacci数列动态递归算法结果:" + fibonacciArray[99]);
//        demo1(40);
//        demo2();
//        demo3();
//        demo4(new int[]{-20, 11, -4, 13, -5, -2});
//        demo5_错("aacdefcaa"); // 正确答案应该是aa
//        demo5_时间过长("aacdefcaa");
        demo5("");
    }

}
