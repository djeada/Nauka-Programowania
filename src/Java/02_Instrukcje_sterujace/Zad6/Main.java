public class Main {
	public static void main(String[] args) {

		//Dla pobranych czterech liczb, znajdz najwieksza liczbe. 

		System.out.print("podaj cztery liczby:");
		System.out.print("\n");

		int a;
		int b;
		int c;
		int d;

		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());
		c = Integer.parseInt(System.console().readLine());
		d = Integer.parseInt(System.console().readLine());

		int maksAB = a > b ? a : b;
		int maksCD = c > d ? c : d;
		int maks = maksAB > maksCD ? maksAB : maksCD;

		System.out.print(maks);
		System.out.print("\n");

	}

}
