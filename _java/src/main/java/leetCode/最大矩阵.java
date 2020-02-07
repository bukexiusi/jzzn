package leetCode;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/4 16:53
 * @description
 */
public class 最大矩阵 {
    public int maximalRectangle(char[][] matrix) {
        return 0;
    }

    public static void main(String[] args) {
        最大矩阵 obj = new 最大矩阵();
        System.out.println(obj.maximalRectangle(new char[][]{
                {1, 0, 1, 0, 0},
                {1, 0, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 0, 0, 1, 0}
        }));
    }
}
