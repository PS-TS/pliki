import org.jetbrains.annotations.NotNull;

import java.util.Arrays;

public class MinValue {
    public static  <T extends Comparable<T>> T minValue(T[] array){
        if(array != null && array.length!=0){
            Arrays.sort(array);
            T min = array[0];
            return min;
        }
        return minValue(array);
    }

    public static void main(String[] args) {
        Integer[] array = {2,1,3,4,5,6,0,-100};
        System.out.println(minValue(array));
        Double[] array2 = {0.0, -1.0, 0.21};
        System.out.println(minValue(array2));
        String[] array3 = {"cos","nwm"};
        System.out.println(minValue(array3));
        Person[] array4 = {
                new Person("ktos", 1),
                new Person("ktos2", 3)
        };
        System.out.println(minValue(array4).getName());
    }
}
class Person implements Comparable<Person>{
    public String name;
    public int age;

    public Person(String name, int age){
        this.age = age;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    @Override
    public int compareTo(@NotNull Person o) {
        return Integer.compare(this.age, o.age);
    }
}


