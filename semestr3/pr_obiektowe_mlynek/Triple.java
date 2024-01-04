public class Triple <T, U, V>{
    public T value1;
    public U value2;
    public V value3;

    public T getValue1() {
        return value1;
    }

    public U getValue2() {
        return value2;
    }

    public V getValue3() {
        return value3;
    }
    public Triple(T first, U second, V third){
        this.value1 = first;
        this.value2 = second;
        this.value3 = third;
    }

    public static void main(String[] args) {
        Triple t1 = new Triple(1, 2.0, true);
        System.out.println(t1.getValue1());
        System.out.println(t1.getValue2());
        System.out.println(t1.getValue3());
    }
}

