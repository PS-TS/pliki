package university;

public class Student implements Comparable<Student>{
    private String name;
    private float grade;

    public Student(String name, float grade) {
        this.name = name;
        this.grade = grade;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() +
                " name='" + name + '\'' +
                ", grade=" + grade ;
    }

    @Override
    public int compareTo(Student o) {
        return Float.compare(this.grade,o.grade);
    }

}
