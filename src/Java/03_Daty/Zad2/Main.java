import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Czy osoba jest pelnoletnia?

		System.out.print("Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:\n");

		int dzien;
		int miesiac;
		int rok;
		
		Scanner s = new Scanner(System.in);

		dzien = Integer.parseInt(s.nextLine());
		miesiac = Integer.parseInt(s.nextLine());
		rok = Integer.parseInt(s.nextLine());

		System.out.print("Podaj trzy liczby reprezentujace dzisiejsza date:\n");

		int dzienAktualny;
		int miesiacAktualny;
		int rokAktualny;

		dzienAktualny = Integer.parseInt(s.nextLine());
		miesiacAktualny = Integer.parseInt(s.nextLine());
		rokAktualny = Integer.parseInt(s.nextLine());
		
		int roznicaLata = rokAktualny - rok;
		int roznicaMiesiace = miesiacAktualny - miesiac;
		int roznicaDni = dzienAktualny - dzien;

		if (roznicaLata > 18) {
			System.out.print("osoba jest pelnoletnia\n");
		} else if (roznicaLata == 18) {

			if (roznicaMiesiace > 0) {
				System.out.print("osoba jest pelnoletnia\n");
			} else if (roznicaMiesiace == 0) {

				if (roznicaDni >= 0) {
					System.out.print("osoba jest pelnoletnia\n");
				} else {
					System.out.print("osoba nie jest pelnoletnia\n");
				}
			} else {
				System.out.print("osoba nie jest pelnoletnia\n");
			}
		} else {
			System.out.print("osoba nie jest pelnoletnia\n");
		}
	}
}
