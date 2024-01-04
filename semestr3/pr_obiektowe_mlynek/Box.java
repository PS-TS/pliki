public class Box <T>{
    public T value;
    public Box(T value){
        this.value = value;
    }
    public T getValue(){
        return value;
    }
    public  void setValue(T value){
        this.value = value;
    }
}
