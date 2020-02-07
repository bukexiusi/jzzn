package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 11:36
 * @description
 */
public class 最大子串和 {

    public int maxSubArray(int[] nums) {
        if (nums.length == 0) {
           return Integer.MIN_VALUE;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        int result = Integer.MIN_VALUE;
        int M = nums.length;
        int[] opt = new int[M + 1];
        for (int i = 1; i < M + 1; i++) {
            opt[i] =  Math.max(opt[i - 1] + nums[i - 1], nums[i - 1]);
            result = Math.max(result, opt[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        最大子串和 obj = new 最大子串和();
        System.out.println(obj.maxSubArray(new int[]{}));
    }
}
