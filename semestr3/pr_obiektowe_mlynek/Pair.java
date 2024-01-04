import org.jetbrains.annotations.NotNull;

import java.util.Arrays;

public class Pair <T>{
    public T first;
    public T second;

    public Pair(T first, T second){
        this.first = first;
        this.second = second;
    }
    public T getFirst() {
        return first;
    }
    public T getSecond() {
        return second;
    }
}
class Plant implements Comparable<Plant>{
    @Override
    public int compareTo(@NotNull Plant o) {
        return 0;
    }
}

class Tree extends Plant{
    public int height;

    public Tree(int height){
        this.height = height;
    }
    public int getHeight() {
        return height;
    }
}
public class cos {
    public static void findMinMaxHeight(Tree[] trees, Pair<? super Tree> result) {
        if (trees != null && trees.length != 0) {
            Arrays.sort(trees, Comparable::compareTo);
            result.getFirst().height = trees[0].getHeight();
            result.getSecond().height = trees[trees.length -1].getHeight();
        }
    }

    public static void main(String[] args) {
        Tree[] trees = {
                new Tree(1),
                new Tree(20),
                new Tree(8),
        };
        Pair<Tree> result = new Pair<>(new Tree(0), new Tree(0));
        findMinMaxHeight(trees,result);
        System.out.println(result.getFirst().getHeight());
        System.out.println(result.getSecond().getHeight());
    }
}