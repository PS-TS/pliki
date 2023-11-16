public class Main {
    public static void main(String[] args) {
        //dodac do oddzielnych metod
        //House
        House domStefana = new House();
        domStefana.area = 150;
        domStefana.floors = 2;
        domStefana.garden = false;
        domStefana.garage = true;
        domStefana.rooms = 6;
        System.out.println(domStefana.getPrice());

        House domSylwii = new House();
        domSylwii.rooms = 3;
        domSylwii.garage = true;
        domSylwii.area = 300;
        domSylwii.garden = true;
        domSylwii.floors = 1;
        System.out.println(domSylwii.getPrice());


        //Dog
        Dog pies1 = new Dog();
        pies1.age = 3;
        pies1.breed = "labrador";
        pies1.name = "Pimpek";
        pies1.bark();


        //BankAccount
        BankAccount konto1 = new BankAccount();
        konto1.balance = 4000;
        konto1.deposit(1500);
        konto1.withdraw(500);
        System.out.println(konto1.balance);


        //Time
        Time time1 = new Time();
        time1.hours = 15;
        time1.minutes = 20;
        Time time2 = new Time();
        time2.hours = 4;
        time2.minutes = 10;
        Time time3 = time1.addTime(time2);
        System.out.println("Godzina: " + time3.hours + " Minuta: " + time3.minutes);


        //Car
        Car car1 = new Car();
        car1.brand = "Audi";
        System.out.println(car1.brand);
        Car car2 = car1;
        //car2 jest zalezny od car1
        System.out.println(car2.brand);
        car1.brand = "Honda";
        System.out.println(car2.brand);


        //Osoba
        Osoba osoba1 = new Osoba();
        osoba1.imie = "Jan";


        //Rodzic, Dziecko
        Rodzic rodzic = new Rodzic();
        rodzic.wiek = 25;
        Dziecko dziecko = new Dziecko();
        dziecko.zmienWiekRodzica(rodzic);
        System.out.println(dziecko.wiekRodzica);


        //Licznik
        Licznik licznik1 = new Licznik();
        int wartosc1 = 5;
        licznik1.zwieksz(wartosc1);
        System.out.println(licznik1.liczba);
        //zmieniala sie

        Licznik licznik2 = new Licznik();
        licznik2.zwieksz(7);
        licznik2.dodaj(licznik1);
        System.out.println("Licznik1: " + licznik1.liczba + " Licznik2: " + licznik2.liczba);


        //Zmieniacz
        int zmienna1 = 3;
        Zmieniacz zmieniacz = new Zmieniacz();
        zmieniacz.zmienWartosc(zmienna1);
        System.out.println("Zmienna1: " + zmienna1);


        //Zmieniacz i Licznik
        Licznik licznik3 = new Licznik();
        zmieniacz.zmienObiekt(licznik3);
        System.out.println("Licznik3: " + licznik3.liczba);
    }
}