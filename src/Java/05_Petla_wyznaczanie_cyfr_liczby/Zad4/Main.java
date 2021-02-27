
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranej liczby, powinny zostac zwrocone cyfry 
		//liczby spelniajce nastepujacy warunek:

		System.out.print("Podaj liczbe: ");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		//a) Liczby parzyste;

		int pom = a;
		System.out.print("Cyfry liczby badace liczbami parzystymi: ");
		System.out.print("\n");

		while (pom > 0)
		{
			int cyfra = pom % 10;

			if (cyfra % 2 == 0)
			{
				System.out.print(cyfra);
				System.out.print("\n");
			}

			pom /= 10;
		}

		//b) Mniejsze niz 5;

		pom = a;
		System.out.print("Cyfry liczby mniejsze niz 5: ");
		System.out.print("\n");

		while (pom > 0)
		{
			int cyfra = pom % 10;

			if (cyfra < 5)
			{
				System.out.print(cyfra);
				System.out.print("\n");
			}

			pom /= 10;
		}

		//c) Rozne od 0;

		pom = a;
		System.out.print("Cyfry liczby rozne od 0: ");
		System.out.print("\n");

		while (pom > 0)
		{
			int cyfra = pom % 10;

			if (cyfra != 0)
			{
				System.out.print(cyfra);
				System.out.print("\n");
			}

			pom /= 10;
		}

	}

}