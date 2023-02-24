import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, wypisz dzien tygodnia odpowiadajcy tej liczbie.

		System.out.print("Podaj numer dnia tygodnia:\n");

		Scanner s = new Scanner(System.in);
		int dzien = Integer.parseInt(s.nextLine());

		switch (dzien) {
			case 1:
				System.out.print("pierwszym dniem tygodnia jest poniedzialek\n");
				break;

			case 2:
				System.out.print("drugim dniem tygodnia jest wtorek\n");
				break;

			case 3:
				System.out.print("trzecim dniem tygodnia jest sroda\n");
				break;

			case 4:
				System.out.print("czwartym dniem tygodnia jest czwartek\n");
				break;

			case 5:
				System.out.print("piatym dniem tygodnia jest piatek\n");
				break;

			case 6:
				System.out.print("szostym dniem tygodnia jest sobota\n");
				break;

			case 7:
				System.out.print("siodmym dniem tygodnia jest niedziela\n");
				break;

			default:
				System.out.print("podano niepoprawna liczbe\n");
		}
	}
}
