Zad 1
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj pierwsza liczbe"); //sout
        int a = scanner.nextInt();
        System.out.println("Podaj druga liczbe");
        int b = scanner.nextInt();

        System.out.println("dodawanie: " + (a+b));
        System.out.println("odejmowanie: " + (a-b));
        System.out.println("mnozenie: " + (a*b));
        System.out.println("dzielenie: " + (a/b));
    }
}



zad 2
        import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj slowo 1"); //sout
        String a = scanner.next();
        System.out.println("Podaj slowo 2");
        String b = scanner.next();

        System.out.println(a + "\n" + b);
    }
}



zad 3
        import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int liczba1, liczba2, liczba3;
        System.out.println("Podaj pierwsza liczbe: ");
        liczba1 = scanner.nextInt();
        System.out.println("Podaj druga liczbe: ");
        liczba2 = scanner.nextInt();
        System.out.println("Podaj trzecia liczbe: ");
        liczba3 = scanner.nextInt();

        if(liczba1 > liczba2 && liczba1 > liczba3){
            System.out.println("Liczba " + liczba1 + " jest najwieksza");
        } else if (liczba2 > liczba1 && liczba2 > liczba3) {
            System.out.println("Liczba " + liczba2 + " jest najwieksza");
        } else if (liczba3 > liczba1 && liczba3 > liczba2) {
            System.out.println("Liczba " + liczba3 + " jest najwieksza");
        } else {
            System.out.println("Nie ma liczby najwieksze, poniewaz co najmniej dwie liczby sa takie same");
        }
    }
}




zad 4
        import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj numer dnia tygodnia: ");
        int numer_dnia = scanner.nextInt();

        switch (numer_dnia){
            case 1:
                System.out.println("Poniedzialek");
                break;
            case 2:
                System.out.println("Wtorek");
                break;
            case 3:
                System.out.println("Sroda");
                break;
            case 4:
                System.out.println("Czwartek");
                break;
            case 5:
                System.out.println("Piatek");
                break;
            case 6:
                System.out.println("Sobota");
                break;
            case 7:
                System.out.println("Niedziela");
                break;
            default:
                System.out.println("Niepoprawny numer dnia tygodnia");
        }
    }
}




Zad 5
        import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj rok: ");
        int rok = scanner.nextInt();

        if((rok % 4 == 0 && rok % 100 != 0) || rok % 400 == 0){
            System.out.println("Rok " + rok + " jest przestepny");
        } else{
            System.out.println("Rok " + rok + " nie jest rokiem przestepnym");
        }

    }
}




zad 6
public class Main {
    public static void main(String[] args) {
        for(int i = 1; i<=100; i++){
            System.out.println(i);
        }
    }
}




zad 7
public class Main {
    public static void main(String[] args) {
        int i = 1, suma = 0;
        while (i <= 50){
            suma += i;
            i++;
        }
        System.out.println("Suma: " + suma);
    }
}




zad 8
        import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int suma = 0;
        System.out.println("Podaj wartosc:");
        int liczba = scanner.nextInt();

        while (liczba != 0)
        {
            suma += liczba%10;
            liczba /= 10;
        }
        System.out.println("Suma " + suma);
    }
}




zad 9
        import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Podaj liczbe");
        int liczba = scanner.nextInt();
        int odwrocona = 0;
        while (liczba != 0) {
            int reszta = liczba % 10;
            System.out.println(reszta);

            odwrocona = odwrocona * 10 + reszta;
            System.out.println(odwrocona);

            liczba = liczba / 10;
            System.out.println(liczba);
        }
        System.out.println("Odwrocona liczba wyglada nastepujaco: " + odwrocona);
    }
}
