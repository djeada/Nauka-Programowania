import java.io.*;

public class Main {
	//Otrzymujesz dwa napisy reprezentujace sciezki folderow.
	//Przenies wszystkie pliki .csv z pierwszego folderu (oraz jego podfolderow) do drugiego folderu.

	public static String nazwaPliku(final String sciezka) {
		File plik = new File(sciezka);
		return plik.getName();
	}

	public static void przeniesPliki(final String sciezka, final String sciezkaDocelowa) {

		File folder = new File(sciezka);

		for (File plik: folder.listFiles()) {
			var nazwa = plik.getName();
			if (nazwa.endsWith(".csv")) {
				plik.renameTo(new File(sciezkaDocelowa + System.getProperty("file.separator") + ".csv"));
			}
		}

	}

	public static void main(String[] args) {

		final String sciezkaA = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder";
		final String sciezkaB = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder2";
		przeniesPliki(sciezkaA, sciezkaB);

	}

}
