package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/3 21:46
 * @description
 */
public class 最长有效括号 {

    public int longestValidParentheses(String s) throws Exception{
        if (null == s || "".equals(s)) {
            return 0;
        }
        int result = 0;
        int[] opt = new int[s.length()];
        opt[0] = 0;
        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                opt[i] = 0;
            } else if (c == ')') {
                char prev = s.charAt(i - 1);
                if (prev == '(') {
                    opt[i] = i - 2 < 0 ? 2 : opt[i - 2] + 2;
                } else {
                    // prev = ')'
                    int vIdx = i - opt[i - 1] - 1;
                    if (vIdx < 0) {
                        opt[i] = 0;
                    } else {
                        char before = s.charAt(vIdx);
                        int addIdx = vIdx - 1;
                        if (before == '(') {
                            if (addIdx < 0) {
                                opt[i] = opt[i - 1] + 2;
                            } else {
                                opt[i] = opt[addIdx] + opt[i - 1] + 2;
                            }

                        } else {
                            opt[i] = 0;
                        }
                    }

                }
                result = Math.max(result, opt[i]);
            } else {
                throw new Exception("包含非法字符");
            }
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        最长有效括号 obj = new 最长有效括号();

        System.out.println(obj.longestValidParentheses("()())"));
    }


}
