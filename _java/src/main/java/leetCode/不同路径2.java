package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 14:01
 * @description
 *
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 *
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 *
 * 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
 *
 */
public class 不同路径2 {

    /**
     *
     * 坑在于第一列或者第一排的其中一个数走不通，则之后的路也就走不通
     * */
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // 可复用obstacleGrid
        int m = obstacleGrid.length;
        if (m == 0) {
            return 0;
        }
        int n = obstacleGrid[0].length;
        if (n == 0) {
            return 0;
        }
        int[][] opt = new int[m][n];
        // 第一列
        int e = 1;
        for (int a = 0; a < m; a++) {
            if (obstacleGrid[a][0] == 1) {
                e = 0;
            }
            opt[a][0] = e;
        }
        // 第一排
        e = 1;
        for (int b = 0; b < n; b++) {
            if (obstacleGrid[0][b] == 1) {
                e = 0;
            }
            opt[0][b] = e;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                opt[i][j] = obstacleGrid[i][j] == 0 ? opt[i - 1][j] + opt[i][j - 1] : 0;
            }
        }
        return opt[m - 1][n - 1];
    }

    public static void main(String[] args) {
        不同路径2 obj = new 不同路径2();
        System.out.println(obj.uniquePathsWithObstacles(new int[][]{
                {1, 0}}));
    }

}
