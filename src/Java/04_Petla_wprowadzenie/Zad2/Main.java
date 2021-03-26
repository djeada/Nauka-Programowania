public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, powinny zostac wyswietlone 
		//wszystkie liczby naturalne mniejsze od podanej liczby.

		System.out.print("Podaj liczbe");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		for (int i = 1; i<a; i++) {
			System.out.print(i);
			System.out.print(" ");
		}

		System.out.print("\n");

	}

}
