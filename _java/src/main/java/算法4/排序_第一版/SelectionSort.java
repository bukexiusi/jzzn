package 算法4.排序_第一版;


/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/2/6 16:00
 * @description 选择排序
 *
 * 选择排序 -> 插入排序 -> 希尔排序
 */
public class SelectionSort {

    public static <T extends Number & Comparable<T>> void sort(T[] array) {
        // 前面一部分表示类型参数T必须是Number的子类，后面一部分表示T实现了Comparable接口。
        int L = array.length;
        for (int i = 0; i < L; i++) {
            int minIdx = i;
            for (int j = i + 1; j < L; j++) {
                if (array[j].compareTo(array[minIdx]) < 0) minIdx = j; // 此处没考虑空的情况，假定数组每个位置都有值
            }
            T temp = array[i];
            array[i] = array[minIdx];
            array[minIdx] = temp;
        }
    }

//    private static <T extends Number & Comparable<? super T>> T min(T[] values) {
//     前面一部分表示类型参数T必须是Number的子类，后面一部分表示T或者T的父类实现了Comparable接口。
//        if (values == null || values.length == 0) return null;
//        T min = values[0];
//        for (int i = 1; i < values.length; i++) {
//            if (min.compareTo(values[i]) > 0) min = values[i];
//        }
//        return min;
//    }

    public static void main(String[] args) {
        Integer[] array = new Integer[]{
                9, 3, 0, 2, 10, 7, 11
        };
        System.out.println("排序前");
        for(Integer i: array) {
            System.out.print(i + " ");
        }
        SelectionSort.sort(array);
        System.out.println("");
        System.out.println("排序后");
        for(Integer i: array) {
            System.out.print(i + " ");
        }
    }

}
