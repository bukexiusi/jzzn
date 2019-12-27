# jvm

## summary

## The Structure of the Java Virtual Machine

### The class File Format

1. Compiled code to be executed by the Java Virtual Machine is represented using a ==hardware- and operating system-independent== binary format
    + 与硬件和操作系统无关的二进制格式

2. typically (==but not necessarily==) stored in a file, known as the class file format
    + class不是唯一的可被jvm识别的文件类型
3. Each class file contains the definition of a single class or interface
4. A class file consists of a stream of ==8-bit bytes==. All 16-bit, 32-bit, and 64-bit quantities are constructed by reading in two, four, and eight ==consecutive 8-bit bytes==, respectively. Multibyte data items are always stored in ==big-endian order==, where the high bytes come first
    + class文件由8比特字节流构成
    + 各个数据项目严格按照顺序紧凑地排列在Class文件之中，中间没有添加任何分隔符，Class文件中存储的内容几乎全部是程序运行的必要数据，没有空隙存在
    + 高位在前
5. This chapter presents the class file format using pseudostructures written in a ==C-like structure== notation
    + 类c结构体结构
6. In the Java SE platform, this format is supported by interfaces java.io.DataInput and java.io.DataOutput and classes such as java.io.DataInputStream and java.io.DataOutputStream.
    + java代码中可通过如上接口读取class类型文件
    + todo，读取代码示例
7. as follows

    ```txt
    ClassFile {
        u4             magic;
        u2             minor_version;
        u2             major_version;
        u2             constant_pool_count;
        cp_info        constant_pool[constant_pool_count-1];
        u2             access_flags;
        u2             this_class;
        u2             super_class;
        u2             interfaces_count;
        u2             interfaces[interfaces_count];
        u2             fields_count;
        field_info     fields[fields_count];
        u2             methods_count;
        method_info    methods[methods_count];
        u2             attributes_count;
        attribute_info attributes[attributes_count];
    }
    ```

    类型|英文名称|中文名称|作用|
    -|-|-|-|-|
    u4|magic|魔数|识别是否class类型文件，值为Oxcafebabe|
    u2|minor_version|次版本|jdk版本|
    u2|major_version|主版本|jdk版本|Ox0034代表可被jdk1.8及其以上版本虚拟机执行，低版本执行会抛错java.lang.UnsupportedClassVersionError
    u2|constant_pool_count|常量池索引数量|
    cp_info|constant_pool|常量池|
    u2|access_flags|访问标记|
    u2|this_class|类索引|
    u2|super_class|父类索引|
    u2|interfaces_count|实现接口数量|
    u2|interfaces[interfaces_count]|接口|
    u2|fields_count|字段数量|
    field_info|fields[fields_count]|字段
    u2|methods_count|方法数量
    method_info|methods[methods_count]|方法
    u2|attributes_count|属性数量
    attribute_info|attributes[attributes_count]|属性
    1. 魔数
        + 它的唯一作用是确定这个文件是否是一个能被虚拟机接收的Class文件，值为Oxcafebabe，Ox代表十六进制
        + 很多文件存储标准中都用魔数来进行文件识别，比如gif、png、jpeg等，文件后缀易于修改，用于识别文件类型准确性低，魔数识别文件类型准确性更高
    2. 版本
        + 低版本(minor_version)
        + 高版本(major_version)
    3. 常量池
        + constant_pool_count
            + A constant_pool index is considered valid if it is ==greater than zero and less than constant_pool_count==
                + 常量池索引大于零小于constant_pool_count，即索引从1开始
            + with the exception for constants of type long and double noted in §4.4.5.
                + todo
        + constant_pool
            + javap -v
                + 上述命令查看常量池
            + The constant_pool table is indexed from 1 to constant_pool_count - 1.
            + 常量池中主要存放两大类常量：字面量和符号引用
                + 字面量
                + 符号引用
                    + 将常量池中的==符号引用(占位符)替换为直接引用==
                    + Java代码在编译的时候，是在虚拟机加载Class文件的时候才会动态链接，也就是说Class文件中不会保存各个方法、字段的最终内存布局信息，因此这些字段、方法的符号引用不经过运行期转换的话无法获得真正的内存入口地址，也就无法直接被虚拟机使用。当虚拟机运行时，需要从常量池获得对应的符号引用，再在类创建时或运行时解析、翻译到具体的内存地址之中
    4. 访问标记
         + 在常量池结束后，紧接着的两个字节代表访问标志（Access Flags），该标志用于识别一些==类或者接口层次的访问信息==，其中包括：Class是类还是接口、是否定义为public、是否定义为abstract类型、类是否被声明为final等
         + ACC_INTERFACE - 0x0200 - 是否为接口
         + ==所有标记都占一个位，并通过位运算得到==，如100 10 1分别代表三个标志位，100|10|1 = 111则能得到三个标记的true和false
    5. 索引
        Class文件依靠这些索引数据来确定这个类的继承关系。所有类（除了java.lang.Object）都只有一个父类索引（Java的单继承），即父类索引不为0，只有java.lang.Object的父类索引为0。
    4. 访问标记