
public class Main
{
	//Napisz funkcje, ktora dla otrzymanej liczby 
	//wypisze zaczyajac od podstawy trojkat prostokatny 
	//rownoboczny o wysokosci rownej otrzymanej liczbie.

	public static void trojkat(int a)
	{

		for (int y = 0; y < a; y++)
		{
			for (int x = 0; x < a - y; x++)
			{
				System.out.print("x");
			}
			System.out.print("\n");
		}
	}

	public static void main(String[] args)
	{

		int a = 5;
		trojkat(a);

	}



}