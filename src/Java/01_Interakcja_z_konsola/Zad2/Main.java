
public class Main
{
	public static void main(String[] args)
	{

		/*
		Wypisz na konsole najpierw druga potem pierwsza pobrana dana.
		*/

		int a;
		int b;

		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());

		System.out.print(b);
		System.out.print("\n");
		System.out.print(a);
		System.out.print("\n");

	}

}