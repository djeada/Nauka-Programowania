public class Main {
	/*
	Wypisz wynik podstawowych operacji arytmetycznych 
	dla dwoch liczb pobranych od uzytkownika.
	*/

	public static void main(String[] args) {

		int x;
		int y;
		System.out.print("Podaj dwie liczby: \n");
		x = Integer.parseInt(System.console().readLine());
		y = Integer.parseInt(System.console().readLine());

		System.out.print("Suma " + x + " oraz " + y + " wynosi " + (x + y) + "\n");
		System.out.print("Roznica " + x + " i " + y + " wynosi " + (x - y) + "\n");
		System.out.print("Iloczyn " + x + " i " + y + " wynosi " + (x * y) + "\n");
		System.out.print("Iloraz " + x + " przez " + y + " wynosi " + (x / y) + "\n");
		System.out.print("Reszta z dzielenia " + x + " przez " + y + " wynosi " + (x % y) + "\n");
		System.out.print(" " + x + " podniesione do " + y + " wynosi " + Math.pow(x, y) + "\n");

	}
}
