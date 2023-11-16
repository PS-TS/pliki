public class OsobaStatic {
    public String imie;
    public static int licznik = 0;

    public OsobaStatic(String imie){
        this.imie = imie;
        licznik++;
    }

    public static int getLicznik(){
        return licznik;
    }
}
