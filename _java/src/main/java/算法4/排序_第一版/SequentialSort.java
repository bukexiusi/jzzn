package 算法4.排序_第一版;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/6 19:45
 * @description
 */
public class SequentialSort {

    public static<T extends Number & Comparable<T>> void sort(T[] array) {
        int L = array.length;
        int mid = L / 2;
        sort(array, 0, mid);
        sort(array, mid + 1, L - 1);

    }

    private static<T extends Number & Comparable<T>> void sort(T[] array, int start, int end) {

    }

    public static void main(String[] args) {

    }
}
