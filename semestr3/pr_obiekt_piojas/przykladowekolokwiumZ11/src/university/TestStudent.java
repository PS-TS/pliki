package university;

import java.util.Arrays;

public class TestStudent {
    public static void main(String[] args) {

        Student[] students = new Student[7];
        students[0]= new Student("A", 2.3F);
        students[1]= new Student("B", 3.4F);
        students[2]= new Student("C", 4.5F);
        students[3]= new Student("D", 2.4F);
        students[4]= new Student("E", 3.5F);
        students[5]= new Student("F", 4.6F);
        students[6]= new Student("G", 3.2F);

        // kolejnosc rosnaca 2.3;2.4;3.2;3.4;3.5;4.5;4.6, wartosc srodkowa 3.4 student B

        Arrays.sort(students);

        Student median  = findMedian(students);
        System.out.println(median);

        //Student[] students1 = new Student[5];
        //Student median1 = findMedian(students1);
        //System.out.println(median1);





    }
    public static <T extends Comparable<T>> T findMedian(T[] array) {
        if(array == null || array.length == 0){
            return null;
        }
        T med = array[array.length/2];

        return med;
    }
}
