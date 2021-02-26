
public class Main
{
	public static void main(String[] args)
	{

		//Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.

		System.out.print("podaj x");
		System.out.print("\n");
		int x;
		x = Integer.parseInt(System.console().readLine());

		System.out.print("3*x+10");
		System.out.print("\n");
		System.out.print(3 * x + 10);
		System.out.print("\n");

		//Pobierz wspolczynniki a, b oraz punkt x i wyznacz wartosc funkcji y = ax + b w zadanym punkcie.

		System.out.print("podaj a");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		System.out.print("podaj b");
		System.out.print("\n");
		int b;
		b = Integer.parseInt(System.console().readLine());

		System.out.print("podaj x");
		System.out.print("\n");
		x = Integer.parseInt(System.console().readLine());

		System.out.print("a*x+b");
		System.out.print("\n");
		System.out.print(a * x + b);
		System.out.print("\n");

		//Wyznacz wartosc funkcji y = x^3 + 2x^2 - 20 w zadanym punkcie.

		System.out.print("podaj x");
		System.out.print("\n");
		x = Integer.parseInt(System.console().readLine());

		System.out.print("y = x**3 + 2x**2 - 20");
		System.out.print("\n");
		System.out.print(Math.pow(x,3) + 2 * Math.pow(x,2) - 20);
		System.out.print("\n");

		//Pobierz wspolczynniki a, b, c, d, m, n oraz punkt x i wyznacz wartosc funkcji y = a*x^m + b*x^n + c - a w zadanym punkcie.

		System.out.print("podaj a");
		System.out.print("\n");
		a = Integer.parseInt(System.console().readLine());

		System.out.print("podaj b");
		System.out.print("\n");
		b = Integer.parseInt(System.console().readLine());

		System.out.print("podaj c");
		System.out.print("\n");
		int c;
		c = Integer.parseInt(System.console().readLine());

		System.out.print("podaj d");
		System.out.print("\n");
		int d;
		d = Integer.parseInt(System.console().readLine());

		System.out.print("podaj m");
		System.out.print("\n");
		int m;
		m = Integer.parseInt(System.console().readLine());

		System.out.print("podaj n");
		System.out.print("\n");
		int n;
		n = Integer.parseInt(System.console().readLine());

		System.out.print("podaj x");
		System.out.print("\n");
		x = Integer.parseInt(System.console().readLine());

		System.out.print("a*x**m + b*x**n + c - a");
		System.out.print("\n");
		System.out.print(a * Math.pow(x,m) + b * Math.pow(x,n) + c - a);
		System.out.print("\n");

		//Wyznacz wartosc funkcji y = sin3x*cos2x + e^x^2 + log(x^3+2x^2-x-3) w zadanym punkcie.

		System.out.print("podaj x");
		System.out.print("\n");

		x = Integer.parseInt(System.console().readLine());

		System.out.print("sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)");
		System.out.print("\n");
		System.out.print(Math.sin(3 * x) * Math.cos(2 * x) + Math.exp(Math.pow(x,2)) + Math.log(Math.pow(x,3) + 2 * Math.pow(x,2) - x - 3));
		System.out.print("\n");

	}

}
