import java.io.File;
import java.util.*;

public class Main {
	//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke folderu.
	//Drugi rozszerzenie plikow. Znajdz w folderze wszystkie pliki z
	//danym rozszerzeniem. Nazwy znalezionych plikow zapisz w liscie.

	public static ArrayList<String> plikiWFolderze(final String sciezka, final String rozszerzenie) {

		ArrayList<String> pliki = new ArrayList<String> ();

		File folder = new File(sciezka);
		for (File plik: folder.listFiles()) {
			var nazwa = plik.getName();
			if (nazwa.endsWith(rozszerzenie)) {
				pliki.add(nazwa);
			}
		}
		return pliki;
	}

	public static void test1() {
		String sciezka = "/home/adam/Documents";
		String rozszerzenie = ".txt";
		ArrayList<String> wynik = new ArrayList<String> (Arrays.asList("lista.txt", "test.txt"));
		assert wynik.equals(plikiWFolderze(sciezka, rozszerzenie));
	}

	public static void main(String[] args) {
		test1();
	}
}
