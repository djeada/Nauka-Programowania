//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to C++ namespace aliases:
//namespace filesys = std::experimental::filesystem;

package <missing>;

public class GlobalMembers
{
	//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke pliku tekstowego.
	//Drugi wiersz tekstu. Dodaj wiersz na poczatku pliku.

	public static void skopiujPlik(final String sciezka, final String sciezkaDocelowa)
	{

		try
		{
			filesys.copy_file(sciezka, sciezkaDocelowa, filesys.copy_options.overwrite_existing);
		}
		catch (filesys.filesystem_error e)
		{
			System.out.print(e.what());
			System.out.print("\n");
		}
	}

	public static void zamienPliki(final String sciezkaA, final String sciezkaB)
	{

		String tempSciezka = sciezkaB;

		while (filesys.exists(tempSciezka))
		{
			tempSciezka = new String(filesys.path(tempSciezka).parent_path()) + filesys.path.preferred_separator + "x" + new String(filesys.path(tempSciezka).filename());
		}

		skopiujPlik(sciezkaA, tempSciezka);
		skopiujPlik(sciezkaB, sciezkaA);
		skopiujPlik(tempSciezka, sciezkaB);
		filesys.remove(tempSciezka);
	}

	public static void main(String[] args)
	{

		final String sciezkaA = "folder/test.txt";
		final String sciezkaB = "folder2/test2.txt";
		zamienPliki(sciezkaA, sciezkaB);

	}

}