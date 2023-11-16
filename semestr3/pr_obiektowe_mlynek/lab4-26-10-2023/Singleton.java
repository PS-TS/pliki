public class Singleton {
    private static Singleton instance;
    public int counter;

    private Singleton(){

    }

    public static Singleton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        instance.counter++;
        return instance;
    }
}
