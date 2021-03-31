import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, powinna zostac wyswietlona suma 
		//wszystkich liczb naturalnych mniejszych od pobranej liczby.

		System.out.print("Podaj liczbe: \n");
		Scanner s = new Scanner(System.in);
		int n = Integer.parseInt(s.nextLine());

		int suma = 0;

		for (int i = 1; i<n; i++) {
			suma += i;
		}

		System.out.print(suma + "\n");

	}
}
