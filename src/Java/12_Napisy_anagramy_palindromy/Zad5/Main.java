import java.util.*;

public class Main
{
	//Otrzymujesz napis reprezentujacy zdanie oraz slowo.
	//Znajdz wszystkie anagramy otrzymanego slowa w zdaniu.
	//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

	public static void naMale(String slowo)
	{
		transform(slowo.iterator(), slowo.end(), slowo.iterator(), tolower);
	}

	public static boolean anagram(String s1, String s2)
	{
	
		int N = s1.length();
		int M = s2.length();

		if (N != M)
		{
			return false;
		}

		int[] pom = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

		for (var znak : s1)
		{
			pom[znak]++;
		}

		for (var znak : s2)
		{
			pom[znak]--;
		}

		for (var x : pom)
		{
			if (x != 0)
			{
				return false;
			}
		}

		return true;
	}

	public static void wyczysc(String napis)
	{
		var it = napis.iterator();

		while (it != napis.end())
		{
			if (ispunct(*it))
			{
				napis = napis.substring(0, it);
			}
			else
			{
				it++;
			}
		}
	}

	public static ArrayList<String> anagramyV1(final String zdanie, final String napis)
	{
		ArrayList<String> wynik = new ArrayList<String>();
		int pocz = 0;
		int konc = 0;
		while ((konc = zdanie.indexOf(' ', pocz)) != -1)
		{
			if (konc != pocz)
			{
				var slowo = zdanie.substring(pocz, konc);
				wyczysc(slowo);
				naMale(slowo);
				if (!slowo.empty() && anagram(new auto(slowo), napis))
				{
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz)
		{
			var slowo = zdanie.substring(pocz);
			wyczysc(slowo);
			naMale(slowo);
			if (!slowo.empty() && anagram(new auto(slowo), napis))
			{
				wynik.add(slowo);
			}
		}

		return new ArrayList<String>(wynik);
	}

	public static void test1()
	{
		String zdanie = "Za jego nikczemne uczynki, spotakla go wysoce sroga kara.";
		String slowo = "arak";
		ArrayList<String> wynik = new ArrayList<String>(Arrays.asList("kara"));
		assert anagramyV1(zdanie, slowo) == wynik;
	}

	public static void main(String[] args)
	{
		test1();

	}

}