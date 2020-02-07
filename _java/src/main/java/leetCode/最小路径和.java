package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 14:27
 * @description
 */
public class 最小路径和 {

    public int minPathSum(int[][] grid) {
        int m = grid.length;
        if (m == 0) {
            return 0;
        }
        int n = grid[0].length;
        if (n == 0) {
            return 0;
        }
        // 第一列
        for (int a = 1; a < m; a++) {
            grid[a][0] = grid[a - 1][0] + grid[a][0];
        }
        // 第一排
        for (int b = 1; b < n; b++) {
            grid[0][b] = grid[0][b - 1] + grid[0][b];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] = Math.min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j];
            }
        }
        return grid[m - 1][n - 1];
    }

    public static void main(String[] args) {
        最小路径和 obj = new 最小路径和();
        System.out.println(obj.minPathSum(new int[][]{
                {1, 3, 1},
                {1, 5, 1},
                {4, 2, 1}}
        ));
    }
}
