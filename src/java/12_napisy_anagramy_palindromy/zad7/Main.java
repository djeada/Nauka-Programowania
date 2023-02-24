import java.util.*;
import java.util.Map.Entry;

public class Main
{
	//Dla dwoch slow, ile minimalnie znakow musimy usunac
	//aby uzyskac anagramy. Zwroc -1 dla slow, o roznych
	//dlugosciach.

	public static HashMap<Character, Integer> histogram(final String slowo)
	{
		HashMap<Character, Integer> histo = new HashMap<Character, Integer>();
		
		for (var znak : slowo.toCharArray())
		{
			if (histo.containsKey(znak))
			histo.put(znak, histo.get(znak) + 1);
			else
				histo.put(znak, 1);

		}

		return new HashMap<Character, Integer>(histo);
	}

	public static int liczbaZnakowV1(final String slowoA, final String slowoB)
	{
		if (slowoA.length() != slowoB.length())
		{
			return -1;
		}

		HashMap<Character, Integer> histoSlowaA = histogram(slowoA);
		HashMap<Character, Integer> histoSlowaB = histogram(slowoB);
		int licznik = 0;
		
		for (Entry<Character, Integer> para : histoSlowaA.entrySet()) {
		    Character klucz = para.getKey();
		    int wartosc = para.getValue();
			if (!histoSlowaB.containsKey(klucz))
			{
				licznik++;
			}
			else
			{
				licznik += wartosc - histoSlowaB.get(klucz);
			}
		}

		for (Entry<Character, Integer> para : histoSlowaB.entrySet()) {
		    Character klucz = para.getKey();
		    int wartosc = para.getValue();
			if (!histoSlowaA.containsKey(klucz))
			{
				licznik++;
			}
			else
			{
				licznik += wartosc - histoSlowaA.get(klucz);
			}
		}

		return licznik;
	}

	public static void test1()
	{
		String slowoA = "grazyna";
		String slowoB = "razynax";
		int wynik = 2;
		assert liczbaZnakowV1(slowoA, slowoB) == wynik;
	}

	public static void test2()
	{
		String slowoA = "pan cytryna";
		String slowoB = "pan pomarancza";
		int wynik = -1;
		assert liczbaZnakowV1(slowoA, slowoB) == wynik;
	}

	public static void test3()
	{
		String slowoA = "20ejdy0978oa";
		String slowoB = "akv81w39j1ob";
		int wynik = 12;
		assert liczbaZnakowV1(slowoA, slowoB) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();
		test3();

	}

}
