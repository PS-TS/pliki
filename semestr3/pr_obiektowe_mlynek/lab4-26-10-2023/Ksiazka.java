public class Ksiazka {
    public String autor;
    public String tytul;
    public int rokWydania;

    public Ksiazka(){

    }

    public Ksiazka(String tytul, String autor, int rokWydania){
        this.autor = autor;
        this.rokWydania = rokWydania;
        this.tytul = tytul;
    }
}
