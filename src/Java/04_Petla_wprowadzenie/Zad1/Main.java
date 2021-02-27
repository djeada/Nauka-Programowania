
public class Main
{
	public static void main(String[] args)
	{
		//Pros uzytkownika o podanie liczby, dopoki 
		//nie zostanie podana liczba 7.

		int a = 0;

		while (a != 7)
		{
			System.out.print("Podaj liczbe: ");
			System.out.print("\n");
			a = Integer.parseInt(System.console().readLine());
		}

	}

}