public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, powinny zostac zwrocone 
		//cyfry pobranej liczby poczynajac od cyfry jednosci.

		System.out.print("Podaj liczbe");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		while (a > 0) {
			System.out.print(a % 10);
			System.out.print("\n");
			a = a / 10;
		}

	}

}
