import java.util.*;

public class Main {
	public static void main(String[] args) {
		//Dla pobranej od uzytkownika liczby, 
		//zwroc liczbe cyfr pobranje liczby.

		System.out.print("Podaj liczbe\n");

		Scanner s = new Scanner(System.in);
		int a = Integer.parseInt(s.nextLine());

		int licznik = 0;

		while (a > 0) {
			a = a / 10;
			licznik++;
		}

		System.out.print("Podana liczba sklada sie z " + licznik + " cyfr.\n");

	}

}
