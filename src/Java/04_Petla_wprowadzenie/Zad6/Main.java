
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranej liczby n, wyswietl sume n 
		//pierwszych wyrazow ciagu danego wzorem:
		System.out.print("Podaj liczbe: ");
		System.out.print("\n");
		int n;
		n = Integer.parseInt(System.console().readLine());


		//a_n = n/(n+1)
		float suma = 0F;
		for (float i = 1F; i <= n; i++)
		{
			float a = i / (i + 1);
			suma += a;
		}
		System.out.printf("%.2f", suma);
		System.out.printf("\n");

		//a_n = (n^2+5)/n
		suma = 0F;
		for (float i = 1F; i <= n; i++)
		{
			float a = (Math.pow(i, 2) + 5) / i;
			suma += a;
		}
		System.out.printf("%.2f", suma);
		System.out.printf("\n");

		//a_n = n + 2^n
		suma = 0F;
		for (int i = 1; i <= n; i++)
		{
			int a = i + Math.pow(2, i);
			suma += a;
		}

		System.out.printf("%.2f", suma);
		System.out.printf("\n");

	}

}
