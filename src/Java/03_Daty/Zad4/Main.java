public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, wypisz dzien tygodnia odpowiadajcy tej liczbie.

		System.out.print("Podaj numer dnia tygodnia:");
		System.out.print("\n");

		int dzien;
		dzien = Integer.parseInt(System.console().readLine());

		switch (dzien) {
			case 1:
				System.out.print("pierwszym dniem tygodnia jest poniedzialek");
				System.out.print("\n");
				break;

			case 2:
				System.out.print("drugim dniem tygodnia jest wtorek");
				System.out.print("\n");
				break;

			case 3:
				System.out.print("trzecim dniem tygodnia jest sroda");
				System.out.print("\n");
				break;

			case 4:
				System.out.print("czwartym dniem tygodnia jest czwartek");
				System.out.print("\n");
				break;

			case 5:
				System.out.print("piatym dniem tygodnia jest piatek");
				System.out.print("\n");
				break;

			case 6:
				System.out.print("szostym dniem tygodnia jest sobota");
				System.out.print("\n");
				break;

			case 7:
				System.out.print("siodmym dniem tygodnia jest niedziela");
				System.out.print("\n");
				break;

			default:
				System.out.print("podano niepoprawna liczbe");
				System.out.print("\n");
		}

	}

}
