import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.

		System.out.print("podaj dwie liczby:\n");

		int a;
		int b;
		Scanner s = new Scanner(System.in);

		a = Integer.parseInt(s.nextLine());
		b = Integer.parseInt(s.nextLine());
		
		if (a > b) {
			System.out.print(a + "\n");
			System.out.print(b + "\n");
			System.out.print("pierwsza liczba jest wieksza od drugiej\n");

		} else {
			System.out.print(b + "\n");
			System.out.print(a + "\n");
			System.out.print("pierwsza liczba nie jest wieksza od drugiej\n");

		}

	}

}
