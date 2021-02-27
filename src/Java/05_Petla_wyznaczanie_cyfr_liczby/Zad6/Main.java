
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranej liczby n, wyswietl sume n 
		//pierwszych wyrazow ciagu danego wzorem:
		System.out.print("Podaj liczbe: ");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		//a) mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10

		System.out.print("mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: ");
		System.out.print("\n");
		for (int i = 0; i < a; i++)
		{
			int pom = i;
			int suma = 0;

			while (pom > 0)
			{
				suma += (pom % 10);
				pom /= 10;
			}

			if (suma == 10)
			{
				System.out.print(i);
				System.out.print("\n");
			}
		}

		//b) dwucyfrowe mniejsze od pobranej liczby

		System.out.print("dwucyfrowe mniejsze od pobranej liczby: ");
		System.out.print("\n");
		for (int i = 10; i < 100 && i < a; i++)
		{
			System.out.print(i);
			System.out.print("\n");
		}


		//c) trzycyfrowe ktorych suma cyfr jest	rowna pobranej liczbie
		System.out.print("trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie");
		System.out.print("\n");
		for (int i = 100; i < 1000; i++)
		{
			int pom = i;
			int suma = 0;

			while (pom > 0)
			{
				suma += (pom % 10);
				pom /= 10;
			}

			if (suma == a)
			{
				System.out.print(i);
				System.out.print("\n");
			}
		}

		//d) trzycyfrowe podzielne przez sume cyfr pobranej liczby
		System.out.print("trzycyfrowe podzielne przez sume cyfr pobranej liczby");
		System.out.print("\n");

		int pom = a;
		int suma = 0;

		while (pom > 0)
		{
			suma += (pom % 10);
			pom /= 10;
		}

		for (int i = 100; i < 1000; i++)
		{

			if (i % suma == 0)
			{
				System.out.print(i);
				System.out.print("\n");
			}
		}

		//e) mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr
		System.out.print("mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr");
		System.out.print("\n");

		for (int i = 0; i < a; i++)
		{
			int pom = i;
			boolean flaga = true;
			while (pom > 0)
			{
				int cyfra = pom % 10;
				if (cyfra % 2 == 1)
				{
					flaga = false;
					break;
				}
				pom /= 10;
			}

			if (flaga)
			{
				System.out.print(i);
				System.out.print("\n");
			}
		}

	}

}