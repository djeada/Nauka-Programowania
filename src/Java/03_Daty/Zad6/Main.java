
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranych trzech liczb, sprawdz czy reprezentuja one poprawna date. 
		//Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.

		System.out.print("Podaj dzien, miesiac i rok: ");
		System.out.print("\n");

		int dzien;
		int miesiac;
		int rok;

		dzien = Integer.parseInt(System.console().readLine());
		miesiac = Integer.parseInt(System.console().readLine());
		rok = Integer.parseInt(System.console().readLine());

		if (rok >= 1)
		{
			if (miesiac == 1 || miesiac == 3 || miesiac == 5 || miesiac == 7 || miesiac == 8 || miesiac == 10 || miesiac == 12)
			{
				if (dzien >= 1 && dzien <= 31)
				{
					System.out.print("Podana data jest poprawna");
					System.out.print("\n");
				}
				else
				{
					System.out.print("Podano niepoprawna date");
					System.out.print("\n");
				}
			}

			else if (miesiac == 4 || miesiac == 6 || miesiac == 9 || miesiac == 11)
			{
				if (dzien >= 1 && dzien <= 30)
				{
					System.out.print("Podana data jest poprawna");
					System.out.print("\n");
				}
				else
				{
					System.out.print("Podano niepoprawna date");
					System.out.print("\n");
				}
			}

			else if (miesiac == 2)
			{
				if (rok % 4 == 0)
				{
							if (rok % 100 == 0)
							{
								if (rok % 400 == 0 && dzien >= 1 && dzien <= 29)
								{
									System.out.print("Podana data jest poprawna");
									System.out.print("\n");
								}
						else if (dzien >= 1 && dzien <= 28)
						{
							System.out.print("Podana data jest poprawna");
							System.out.print("\n");
						}
						else
						{
							System.out.print("Podano niepoprawna date");
							System.out.print("\n");
						}
							}
							 else if (dzien >= 1 && dzien <= 29)
							 {
								System.out.print("Podana data jest poprawna");
								System.out.print("\n");
							 }
					else
					{
						System.out.print("Podano niepoprawna date");
						System.out.print("\n");
					}
				}
					 else if (dzien >= 1 && dzien <= 28)
					 {
						System.out.print("Podana data jest poprawna");
						System.out.print("\n");
					 }
			}

			else
			{
				System.out.print("Podano niepoprawna date");
				System.out.print("\n");
			}
		}
		else
		{
			System.out.print("Podano niepoprawna date");
			System.out.print("\n");
		}

	}

}