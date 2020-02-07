package leetCode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/31 11:31
 * @description
 *
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 * 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
 * 示例:
 * 给定 nums = [2, 7, 11, 15], target = 9
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 *
 */
public class 两数相加 {

    /**数组元素不可重复的解法*/
    public int[] twoSum_2(int[] nums, int target) {
        int[] result = new int[2];
        for (int i=0; i < nums.length; i++) {
            int match = target - nums[i];
            int index = Arrays.binarySearch(nums, match);
            if (index > -1) {
                return new int[]{i, index};
            }
        }

        return result;
    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0; i < nums.length; i++) {
            int match = target - nums[i];

            if (map.containsKey(match)) {
                return new int[]{i, map.get(match)};
            }
            map.put(nums[i], i);
        }

        return null;
    }

    public static void main(String[] args) {
        两数相加 obj = new 两数相加();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        for (int i: obj.twoSum(nums, target)) {
            System.out.println(i);
        }

    }

}
/**
 * 第一遍采用嵌套循环的方式
 * 第二遍想直接采用java判断数组元素所在数组索引的方式，但是遇到一个问题，Arrays.binarySearch()只能用于有序数组，具有一定的局限性，而且不允许有重复元素出现
 *     [3, 3] -> 6 此种方式运行错误
 * 第三遍采用Map的方式
 * */