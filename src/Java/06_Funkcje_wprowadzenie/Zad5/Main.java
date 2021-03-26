public class Main {
	//Napisz funkcje, ktora:

	//a) dla podanych dwoch liczb, zwroci mniejsza
	public static int min2(int a, int b) {
		return a<b ? a : b;
	}

	//b) dla podanych dwoch liczb, zwroci wieksza
	public static int maks2(int a, int b) {
		return a > b ? a : b;
	}

	//c) dla podanych trzech liczb, zwroci najmniejsza
	public static int min3(int a, int b, int c) {
		int minAB = a<b ? a : b;
		return minAB<c ? minAB : c;
	}

	//d) dla podanych trzech liczb, zwroci najwieksza
	public static int maks3(int a, int b, int c) {
		int maksAB = a > b ? a : b;
		return maksAB > c ? maksAB : c;
	}

	public static void main(String[] args) {
		System.out.print("Podaj dwie liczby: ");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());
		int b;
		b = Integer.parseInt(System.console().readLine());

		System.out.print("mniejsza liczba to: ");
		System.out.print(min2(a, b));
		System.out.print("\n");
		System.out.print("wieksza liczba to: ");
		System.out.print(maks2(a, b));
		System.out.print("\n");

		System.out.print("Podaj trzy liczby: ");
		System.out.print("\n");
		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());
		int c;
		c = Integer.parseInt(System.console().readLine());

		System.out.print("najmniejsza liczba to: ");
		System.out.print(min3(a, b, c));
		System.out.print("\n");
		System.out.print("najwieksza liczba to ");
		System.out.print(maks3(a, b, c));
		System.out.print("\n");

	}

}
