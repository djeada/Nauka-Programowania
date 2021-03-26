public class Main {
	public static void main(String[] args) {

		//Dla dwoch pobranych liczb, sprawdz czy pobrane liczby sa identyczne.

		System.out.print("podaj dwie liczby:");
		System.out.print("\n");
		int a;
		int b;

		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());

		if (a == b) {
			System.out.print("liczby sa jednakowe");
			System.out.print("\n");
		} else {
			System.out.print("liczby sa rozne");
			System.out.print("\n");
		}
	}

}
