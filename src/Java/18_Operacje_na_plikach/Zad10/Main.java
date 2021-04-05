import java.io.*;
import java.nio.file.*;

public class Main {
	//Otrzymujesz dwa napisy reprezentujace sciezki folderow.
	//Skopiuj wszystkie pliki .png z pierwszego folderu do drugiego.

	public static String nazwaPliku(final String sciezka) {
		File plik = new File(sciezka);
		return plik.getName();
	}

	public static void skopiujPlik(final String sciezka, final String sciezkaDocelowa) {
		var zrodlo = (new File(sciezka)).toPath();
		var cel = (new File(sciezkaDocelowa + System.getProperty("file.separator") + nazwaPliku(sciezka))).toPath();
		try {
			Files.copy(zrodlo, cel);
		} catch (IOException e) {
			System.out.println("Blad przy kopiowaniu.");
		}
	}

	public static void skopiujPliki(final String sciezka, final String sciezkaDocelowa) {
		File folder = new File(sciezka);

		for (File plik: folder.listFiles()) {
			var nazwa = plik.getName();
			if (nazwa.endsWith(".png")) {
				skopiujPlik(plik.getAbsolutePath(), sciezkaDocelowa);
			}
		}
	}

	public static void main(String[] args) {

		final String sciezka = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder";
		final String sciezkaDocelowa = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder2";
		skopiujPliki(sciezka, sciezkaDocelowa);

	}

}
