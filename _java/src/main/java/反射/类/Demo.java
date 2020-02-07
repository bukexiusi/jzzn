package 反射.类;

import java.lang.reflect.Field;

/**
 * @author 图南
 * @version 1.0
 * @email 935281275@qq.com
 * @date 2020/1/30 23:08
 * @description
 */


class Dog {
    static {
        System.out.println("Loading Dog");
    }

    public  String nickname;
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
class Cat {
    static {
        System.out.println("Loading Cat");
    }
}

public class Demo {


    public static void main(String[] args) throws Exception {

        Class a = int.class;
        Class b = Integer.TYPE;
        Class c = Integer.class;
        System.out.println(System.identityHashCode(a));
        System.out.println(System.identityHashCode(b));
        System.out.println(System.identityHashCode(c));
        System.out.println(a == b);
        System.out.println(b == c);
        System.out.println(a == c);

        Class clz = Class.forName("反射.类.Dog");
        Class clz2 = Dog.class;
        Class clz3 = new Dog().getClass();
        System.out.println(clz == clz2);
        System.out.println(clz2 == clz3);

        Object obj = clz.newInstance();
        Dog dog = (Dog) obj;
        dog.setName("旺财");

        Field field = dog.getClass().getDeclaredField("name");
        field.setAccessible(true);
        System.out.println(field.get(dog));
        System.out.println(field.get(obj));
        field.set(dog, "帕吉");
        System.out.println(field.get(dog));
        System.out.println(field.get(obj));

        Class dogClaz = Dog.class;
        Field[] fields = dogClaz.getDeclaredFields();

    }

}
