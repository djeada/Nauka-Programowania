import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, wyswietl liczbe Pi podniesiona 
		//do potegi rownej pobranej liczbie. Wynik powinien byc
		//zaokraglony do dwoch miejsc po przecinku.

		System.out.print("Podaj liczbe: \n");
		Scanner s = new Scanner(System.in);
		int n = Integer.parseInt(s.nextLine());

		float wynik = (float) 1.0;
		for (int i = 0; i<n; i++) {
			wynik *= 3.14;
		}

		System.out.printf("%.2f", wynik);
		System.out.printf("\n");

	}

}
