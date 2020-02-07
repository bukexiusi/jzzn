package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/1 13:48
 * @description There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 * You may assume nums1 and nums2 cannot be both empty.
 * Example 1:
 * nums1 = [1, 3]
 * nums2 = [2]
 * The median is 2.0
 * Example 2:
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * The median is (2 + 3)/2 = 2.5
 */
public class 寻找两个有序数组中的中位数 {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int maxLen = nums1.length + nums2.length;
        boolean even = maxLen % 2 == 0;
        int midIdx = (int) Math.ceil((double) maxLen / 2);
        int offset = (int) Math.ceil((double) midIdx / 2);
        int io = Math.min(offset, nums1.length);
        int jo = Math.min(offset, nums2.length);
        int i = 0, j = 0;
        while (midIdx > 1) {
            int nums1Idx = i + io - 1;
            int nums2Idx = j + jo - 1;
            if (nums1[nums1Idx] > nums2[nums2Idx]) {
                j = nums2Idx + 1;
                offset = jo;
                if (j == nums2.length) {
                    i = midIdx - offset -1;
                    j--;
                    break;
                }
            } else {
                i = nums1Idx + 1;
                offset = io;
                if (i == nums1.length) {
                    j = midIdx - offset - 1;
                    i--;
                    break;
                }

            }

            midIdx = (int) Math.ceil((double) (midIdx - offset) / 2);
        }

        double result;
        if (even) {
            double one = Math.max(nums1[i], nums2[j]);
            double another = one == nums1[i] ?
                    Math.max(nums1[i + 1], nums2[j]) :
                    Math.max(nums1[i], nums2[j + 1]);
            result = (one + another) / 2;
        } else {
            result = Math.max(nums1[i], nums2[j]);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] array1 = {1, 4};
        int[] array2 = {2, 3};
        寻找两个有序数组中的中位数 obj = new 寻找两个有序数组中的中位数();
        System.out.println(obj.findMedianSortedArrays(array1, array2));
    }

}
//   1, 12, 23, 34
//   2, 13, 24, 35
//
//
//
