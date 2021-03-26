public class Main {
	public static void main(String[] args) {

		//Dla pobranej liczby, wyswietl liczbe Pi podniesiona 
		//do potegi rownej pobranej liczbie. Wynik powinien byc
		//zaokraglony do dwoch miejsc po przecinku.

		System.out.print("Podaj liczbe: ");
		System.out.print("\n");
		int n;
		n = Integer.parseInt(System.console().readLine());

		float wynik = 1.00;
		for (int i = 0; i<n; i++) {
			wynik *= 3.14;
		}

		System.out.printf("%.2f", wynik);
		System.out.printf("\n");

	}

}
