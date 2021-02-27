
public class Main
{
	public static void main(String[] args)
	{

		//Czy osoba jest pelnoletnia?

		System.out.print("Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:");
		System.out.print("\n");

		int dzien;
		int miesiac;
		int rok;

		dzien = Integer.parseInt(System.console().readLine());
		miesiac = Integer.parseInt(System.console().readLine());
		rok = Integer.parseInt(System.console().readLine());

		System.out.print("Podaj trzy liczby reprezentujace dzisiejsza date:");
		System.out.print("\n");

		int dzienAktualny;
		int miesiacAktualny;
		int rokAktualny;

		dzienAktualny = Integer.parseInt(System.console().readLine());
		miesiacAktualny = Integer.parseInt(System.console().readLine());
		rokAktualny = Integer.parseInt(System.console().readLine());

		int roznicaLata = rokAktualny - rok;
		int roznicaMiesiace = miesiacAktualny - miesiac;
		int roznicaDni = dzienAktualny - dzien;

		if (roznicaLata > 18)
		{
			System.out.print("osoba jest pelnoletnia");
			System.out.print("\n");
		}

		else if (roznicaLata == 18)
		{

			if (roznicaMiesiace > 0)
			{
				System.out.print("osoba jest pelnoletnia");
				System.out.print("\n");
			}

			else if (roznicaMiesiace == 0)
			{

				if (roznicaDni >= 0)
				{
					System.out.print("osoba jest pelnoletnia");
					System.out.print("\n");
				}

				else
				{
					System.out.print("osoba nie jest pelnoletnia");
					System.out.print("\n");
				}
			}
			else
			{
				System.out.print("osoba nie jest pelnoletnia");
				System.out.print("\n");
			}
		}

		else
		{
			System.out.print("osoba nie jest pelnoletnia");
			System.out.print("\n");
		}

	}


}