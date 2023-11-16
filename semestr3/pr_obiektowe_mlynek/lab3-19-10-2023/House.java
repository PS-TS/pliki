public class House {
    public int area;
    public boolean garage;
    public int rooms;
    public boolean garden;
    public int floors;

    public int getPrice(){
        return area * 3000;
    }
}
