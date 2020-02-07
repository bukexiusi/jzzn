package leetCode;

import java.util.*;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/31 21:39
 * @description
 */
public class 无重复字符的最长子串 {

    public int lengthOfLongestSubstring_(String s) {
        char[] chars = s.toCharArray();
        Map<Character, List<Integer>> map = new HashMap<Character, List<Integer>>();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            List<Integer> array = map.get(c);
            if (null == array) {
                array = new ArrayList<Integer>();
                map.put(c, array);
            }
            array.add(i);
        }

        // 最大长度
        int maxLen = chars.length;
        // 取出区间
        List<List<Integer>> region = new ArrayList<List<Integer>>();
        for (List<Integer> list : map.values()) {
            if (list.size() > 1) region.add(list);
        }
        if (region.size() == 0) return maxLen;
        // 用于区间外数组
        int[] out = new int[maxLen];
        for (int i = 0; i < maxLen; i++) {
            out[i] = i;
        }
        int max = 0;
        // 区间内最大无重复字符串
        for (List<Integer> compareList1 : region) {
            for (int i = 0; i < compareList1.size() - 1; i++) {
                int diff = compareList1.get(i + 1) - compareList1.get(i);
                max = Math.max(diff, max);
            }
            int t_min = compareList1.get(0);
            int t_max = compareList1.get(compareList1.size() - 1);
            for (int i = t_min; i < t_max + 1; i++) {
                out[i] = 0;
            }

        }

        // 区间外最大无重复字符串
        if (out[out.length - 1] > 0) {
            int[] out_ = Arrays.copyOf(out, out.length + 1);
            out = out_;
        }
        List<Integer> outMaxList = new ArrayList<Integer>();
        int subtrahendIndex = 0;
        boolean b = false;
        for (int i = 0; i < out.length; i++) {
            int j = out[i];
            if (b) {
                if (j == 0) outMaxList.add(i - subtrahendIndex);
                b = false;
            }
            if (j > 0) {
                b = true;
            } else {
                subtrahendIndex = i;
            }

        }

        for (Integer i : outMaxList) {
            max = Math.max(i, max);
        }

        return max;
    }

    public int lengthOfLongestSubstring(String s) {
        char[] chars = s.toCharArray();
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        int max = 0;
        int i = 0;
        int j = 0;
        for (; j < chars.length; j++) {
            Character c = chars[j];
            Integer index = map.get(c);
            if (null != index) {
                max = Math.max(j - i, max);
                int c_index = map.get(c) + 1;
                i = Math.max(i, c_index);
            }
            map.put(c, j);
        }
        max = Math.max(j - i, max);
        return max;
    }

    public static void main(String[] args) {
        无重复字符的最长子串 obj = new 无重复字符的最长子串();
        String str1 = "abcabcbb";
        String str2 = "bbbbbb";
        String str3 = "pwwkew";
        String str4 = "abcd";
        String str5 = "abcdzefz";
        String str6 = "aab";
        String str7 = "cdd";
        String str8 = "abcb";
        String str9 = "abba";
        System.out.println(obj.lengthOfLongestSubstring(str1));
        System.out.println(obj.lengthOfLongestSubstring(str2));
        System.out.println(obj.lengthOfLongestSubstring(str3));
        System.out.println(obj.lengthOfLongestSubstring(str4));
        System.out.println(obj.lengthOfLongestSubstring(str5));
        System.out.println(obj.lengthOfLongestSubstring(str6));
        System.out.println(obj.lengthOfLongestSubstring(str7));
        System.out.println(obj.lengthOfLongestSubstring(str8));
        System.out.println(obj.lengthOfLongestSubstring(str9));

    }

}

/**
 * 第一遍的思路,将出现字符分类如"abca"分为
 * a: [0, 3]
 * b: [1]
 * c: [2]
 * 区间内最大值和区间外最大值相比较，做了两个小时没做出结果，暂时放弃
 * <p>
 * 第二种思路采用,队列进出
 */
