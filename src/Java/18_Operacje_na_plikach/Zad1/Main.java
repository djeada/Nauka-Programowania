import java.io.File;

public class Main {
	//Otrzymujesz napis reprentujcy sciezke.
	//Sprawdz, czy sciezka należy do pliku czy folderu.

	public static boolean czyPlik(String sciezka) {
		File plik = new File(sciezka);
		return plik.exists() && plik.isFile();
	}

	public static boolean czyFolder(String sciezka) {
		File plik = new File(sciezka);
		return plik.exists() && plik.isDirectory();
	}

	public static void test1() {
		String sciezkaPliku = "/home/Nauka-programowania/Zad1.cpp";
		assert czyPlik(sciezkaPliku);
		assert!czyFolder(sciezkaPliku);
	}

	public static void test2() {
		String sciezkaFolderu = "/home/adam/Documents/Programming";

		assert!czyPlik(sciezkaFolderu);
		assert czyFolder(sciezkaFolderu);
	}

	public static void main(String[] args) {
		test1();
		test2();

	}
}
