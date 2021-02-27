
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.

		System.out.print("podaj trzy liczby:");
		System.out.print("\n");

		int a;
		int b;
		int c;

		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());
		c = Integer.parseInt(System.console().readLine());

		if (a >= b && a >= c)
		{
			if (b >= c)
			{
				System.out.print(c + "\n");
				System.out.print(b + "\n");
				System.out.print(a + "\n");
				System.out.print("\n");
			}
			else
			{
				System.out.print(b + "\n");
				System.out.print(c + "\n");
				System.out.print(a + "\n");
				System.out.print("\n");
			}
		}

		else if (c >= b && c >= a)
		{
			if (a >= b)
			{
				System.out.print(b + "\n");
				System.out.print(a + "\n");
				System.out.print(c + "\n");
				System.out.print("\n");
			}
			else
			{
				System.out.print(a + "\n");
				System.out.print(b + "\n");
				System.out.print(c + "\n");
				System.out.print("\n");
			}
		}
		else
		{
			if (a >= c)
			{
				System.out.print(c + "\n");
				System.out.print(a + "\n");
				System.out.print(b + "\n");
				System.out.print("\n");
			}
			else
			{
				System.out.print(a + "\n");
				System.out.print(c + "\n");
				System.out.print(b + "\n");
				System.out.print("\n");
			}
		}
	}


}