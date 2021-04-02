package <missing>;

public class GlobalMembers
{
	//Otrzymujesz napis reprezentujący sciezke pliku tekstowego.
	//Wczytaj i wypisz tresc pliku.

	public static void wypiszPlik(final String sciezka)
	{
		try
		{
			String wiersz;
			std::ifstream plik = new std::ifstream(sciezka);
			plik.exceptions(std::ifstream.eofbit | std::ifstream.failbit | std::ifstream.badbit);

			while (plik != null)
			{
				getline(plik, wiersz);
				System.out.print(wiersz);
				System.out.print("\n");
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

		final String sciezka = "test.txt";
		wypiszPlik(sciezka);

	}

}