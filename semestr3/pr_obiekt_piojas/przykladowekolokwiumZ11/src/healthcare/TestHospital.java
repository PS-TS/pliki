package healthcare;

public class TestHospital {
    public static void main(String[] args) {
        Hospital hospital = new Hospital("A", 34.5);
        Hospital hospital2 = hospital.clone();
        System.out.println(hospital);
        System.out.println(hospital2);
        hospital.setName("B");
        System.out.println(hospital);
        System.out.println(hospital2);
    }
}
