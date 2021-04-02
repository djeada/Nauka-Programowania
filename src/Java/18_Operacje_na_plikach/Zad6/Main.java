import java.util.*;



package <missing>;

public class GlobalMembers
{
	//Otrzymujesz napis reprezentujacy scieżke pliku tekstowego. Oblicz:
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

	public static ArrayList<String> rozdzielSlowa(String napis)
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

	public static ArrayList<String> wczytajPlik(final String sciezka)
	{

		ArrayList<String> tresc = new ArrayList<String>();
		try
		{
			String wiersz;
			std::ifstream plik = new std::ifstream(sciezka);
			plik.exceptions(std::ifstream.eofbit | std::ifstream.failbit | std::ifstream.badbit);

			while (plik != null)
			{
				getline(plik, wiersz);
				tresc.add(wiersz);
			}

			plik.close();
		}

		catch (RuntimeException e)
		{
			System.out.print("Error : ");
			System.out.print(e.getMessage());
			System.out.print("\n");
		}

		return new ArrayList<String>(tresc);
	}

	//Liczbe wierszy pliku.
	public static int liczbaWierszy(ArrayList<String> trescPliku)
	{
		return trescPliku.size();
	}

	//Liczbe slow w pliku. Slowa oddzielone sa spacjami i nie moga skladac
	//sie wylacznie ze znakow nie bedacych literami.
	public static int liczbaSlow(ArrayList<String> trescPliku)
	{
		int wynik = 0;

		for (String wiersz : trescPliku)
		{
			wynik += rozdzielSlowa(wiersz).size();
		}

		return wynik;
	}

	//srednia dlugosc wiersza.
	public static double sredniaDlugoscWiersza(ArrayList<String> trescPliku)
	{

		int calkDlugosc = 0;

		for (String wiersz : trescPliku)
		{
			calkDlugosc += wiersz.length();
		}

		return calkDlugosc / (double)trescPliku.size();
	}

	//srednia liczbe slow na wiersz.
	public static double sredniaLiczbaSlow(ArrayList<String> trescPliku)
	{
		return liczbaSlow(trescPliku) / (double)liczbaWierszy(trescPliku);
	}

	//Czestosc wystepowania każdego ze slow w pliku.
	public static String wektorNaString(ArrayList<String> wektor)
	{
		String s;
		for (var piece : wektor)
		{
			s += piece;
		}
		return s;
	}

	public static HashMap<String, Integer> histogramSlow(String trescPliku)
	{
		HashMap<String, Integer> slownik = new HashMap<String, Integer>();

		ArrayList<String> slowa = rozdzielSlowa(trescPliku);

		for (var slowo : slowa)
		{
			slownik.get(slowo)++;
		}

		return new HashMap<String, Integer>(slownik);
	}

	public static void main(String[] args)
	{

		String sciezka = "folder/test.txt";
		var trescPliku = wczytajPlik(sciezka);

		System.out.print("Liczba wierszy: ");
		System.out.print(liczbaWierszy(trescPliku));
		System.out.print("\n");
		System.out.print("Liczba slow: ");
		System.out.print(liczbaSlow(trescPliku));
		System.out.print("\n");
		System.out.print("Srednia dlugosc wiersza: ");
		System.out.print(sredniaDlugoscWiersza(trescPliku));
		System.out.print("\n");
		System.out.print("Srednia liczba slow na wiersz: ");
		System.out.print(sredniaLiczbaSlow(trescPliku));
		System.out.print("\n");
		System.out.print("Histogram slow: ");
		System.out.print("\n");

		var tekst = wektorNaString(trescPliku);

		for (var it : histogramSlow(tekst))
		{
			System.out.print(it.first);
			System.out.print(" : ");
			System.out.print(it.second);
			System.out.print("\n");
		}

	}

}