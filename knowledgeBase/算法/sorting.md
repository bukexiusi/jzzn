# <center>Sorting</center>

# 选择排序

<font color="gree">算法理念</font>
找到数组中最小（最大）的元素，让其与第一个元素交换。找到数组中第二小（大）的元素，让其与第二个元素交换。以此类推。

<font color="gree">代码构思</font>
找到数组中最小（最大）的元素 -> 双层循环 -> 让元素依次与其后的元素比大小

<font color="gree">复杂度</font>
T(n)=O(n^2) -> n^2级别比较次数
N次交换

<font color="gree">特点</font>
<font color="orange">运行时间与输入无关</font>

  + 长度相同的排好序的数组和混乱的数组运行时间一样
    + 无论第一个是不是最小（最大）元素，都需要和后面的元素相比
      + 没有利用数组的初始化条件
  
<font color="orange">数据移动最少（比其他任何算法）</font>

  + 移动N次

## 插入排序（冒泡排序）

<font color="gree">算法理念</font>
从第i个元素开始，与第i-1个元素对比大小，若小则交换第i个元素和第i-1个元素，直至原来的第i个元素大于第i-n个元素停止交换。

  + 依次对比之前元素，直至大于
  + 当第i个元素开始对比之前，0...i-1已经按照大小排好序。

<font color="gree">代码构思</font>
略

<font color="gree">复杂度</font>
T(n)=O(n^2) ~ 0 -> n^2~0级别比较次数
交换次数 n^2级别 ~ N-1

<font color="gree">特点</font>
<font color="orange">当数组越接近升序（降序），则排列效率约高</font>

  + 当数组越整齐，此方法是最高效的

## 希尔排序

<font color="gree">算法理念</font>
插入排序进阶版本，插入排序是相邻元素对比，希尔排序是不相邻元素对比

<font color="gree">代码构思</font>
h = 相隔数，当h为4时，索引为0，4，8，12的元素为一组进行插入排序
h = 1, 4, 13, 40...
-> 40 / 3 = 13
-> 13 / 3 = 4
-> 4 / 3 = 1

如何选择h是一个世界难题，以后我会使用1，4，13...
while (h < L/3) h = 3*h + 1; // 其中L为数据长度

<font color="gree">复杂度</font>
T(n)=O(n^(3/2))，下界是n*log2n

<font color="gree">特点</font>