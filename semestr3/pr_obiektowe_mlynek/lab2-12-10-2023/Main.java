zad1
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        odwrocLiczbe();
    }
    public static void odwrocLiczbe(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbe");
        int liczba = scanner.nextInt();
        int odwrocona = 0;
        while(liczba != 0){
            odwrocona = odwrocona * 10 + liczba % 10;
            liczba/=10;
        }
        System.out.println(odwrocona);
    }
}

albo

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(odwrocLiczbe());
    }

    public static int odwrocLiczbe(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj liczbe");
        int liczba = scanner.nextInt();
        int odwrocona = 0;
        while(liczba != 0){
            odwrocona = odwrocona * 10 + liczba % 10;
            liczba/=10;
        }
        return odwrocona;
    }
}

albo


import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        int liczba = random.nextInt(10,15);
        double liczba2 = random.nextDouble(10.0, 20.0);
        System.out.println(liczba2);
    }
}



zad2
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        piramida();
    }

    public static void zad5(){
        Random random = new Random();
        int[] tab = new int[10];
        for(int i=0; i<10; i++){
            tab[i] = random.nextInt();
        }
        for (int i=9; i>=0; i--){
            System.out.println(tab[i]);
        }
    }


    public static void zad6(){
        Random random = new Random();
        double suma = 0;
        int[] tab2 = new int[20];
        for(int i=0; i<=19; i++){
            tab2[i] = random.nextInt(1, 100);
            suma += tab2[i];
        }
        double srednia = suma/20;
        System.out.println(suma + " " + srednia);
    }



    public static void zad7(){
        Random random = new Random();
        double suma = 0;
        int[] tab = new int[15];
        for(int i=0; i<14; i++){
            tab[i] = random.nextInt();



        }
    }





    public static void piramida(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj znak ");
        String znak = scanner.next();
        System.out.println("Podaj wysokosc piramidy ");
        int wysokosc = scanner.nextInt();



        for (int i=0; i<wysokosc; i++){
            int liczbaspacji = wysokosc - i - 1;
            int iloscznakow = 2 * i + 1;
            StringBuilder sb = new StringBuilder();
            while(liczbaspacji-->0){
                sb.append(' ');
            }
            while(iloscznakow-->0){
                sb.append(znak);
            }
            System.out.println(sb.toString());
        }
    }
}





zad3
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        reverseString();
    }

    public static void reverseString(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj napis");
        String napis = "Kot";



        StringBuilder str = new StringBuilder(napis);
        StringBuilder odwr = str.reverse();
        System.out.println("Odwrocony = " + odwr.toString());
    }
}



zad4
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        zad11();
    }


    public static void zad11(){
        Random random = new Random();
        ArrayList<Integer> lista = new ArrayList<Integer>();



        for(int i = 0; i < 10; i++){
            lista.add(random.nextInt(1, 100));
            System.out.println("Liczba " + lista.get(i));
        }


        System.out.println("Odwrocone:");
        for(int i = 9; i >= 0; i--){
            System.out.println("Liczba " + lista.get(i));
        }
    }
}



zad10
public static void reverseString(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Podaj napis");
        String napis = "Kot";


        StringBuilder str = new StringBuilder(napis);
        StringBuilder odwr = str.reverse();
        System.out.println("Odwrocony = " + odwr.toString());
        }





zad11
import java.util.*;

public class Main {
    public static void main(String[] args) {
        zad11();
    }

    public static void zad11(){
        Random random = new Random();
        ArrayList<Integer> lista= new ArrayList<Integer>();


        for(int i = 0; i < 10; i++){
            lista.add(random.nextInt(1, 100));
            System.out.println("Liczba " + lista.get(i));
        }


        System.out.println("Odwrocone:");
        for(int i = 9; i >= 0; i--){
            System.out.println("Liczba " + lista.get(i));
        }


        Collections.sort(lista);
        System.out.println("Posortowane:");
        for(int i = 9; i >= 0; i--){
            System.out.println("Liczba " + lista.get(i));
        }
    }
}