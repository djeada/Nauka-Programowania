import java.util.*;



package <missing>;

public class GlobalMembers
{
	//Otrzymujesz tekst w postaci napisu. Znajdz czestosc wystepowania kazdego ze slow w tekscie.
	//Zignoruj roznice miedzy malymi i wielkimi literami. Pamietaj, slowa skladaja sie wylacznie z liter!

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

	public static void naMale(String slowo)
	{
		transform(slowo.iterator(), slowo.end(), slowo.iterator(), tolower);
	}

	public static ArrayList<String> rozdzielSlowa(final String napis)
	{
		ArrayList<String> wynik = new ArrayList<String>();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1)
		{
			if (konc != pocz)
			{
				var slowo = napis.substring(pocz, konc);
				wyczysc(slowo);
				naMale(slowo);
				if (!slowo.empty())
				{
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz)
		{
			var slowo = napis.substring(pocz);
			wyczysc(slowo);
			naMale(slowo);
			if (!slowo.empty())
			{
				wynik.add(slowo);
			}
		}

		return new ArrayList<String>(wynik);
	}

	public static HashMap<Character, Integer> budujSlownik(final String slowo)
	{
		HashMap<Character, Integer> slownik = new HashMap<Character, Integer>();

		for (var znak : slowo)
		{
			slownik.get(znak)++;
		}

		return new HashMap<Character, Integer>(slownik);
	}

	public static ArrayList<ArrayList<String>> znajdzAnagramy(final String tekst)
	{

		var slowa = rozdzielSlowa(tekst);

		ArrayList<ArrayList<String>> wynik = new ArrayList<ArrayList<String>>();

		var it = slowa.iterator();

		while (it.hasNext())
		{
			var it2 = it;
			var slowo = it.next();
			var histogram = budujSlownik(slowo);

			ArrayList<String> anagramy = new ArrayList<String>(Arrays.asList(slowo));

//C++ TO JAVA CONVERTER TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
			it2++;
			while (it2.hasNext())
			{
				slowo = it2.next();

				if (histogram == budujSlownik(slowo))
				{
					if (find(anagramy.iterator(), anagramy.end(), slowo) == anagramy.end())
					{
						anagramy.add(slowo);
					}
//C++ TO JAVA CONVERTER TODO TASK: There is no direct equivalent to the STL vector 'erase' method in Java:
//C++ TO JAVA CONVERTER TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copyFrom' method should be created:
//ORIGINAL LINE: it2 = slowa.erase(it2);
					it2.copyFrom(slowa.erase(it2));
				}
				else
				{
				}
			}

			if (anagramy.size() > 1)
			{
				wynik.add(anagramy);
			}

//C++ TO JAVA CONVERTER TODO TASK: There is no direct equivalent to the STL vector 'erase' method in Java:
//C++ TO JAVA CONVERTER TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copyFrom' method should be created:
//ORIGINAL LINE: it = slowa.erase(it);
			it.copyFrom(slowa.erase(it));
		}

		return new ArrayList<ArrayList<String>>(wynik);
	}

	public static void test1()
	{
		String slowo = "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. " + "Burza nad galeria i alergia na narty to zadna zbrodnia, jak bandzior i jego arbuz.";

		ArrayList<ArrayList<String>> wynik = new ArrayList<ArrayList<String>>(Arrays.asList(new ArrayList<String>(Arrays.asList("absurd", "brudas")), new ArrayList<String>(Arrays.asList("tyran", "narty")), new ArrayList<String>(Arrays.asList("bandzior", "zbrodnia")), new ArrayList<String>(Arrays.asList("burza", "arbuz")), new ArrayList<String>(Arrays.asList("galeria", "alergia"))));

		var anagramy = znajdzAnagramy(slowo);
		assert equal(anagramy.iterator(), anagramy.end(), wynik.iterator());
	}

	public static void test2()
	{
		String slowo = "I love the way sometimes the letters of an anagram rearrange themselves in my " + "head with no effort, whereas sometimes I have to write them out in a circle to work it out.";

		ArrayList<ArrayList<String>> wynik = new ArrayList<ArrayList<String>>();

		var anagramy = znajdzAnagramy(slowo);
		assert equal(anagramy.iterator(), anagramy.end(), wynik.iterator());
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}