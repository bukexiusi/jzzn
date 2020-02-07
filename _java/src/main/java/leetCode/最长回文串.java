package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/3 20:46
 * @description
 */
public class 最长回文串 {


    public String longestPalindrome(String s) {
        if(s == null || s.length()==0){
            return "";
        }

        int sLength = s.length();
        if(sLength == 1){
            return s;
        }
        char[] chars = s.toCharArray();

        int[] result = new int[2];
        for(int i = 0; i < sLength ;i++){
            i = explore(chars,i,result);
        }
        return s.substring(result[0] + 1, result[1]);
    }

    private int explore(char[] chars, int i ,int [] result){
        int l =i;
        int r = i;
        int length = chars.length;
        while ((r+1) < length && chars[r+1] ==  chars[r]){
            r++;
        }
        int re =r;
        while(l>=0 && r < length && chars[l] ==  chars[r]){
            l--;
            r++;
        }
        if((r-l) > (result[1]- result[0])){
            result[0]= l;
            result[1]= r;
        }
        return re;
    }

    public static void main(String[] args) {
        最长回文串 obj = new 最长回文串();
        obj.longestPalindrome("aabbaa");
    }
}
