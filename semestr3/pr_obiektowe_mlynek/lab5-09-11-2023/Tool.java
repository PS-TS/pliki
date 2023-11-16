public class Tool {
    String narzedzie;
    protected Tool(String narzedzie){
        this.narzedzie = narzedzie;
    }
}

class Hammer extends Tool{
    protected Hammer(String narzedzie){
        super(narzedzie);
    }
}