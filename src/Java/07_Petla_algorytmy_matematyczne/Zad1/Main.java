import java.util.*;

public class Main
{
	//Napisz funkcje, ktora dla otrzymanej liczby n,
	//poprosi uzytkownika o podanie n liczb i zwroci
	//ich srednia arytmetyczna

	public static float srednia(int n)
	{

		float suma = 0.0F;
		int x;

		for (int i = 0; i < n; i++)
		{
			System.out.print("Podaj liczbe: \n");
			Scanner s = new Scanner(System.in);
			x = Integer.parseInt(s.nextLine());
			suma += x;
		}

		return suma / n;
	}

	public static void main(String[] args)
	{
		System.out.print("Podaj liczbe: \n");
		Scanner s = new Scanner(System.in);
		int n = Integer.parseInt(s.nextLine());

		float wynik = srednia(n);

		System.out.print("Srednia z podanych liczb to " + wynik + "\n");

	}
}
