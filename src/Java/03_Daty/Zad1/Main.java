public class Main {
	public static void main(String[] args) {

		//Czy liczba jest numerem tygodnia/miesiaca?

		System.out.print("Podaj liczbe:");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		if (a >= 1 && a<= 7) {
			System.out.print("Liczba jest poprawnym numerem tygodnia");
			System.out.print("\n");
		} else {
			System.out.print("Liczba nie jest poprawnym numerem tygodnia");
			System.out.print("\n");
		}

		if (a >= 1 && a<= 12) {
			System.out.print("Liczba jest poprawnym numerem miesiaca");
			System.out.print("\n");
		} else {
			System.out.print("Liczba nie jest poprawnym numerem miesiaca");
			System.out.print("\n");
		}

	}

}
