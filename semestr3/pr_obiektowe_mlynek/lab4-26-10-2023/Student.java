public class Student {
    public String imie;
    public String nazwisko;
    public String kierunekStudiow;

    public Student(String imie, String nazwisko){
        this(imie, nazwisko, "nieznany");
    }

    public Student(String imie, String nazwisko, String kierunekStudiow){
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.kierunekStudiow = kierunekStudiow;
    }
}
