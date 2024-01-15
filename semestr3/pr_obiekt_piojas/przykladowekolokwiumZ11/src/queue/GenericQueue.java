package queue;

import java.util.LinkedList;

public class GenericQueue<T> {
    private LinkedList<T> list = new LinkedList<>();
    public void enqueue(T element){
        list.add(element);
    }
    public T dequeue(){
      if(list.isEmpty()){
          throw new IllegalStateException("Kolejka jest pusta");
      }
      return list.removeFirst();
    }


}
