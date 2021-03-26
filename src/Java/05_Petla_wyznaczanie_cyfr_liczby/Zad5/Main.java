public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, sprawdz czy jest palindromem.

		System.out.print("Podaj liczbe");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		int odwrocona = 0;
		int pom = a;

		while (pom > 0) {
			int cyfra = pom % 10;
			odwrocona = (odwrocona * 10 + cyfra);
			pom /= 10;
		}

		if (odwrocona == a) {
			System.out.print("podana liczba jest palindromem");
			System.out.print("\n");
		} else {
			System.out.print("podana liczba nie jest palindromem");
			System.out.print("\n");
		}

	}

}
