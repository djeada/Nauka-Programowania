//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to C++ namespace aliases:
//namespace filesys = std::experimental::filesystem;

package <missing>;

public class GlobalMembers
{
	//Otrzymujesz dwa napisy reprezentujace sciezki folderow.
	//Przenies wszystkie pliki .csv z pierwszego folderu (oraz jego podfolderow) do drugiego folderu.

	public static String nazwaPliku(final String sciezka)
	{
		return filesys.path(sciezka).filename();
	}

	public static void przeniesPlik(final String sciezka, final String sciezkaDocelowa)
	{

		try
		{
			filesys.copy_file(sciezka, sciezkaDocelowa + filesys.path.preferred_separator + nazwaPliku(sciezka), filesys.copy_options.overwrite_existing);
			filesys.remove(sciezka);
		}
		catch (filesys.filesystem_error e)
		{
			System.out.print(e.what());
			System.out.print("\n");
		}
	}

	public static String znajdzRozszerzenie(String sciezka)
	{

		filesys.path obiekt = new filesys.path(sciezka);

		if (obiekt.has_extension())
		{
			return obiekt.extension().string();
		}

		return "";
	}

	public static void przeniesPliki(final String sciezka, final String sciezkaDocelowa)
	{

		for (var plik : filesys.directory_iterator(sciezka))
		{
			if (znajdzRozszerzenie(plik.path()).equals(".csv"))
			{
				przeniesPlik(plik.path(), sciezkaDocelowa);
			}
		}
	}

	public static void main(String[] args)
	{

		final String sciezkaA = "folder/";
		final String sciezkaB = "folder2/";
		przeniesPliki(sciezkaA, sciezkaB);

	}

}