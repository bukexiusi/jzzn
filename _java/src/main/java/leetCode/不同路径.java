package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 12:01
 * @description
 */
public class 不同路径 {

    public int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) {
            return 0;
        }
        int[][] opt = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    opt[i][j] = 1;
                    continue;
                }
                opt[i][j] = opt[i - 1][j] + opt[i][j - 1];
            }
        }
        return opt[m - 1][n - 1];
    }

    public static void main(String[] args) {
        不同路径 obj = new 不同路径();
        System.out.println(obj.uniquePaths(3, 7));
    }

}
