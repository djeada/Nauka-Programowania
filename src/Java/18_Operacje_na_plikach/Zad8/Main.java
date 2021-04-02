import java.util.*;

//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to C++ namespace aliases:
//namespace filesys = std::experimental::filesystem;

package <missing>;

public class GlobalMembers
{
	//Otrzymujesz napis reprezentujacy sciezkę folderu.
	//Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych
	//się w folderze oraz podfolderach.

	public static String znajdzRozszerzenie(String sciezka)
	{

		filesys.path obiekt = new filesys.path(sciezka);

		if (obiekt.has_extension())
		{
			return obiekt.extension().string();
		}

		return "";
	}

	public static ArrayList<String> plikiWFolderze(final String sciezka, final String rozszerzenie)
	{

		ArrayList<String> pliki = new ArrayList<String>();

		for (var plik : filesys.directory_iterator(sciezka))
		{
			if (rozszerzenie.equals(znajdzRozszerzenie(plik.path())))
			{
				pliki.add(filesys.path(plik.path()));
			}
		}

		return new ArrayList<String>(pliki);
	}

	public static void dodajInicjaly(final String sciezkaFolderu, final String dane)
	{

	var _dodajInicjaly = (String sciezka, String dane) ->
	{
		std::ofstream plik = new std::ofstream();
		plik.open(sciezka, std::ios.out | std::ios.app);
		if (plik.fail())
		{
			throw std::ios_base.failure(std::strerror(errno));
		}

		plik.exceptions(plik.exceptions() | std::ios.failbit | std::ifstream.badbit);
		plik << dane << std::endl;
		System.out.print(dane);
		System.out.print("\n");
	};

		var sciezki = plikiWFolderze(sciezkaFolderu, ".txt");

		for (var sciezka : sciezki)
		{
			_dodajInicjaly(sciezka, dane);
		}
	}

	//Usun srodkowy wiersz z kazdego pliku csv znajdujacego się w folderze
	//oraz podfolderach.
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

	public static void usunSrodkowy(final String sciezkaFolderu)
	{

	var _usunSrodkowy = (String sciezka) ->
	{
		var trescPliku = wczytajPlik(sciezka);

		try
		{
			String wiersz;
			std::ofstream plik = new std::ofstream(sciezka);
			plik.exceptions(std::ifstream.eofbit | std::ifstream.failbit | std::ifstream.badbit);

			trescPliku.remove(trescPliku.size() / 2);

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
	};

		var sciezki = plikiWFolderze(sciezkaFolderu, ".csv");

		for (var sciezka : sciezki)
		{
			_usunSrodkowy(sciezka);
		}
	}

	public static void main(String[] args)
	{

		String sciezka = new String(filesys.current_path()) + filesys.path.preferred_separator + "folder/";
		String dane = "A.D.";
		dodajInicjaly(sciezka, dane);
		usunSrodkowy(sciezka);

	}

}