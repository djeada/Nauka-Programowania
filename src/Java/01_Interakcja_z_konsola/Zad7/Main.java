import java.util.*;

public class Main {
	public static void main(String[] args) {
		//Pobierz podstawe i wysokosc trojkata i wypisz pole. 

		System.out.print("podaj podstawe i wysokosc trojkata: \n");

		Scanner s = new Scanner(System.in);

		float a = Float.parseFloat(s.nextLine());
		float h = Float.parseFloat(s.nextLine());


		System.out.print("pole trojkata o podstawie " + a + " i wysokosci " + h + " jest rowne " + (a * h / 2) + "\n");

		//Pobierz dlogosci bokow prostokata i wypisz pole.

		System.out.print("podaj dlugosci bokow prostokata:\n");

		a = Float.parseFloat(s.nextLine());

		float b = Float.parseFloat(s.nextLine());

		System.out.print("pole prostokata o bokach " + a + " i " + b + " jest rowne " + (a * b) + "\n");

	}

}
