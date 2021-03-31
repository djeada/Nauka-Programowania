import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, wyswietl liczbe Pi tyle razy 
		//ile wynosi pobrana liczba, z dokladnoscia do tylu 
		//miejsc po przecinku ile wynosi pobrana liczba.

		System.out.print("Podaj liczbe\n");
		Scanner s = new Scanner(System.in);
		int a = Integer.parseInt(s.nextLine());

		int suma = 0;

		while (a > 0) {
			suma += (a % 10);
			a = a / 10;
		}

		System.out.print("Suma cyfr podanej liczby wynosi " + suma + "\n");

	}

}
