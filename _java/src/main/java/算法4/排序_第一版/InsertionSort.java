package 算法4.排序_第一版;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/6 16:51
 * @description 插入排序（冒泡排序）
 *
 * 选择排序 -> 插入排序 -> 希尔排序
 */
public class InsertionSort {

    public static <T extends Number & Comparable<T>> void sort(T[] array) {
        int L = array.length;
        for (int i = 1; i < L; i++) {
            for (int j = i - 1; j > -1 && array[j + 1].compareTo(array[j]) < 0; j--) {
                T temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }

    public static void main(String[] args) {

        Integer[] array = new Integer[]{
                9, 3, 0, 2, 10, 7, 11
        };
        System.out.println("排序前");
        for (Integer i : array) {
            System.out.print(i + " ");
        }
        InsertionSort.sort(array);
        System.out.println("");
        System.out.println("排序后");
        for (Integer i : array) {
            System.out.print(i + " ");
        }
    }
}
