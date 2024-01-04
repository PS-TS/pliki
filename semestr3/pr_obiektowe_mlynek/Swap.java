import java.util.Arrays;

public class Swap {
    public static<T> void swap(T[]array, int index1, int index2){
        if(array!= null && index2>=0 && index1>=0 && index1< array.length && index2< array.length){
            T temp = array[index1];
            array[index1]=array[index2];
            array[index2]= temp;
        }
    }

    public static void main(String[] args) {
        Integer[] myArray = {1,2,3,4,5,6};
        swap(myArray,0,1);
        System.out.println(Arrays.toString(myArray));

    }
}
