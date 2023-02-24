import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, powinny zostac wyswietlone 
		//wszystkie liczby naturalne mniejsze od podanej liczby.

		System.out.print("Podaj liczbe\n");
		Scanner s = new Scanner(System.in);
		int a = Integer.parseInt(s.nextLine());

		for (int i = 1; i<a; i++) {
			System.out.print(i);
			System.out.print(" ");
		}

		System.out.print("\n");

	}
}
