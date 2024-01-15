package kolekcje.zadA1;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;

public class TestA1 {

    public static void main(String[] args) {
        ArrayList<Integer> list1 = new ArrayList<>();
        list1.add(3);
        list1.add(6);
        list1.add(-12);
        list1.add(14);
        list1.add(3);
        printUnique(list1);
        HashSet<Object> objects = new HashSet<>();
        HashSet<String> h1 = new HashSet<>();
        h1.add("hhh");
        h1.add("hhh");
        h1.add("tt");
        printUnique(h1);

    }

    public static <T> void printUnique(Collection<T> items){
        HashSet<T> temp = new HashSet<>();
        for(var elem: items){
                temp.add(elem);

        }
        for(var elem: temp){
            System.out.println(elem);
        }
    }
}
