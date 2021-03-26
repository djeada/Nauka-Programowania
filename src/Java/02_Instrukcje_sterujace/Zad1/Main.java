public class Main {
	public static void main(String[] args) {

		//Wypisz pobrana od uzytkownika liczbe, jesli jest wieksza od 5.

		System.out.print("podaj liczbe:");
		System.out.print("\n");
		int x;
		x = Integer.parseInt(System.console().readLine());

		if (x > 5) {
			System.out.print(x);
			System.out.print("\n");
		}

	}

}
