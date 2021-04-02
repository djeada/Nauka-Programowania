import java.util.*;

public class Main
{
	//Wieza Hanoi.

	public static void hanoiWew(int n, char a, char b, char c, ArrayList<Pair<Character, Character>> wynik)
	{

		if (n == 1)
		{
			wynik.emplace_back(a, b);
			return;
		}

		hanoiWew(n - 1, a, c, b, wynik);
		wynik.emplace_back(a, b);
		hanoiWew(n - 1, c, b, a, wynik);
	}

	public static ArrayList<Pair<Character, Character>> hanoi(int n)
	{
		ArrayList<Pair<Character, Character>> wynik = new ArrayList<Pair<Character, Character>>();
		hanoiWew(n, 'A', 'B', 'C', wynik);
		return new ArrayList<Pair<Character, Character>>(wynik);
	}

	public static void test1()
	{
		int n = 3;
		ArrayList<Pair<Character, Character>> wynik = new ArrayList<Pair<Character, Character>>(Arrays.asList({'A', 'B'}, {'A', 'C'}, {'B', 'C'}, {'A', 'B'}, {'C', 'A'}, {'C', 'B'}, {'A', 'B'}));

		assert hanoi(n) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}