import java.util.*;

public class Main
{
	//Dla otrzymanych dwoch list wypisz na przemian elemnty pierwszej
	//i drugiej listy. Jesli listy nie sa rownej dlugosci, po wyczerpaniu
	//elementow krotszej listy, wypisuj tylko elementy dluzszej listy.

	public static void wypisz(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{
		int n = listaA.size() < listaB.size() ? listaA.size() : listaB.size();

		for (int i = 0; i < n; i++)
		{
			System.out.print(listaA.get(i));
			System.out.print(", ");
			System.out.print(listaB.get(i));
			System.out.print(", ");
		}

		for (int i = n; i < listaA.size(); i++)
		{
			System.out.print(listaA.get(i));
			System.out.print(", ");
		}

		for (int i = n; i < listaB.size(); i++)
		{
			System.out.print(listaB.get(i));
			System.out.print(", ");
		}
	}

	public static void main(String[] args)
	{

		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(5, 3, 7, 2));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, -2, 3));

		wypisz(listaA, listaB);

	}

}
