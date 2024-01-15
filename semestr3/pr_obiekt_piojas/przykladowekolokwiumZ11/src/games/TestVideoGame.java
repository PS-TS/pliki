package games;

import java.util.ArrayList;
import java.util.Arrays;

public class TestVideoGame {
    public static void main(String[] args) {
        ArrayList<VideoGame> list = new ArrayList<VideoGame>();
        list.add(new VideoGame("A","A",42));
        list.add(new VideoGame("AA","A",42));
        list.add(new VideoGame("AAA","A",42));
        list.add(new VideoGame("AAAA","A",42));
        list.sort(null);
        for(VideoGame game : list){
            System.out.println(game);
        }

    }
}
