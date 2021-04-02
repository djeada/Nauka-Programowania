//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to C++ namespace aliases:
//namespace filesys = std::experimental::filesystem;

package <missing>;

public class GlobalMembers
{
	//Otrzymujesz napis reprezentujacy sciezke folderu.
	//Usun wszystkie pliki o rozmiarach wiekszych niż 10kB
	//znajdujacych sie w folderze oraz podfolderach.

	public static int rozmiarPliku(final String sciezka)
	{
		return filesys.file_size(filesys.path(sciezka));
	}

	public static void usunPliki(final String sciezka)
	{

		for (var plik : filesys.directory_iterator(sciezka))
		{
			if (rozmiarPliku(plik.path()) > 10000)
			{
				filesys.remove(filesys.path(plik.path()));
			}
		}
	}

	public static void main(String[] args)
	{

		final String sciezka = "folder/";
		usunPliki(sciezka);

	}

}