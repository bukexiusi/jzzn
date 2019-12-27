# jvm knowledge points

+ the class file format
+ data type
  + primitive types
    + the numeric types
      + the intergral types
      + the floating-point types
    + the boolean type
    + the returnAddress type
      + returnAddress 数据只存在于字节码层面，与编程语言无关，也就是说，我们在 Java 语言中是不会直接与 returnAddress 类型的数据打交道的。
      + 每个线程有自己的程序计数器（pc register），而 pc 中的值就是当前指令所在的内存地址，即 returnAddress 类型的数据，当线程执行 native 方法时，pc 中的值为 undefined。
  + reference types