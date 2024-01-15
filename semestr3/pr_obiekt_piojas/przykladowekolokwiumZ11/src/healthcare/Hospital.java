package healthcare;

public class Hospital implements Cloneable {
    private String name;
    private double capacity;

    public Hospital(String name, double capacity) {
        this.name = (name == null) ? "" : name;
        this.capacity = (capacity<=0)? 50.0: capacity;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() +
                " name='" + name + '\'' +
                ", capacity=" + capacity
                ;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public Hospital clone() {
        try {
            Hospital clone = (Hospital) super.clone();
            return clone;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
