import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Wypisz pobrana od uzytkownika liczbe, jesli jest wieksza od 5.

		System.out.print("podaj liczbe:\n");
		
		Scanner s = new Scanner(System.in);
		int x = Integer.parseInt(s.nextLine());

		if (x > 5) {
			System.out.print(x);
			System.out.print("\n");
		}

	}

}
