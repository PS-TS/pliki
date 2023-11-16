public class Main {
    public static void main(String[] args) {
        Book k1 = new Book("Dziady", "Adam Mickiewicz", 300);
        Book k2 = new Book("Dziady", "Adam Mickiewicz", 200);
        k2.equals(k1);
        System.out.println(k1.toString());


        Samochod s1 = new Samochod();
        s1.jedz();
    }
}