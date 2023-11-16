public class Osoba {
    public String imie;
    public String nazwisko;
    public int wiek;

    public Osoba(String imie, String nazwisko, int wiek){
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.wiek = wiek;
    }

    public Osoba(String imie, String nazwisko){
        this(imie, nazwisko, 0);
    }
}
