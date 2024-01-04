public class zad2{

    public static <T> boolean isEqual(T other, T other2){
        return (other.equals(other2));
    }

    public static void main(String[] args) {
        System.out.println(zad2.isEqual(1,2));
        int a = 2;
        String c ="ab";
        System.out.println(zad2.isEqual(a,c));

    }
}
