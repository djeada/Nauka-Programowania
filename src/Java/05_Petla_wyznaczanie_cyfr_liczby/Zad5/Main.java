import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, sprawdz czy jest palindromem.

		System.out.print("Podaj liczbe\n");
		Scanner s = new Scanner(System.in);
		int a = Integer.parseInt(s.nextLine());

		int odwrocona = 0;
		int pom = a;

		while (pom > 0) {
			int cyfra = pom % 10;
			odwrocona = (odwrocona * 10 + cyfra);
			pom /= 10;
		}

		if (odwrocona == a) {
			System.out.print("podana liczba jest palindromem\n");
		} else {
			System.out.print("podana liczba nie jest palindromem\n");
		}

	}

}
