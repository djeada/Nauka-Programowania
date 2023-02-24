import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, wyswietl liczbe dni miesiaca odpowiadajacemu danej liczbie.

		System.out.print("Podaj numer miesiaca:\n");

		Scanner s = new Scanner(System.in);
		int numer = Integer.parseInt(s.nextLine());

		switch (numer) {
			case 1:
				System.out.print("Styczen ma 31 dni\n");
				break;

			case 2:
				System.out.print("Luty ma 28 lub 29 dni\n");
				break;

			case 3:
				System.out.print("Marzec ma 31 dni\n");
				break;

			case 4:
				System.out.print("Kwiecien ma 30 dni\n");
				break;

			case 5:
				System.out.print("Maj ma 31 dni\n");
				break;

			case 6:
				System.out.print("Czerwiec ma 30 dni\n");
				break;

			case 7:
				System.out.print("Lipiec ma 31 dni\n");
				break;

			case 8:
				System.out.print("Sierpien ma 31 dni\n");
				break;

			case 9:
				System.out.print("Wrzesien ma 30 dni\n");
				break;

			case 10:
				System.out.print("Pazdziernik ma 31 dni\n");
				break;

			case 11:
				System.out.print("Listopad ma 30 dni\n");
				break;

			case 12:
				System.out.print("Grudzien ma 31 dni\n");
				break;

			default:
				System.out.print("Podano niepoprawny numer miesiaca\n");
		}
	}
}
