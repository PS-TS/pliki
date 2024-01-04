public class Counter <T>{

    public T value;
    public int count;
    public void add(T element){
        count++;
    }
    public int getCount() {
        return count;
    }

    public static void main(String[] args) {
        Counter c1 = new Counter();
        c1.add(1);
        c1.add("cos");
        System.out.println(c1.getCount());
    }
}
