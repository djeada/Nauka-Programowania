import java.util.*;



package <missing>;

public class GlobalMembers
{
	//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke pliku tekstowego.
	//Drugi wiersz tekstu. Dodaj wiersz na poczatku pliku.

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

	public static void zapiszNaPoczatku(final String sciezka, final String dane)
	{

		var trescPliku = wczytajPlik(sciezka);

		try
		{
			String wiersz;
			std::ofstream plik = new std::ofstream(sciezka);
			plik.exceptions(std::ifstream.eofbit | std::ifstream.failbit | std::ifstream.badbit);

			plik << dane;
			for (var wiersz : trescPliku)
			{
				plik << wiersz + "\n";
			}

			plik.close();
		}

		catch (RuntimeException e)
		{
			System.out.print("Error: ");
			System.out.print(e.getMessage());
			System.out.print("\n");
		}
	}

	public static void main(String[] args)
	{

		final String sciezka = "folder/test.txt";
		zapiszNaPoczatku(sciezka, "Hej \n");

	}

}