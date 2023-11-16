public class Person {
    private String firstName;
    protected String lastName;

    public Person(){}
    public Person(String firstName, String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }
    public String getFirstName() {
        return firstName;
    }

    public String getLastName(){
        return lastName;
    }
}


class Employee extends Person{
    public Employee(String firstName, String lastName){
        super(firstName, lastName);
    }

    public void displayData(){
        String pracownikImie = getFirstName();
        String pracownikNazwisko = getLastName();
        System.out.println("Imie i nazwisko pracownika: " + pracownikImie + pracownikNazwisko);
    }
}