import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, powinny zostac zwrocone cyfry 
		//liczby spelniajce nastepujacy warunek:
		
		System.out.print("Podaj liczbe\n");
		Scanner s = new Scanner(System.in);
		int a = Integer.parseInt(s.nextLine());

		//a) Liczby parzyste;

		int pom = a;
		System.out.print("Cyfry liczby badace liczbami parzystymi: \n");

		while (pom > 0) {
			int cyfra = pom % 10;

			if (cyfra % 2 == 0) {
				System.out.print(cyfra + "\n");
			}

			pom /= 10;
		}

		//b) Mniejsze niz 5;

		pom = a;
		System.out.print("Cyfry liczby mniejsze niz 5: \n");

		while (pom > 0) {
			int cyfra = pom % 10;

			if (cyfra<5) {
				System.out.print(cyfra + "\n");
			}

			pom /= 10;
		}

		//c) Rozne od 0;

		pom = a;
		System.out.print("Cyfry liczby rozne od 0: \n");

		while (pom > 0) {
			int cyfra = pom % 10;

			if (cyfra != 0) {
				System.out.print(cyfra + "\n");
			}

			pom /= 10;
		}

	}

}
