import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Czy liczba jest numerem tygodnia/miesiaca?

		System.out.print("Podaj liczbe:\n");
		Scanner s = new Scanner(System.in);
		int a = Integer.parseInt(s.nextLine());

		if (a >= 1 && a<= 7) {
			System.out.print("Liczba jest poprawnym numerem tygodnia\n");
		} else {
			System.out.print("Liczba nie jest poprawnym numerem tygodnia\n");
		}

		if (a >= 1 && a<= 12) {
			System.out.print("Liczba jest poprawnym numerem miesiaca\n");
		} else {
			System.out.print("Liczba nie jest poprawnym numerem miesiaca\n");
		}

	}

}
