import java.util.*;
import java.io.*;
import java.nio.file.*;

public class Main {
	//Otrzymujesz napis reprezentujacy sciezkę folderu.
	//Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych
	//się w folderze oraz podfolderach.

	public static ArrayList<String> plikiWFolderze(final String sciezka, final String rozszerzenie) {

		ArrayList<String> pliki = new ArrayList<String> ();

		File folder = new File(sciezka);

		for (File plik: folder.listFiles()) {
			var nazwa = plik.getName();
			if (nazwa.endsWith(rozszerzenie)) {
				pliki.add(plik.getAbsolutePath());
			}
		}
		return pliki;
	}

	public static ArrayList<String> wczytajPlik(final String sciezka) {
		File plik = new File(sciezka);
		ArrayList<String> tresc = new ArrayList<String> ();

		if (plik.exists()) {
			try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(plik), "UTF-8"))) {
				String wiersz = null;
				while ((wiersz = br.readLine()) != null) {
					tresc.add(wiersz);

				}
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			System.out.println("Plik nie istnieje." + sciezka);
		}

		return tresc;
	}

	public static void dodajInicjaly(final String sciezkaFolderu, final String dane) {

		var sciezki = plikiWFolderze(sciezkaFolderu, ".txt");

		for (var sciezka: sciezki) {
			var trescPliku = wczytajPlik(sciezka);
			var tekst = Arrays.deepToString(trescPliku.toArray()) + dane;

			try {
				Files.write(Paths.get(sciezka), tekst.getBytes());
			} catch (IOException e) {
				System.out.println("Blad zapisu do pliku.");
			}
		}
	}

	//Usun srodkowy wiersz z kazdego pliku csv znajdujacego się w folderze
	//oraz podfolderach.

	public static void zapiszDoPilku(final String sciezka, final String dane) {
		try {
			Files.write(Paths.get(sciezka), dane.getBytes());
		} catch (IOException e) {
			System.out.println("Blad zapisu do pliku.");
		}
	}

	public static void usunSrodkowy(final String sciezkaFolderu) {

		var sciezki = plikiWFolderze(sciezkaFolderu, ".csv");

		for (var sciezka: sciezki) {

			File plik = new File(sciezka);
			ArrayList<String> tresc = new ArrayList<String> ();

			if (plik.exists()) {
				try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(plik), "UTF-8"))) {
					String wiersz = null;
					while ((wiersz = br.readLine()) != null) {
						tresc.add(wiersz);
					}

					if (tresc.size() / 2 - 1 > 0) {
						tresc.remove(tresc.size() / 2 - 1);
						zapiszDoPilku(sciezka, Arrays.deepToString(tresc.toArray()));
					}
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else {
				System.out.println("Plik nie istnieje." + sciezka);
			}

		}
	}

	public static void main(String[] args) {

		String sciezka = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder";
		String dane = "A.D.";
		dodajInicjaly(sciezka, dane);
		usunSrodkowy(sciezka);
	}
}
