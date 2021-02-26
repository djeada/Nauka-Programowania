
public class Main
{
	public static void main(String[] args)
	{
		//Pobierz podstawe i wysokosc trojkata i wypisz pole. 

		System.out.print("podaj podstawe i wysokosc trojkata: \n");

		float a = Float.parseFloat(System.console().readLine());
		float h = Float.parseFloat(System.console().readLine());

		System.out.print("pole trojkata o podstawie " + a + " i wysokosci " + h + " jest rowne " + (a * h / 2) + "\n");

		//Pobierz dlogosci bokow prostokata i wypisz pole.

		System.out.print("podaj dlugosci bokow prostokata:");
		System.out.print("\n");

		a = Float.parseFloat(System.console().readLine());
		float b;
		b = Float.parseFloat(System.console().readLine());

		System.out.print("pole prostokata o bokach " + a + " i " + b + " jest rowne " + (a * b) + "\n");

	}

}