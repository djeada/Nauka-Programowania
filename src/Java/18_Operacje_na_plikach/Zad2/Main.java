import java.util.*;

//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to C++ namespace aliases:
//namespace filesys = std::experimental::filesystem;

package <missing>;

public class GlobalMembers
{
	//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke folderu.
	//Drugi rozszerzenie plikow. Znajdz w folderze wszystkie pliki z
	//danym rozszerzeniem. Nazwy znalezionych plikow zapisz w liscie.

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
				pliki.add(filesys.path(plik.path()).filename());
			}
		}

		return new ArrayList<String>(pliki);
	}

	public static void test1()
	{
		String sciezka = "/home/adam/Documents";
		String rozszerzenie = ".txt";
		ArrayList<String> wynik = new ArrayList<String>(Arrays.asList("lista.txt", "test.txt"));
		assert plikiWFolderze(sciezka, rozszerzenie) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}