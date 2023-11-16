public class Licznik {
    public int liczba;


    public void zwieksz(int wartosc){
        liczba += wartosc;
    }

    public void dodaj(Licznik licznik2){
        this.liczba += licznik2.liczba;
    }
}
