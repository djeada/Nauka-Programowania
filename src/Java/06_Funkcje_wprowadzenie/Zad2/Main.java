
public class Main
{
	//Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora 
	//dla otrzymanych dwoch liczb zwroci: 

	//a) ich sume
	public static int suma(int a, int b)
	{
		return a + b;
	}

	//b) roznice drugiej i pierwszej
	public static int roznica(int a, int b)
	{
		return b - a;
	}

	//c) ich iloczyn
	public static int iloczyn(int a, int b)
	{
		return a * b;
	}

	//d) reszte z dzielenia pierwszej przez druga
	public static int reszta(int a, int b)
	{
		return a % b;
	}

	public static void main(String[] args)
	{
		System.out.print("Podaj dwie liczby: ");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());
		int b;
		b = Integer.parseInt(System.console().readLine());

		System.out.print("suma liczb to: " + suma(a, b) + "\n");
		System.out.print("roznice drugiej i pierwszej to: " + roznica(a, b) + "\n");
		System.out.print("iloczyn liczb to: " + iloczyn(a, b) + "\n");
		System.out.print("reszte z dzielenia pierwszej przez druga to: " + reszta(a, b) + "\n");

	}
}
