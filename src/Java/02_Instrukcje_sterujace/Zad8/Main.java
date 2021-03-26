public class Main {
	public static void main(String[] args) {

		//Pobierz od uzytkownika trzy dlugosci bokow i sprawdz, 
		//czy mozna z nich zbudowac trojkat.

		System.out.print("podaj trzy liczby:");
		System.out.print("\n");

		int a;
		int b;
		int c;

		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());
		c = Integer.parseInt(System.console().readLine());

		if (a + b > c && b + c > a && a + c > b) {
			System.out.print("z podanych bokow mozna zbudowac trojkat");
			System.out.print("\n");
		} else {
			System.out.print("z podanych bokow nie mozna zbudowac trojkata");
			System.out.print("\n");
		}

	}

}
