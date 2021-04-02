//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to C++ namespace aliases:
//namespace filesys = std::experimental::filesystem;

package <missing>;

public class GlobalMembers
{
	//Otrzymujesz napis reprentujcy sciezke.
	//Sprawdz, czy sciezka należy do pliku czy folderu.

	public static boolean czyPlik(String sciezka)
	{
		try
		{
			filesys.path obiekt = new filesys.path(sciezka);
			if (filesys.exists(obiekt) && filesys.is_regular_file(obiekt))
			{
				return true;
			}
		}

		catch (filesys.filesystem_error e)
		{
			std::cerr << e.what() << std::endl;
		}

		return false;
	}

	public static boolean czyFolder(String sciezka)
	{
		try
		{
			filesys.path obiekt = new filesys.path(sciezka);
			if (filesys.exists(obiekt) && filesys.is_directory(obiekt))
			{
				return true;
			}
		}

		catch (filesys.filesystem_error e)
		{
			std::cerr << e.what() << std::endl;
		}

		return false;
	}

	public static void test1()
	{
		String sciezkaPliku = "/home/Nauka-programowania/Zad1.cpp";
		assert czyPlik(sciezkaPliku);
		assert!czyFolder(sciezkaPliku);
	}

	public static void test2()
	{
		String sciezkaFolderu = "/home/adam/Documents/Programming";

		assert!czyPlik(sciezkaFolderu);
		assert czyFolder(sciezkaFolderu);
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

	//Compiling with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe

}