import java.util.*;
import java.util.Map.Entry;
import java.io.*;

public class Main {
	//Otrzymujesz napis reprezentujacy scieżke pliku tekstowego. Oblicz:
	public static String wyczysc(String napis) {
		napis = napis.trim();
		return napis.replaceAll("\\p{Punct}", "");
	}

	public static ArrayList<String> rozdzielSlowa(String napis) {
		ArrayList<String> wynik = new ArrayList<String> ();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				slowo = wyczysc(slowo);
				slowo = slowo.toLowerCase();
				if (!slowo.isEmpty()) {
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			slowo = wyczysc(slowo);
			slowo = slowo.toLowerCase();
			if (!slowo.isEmpty()) {
				wynik.add(slowo);
			}
		}

		return new ArrayList<String> (wynik);
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
			System.out.println("Plik nie istnieje.");
		}

		return tresc;
	}

	//Liczbe wierszy pliku.
	public static int liczbaWierszy(ArrayList<String> trescPliku) {
		return trescPliku.size();
	}

	//Liczbe slow w pliku. Slowa oddzielone sa spacjami i nie moga skladac
	//sie wylacznie ze znakow nie bedacych literami.
	public static int liczbaSlow(ArrayList<String> trescPliku) {
		int wynik = 0;

		for (String wiersz: trescPliku) {
			wynik += rozdzielSlowa(wiersz).size();
		}

		return wynik;
	}

	//srednia dlugosc wiersza.
	public static double sredniaDlugoscWiersza(ArrayList<String> trescPliku) {

		int calkDlugosc = 0;

		for (String wiersz: trescPliku) {
			calkDlugosc += wiersz.length();
		}

		return calkDlugosc / (double) trescPliku.size();
	}

	//srednia liczbe slow na wiersz.
	public static double sredniaLiczbaSlow(ArrayList<String> trescPliku) {
		return liczbaSlow(trescPliku) / (double) liczbaWierszy(trescPliku);
	}

	//Czestosc wystepowania każdego ze slow w pliku.
	public static HashMap<String, Integer> histogramSlow(String trescPliku) {
		HashMap<String, Integer> slownik = new HashMap<String, Integer> ();

		ArrayList<String> slowa = rozdzielSlowa(trescPliku);

		for (var slowo: slowa) {
			if (slownik.containsKey(slowo))
				slownik.put(slowo, slownik.get(slowo) + 1);
			else
				slownik.put(slowo, 1);

		}

		return new HashMap<String, Integer> (slownik);
	}

	public static void main(String[] args) {

		String sciezka = "folder/test.txt";
		var trescPliku = wczytajPlik(sciezka);

		System.out.print("Liczba wierszy: ");
		System.out.println(liczbaWierszy(trescPliku));
		System.out.print("Liczba slow: ");
		System.out.println(liczbaSlow(trescPliku));
		System.out.print("Srednia dlugosc wiersza: ");
		System.out.println(sredniaDlugoscWiersza(trescPliku));
		System.out.print("Srednia liczba slow na wiersz: ");
		System.out.println(sredniaLiczbaSlow(trescPliku));
		System.out.println("Histogram slow: ");

		var tekst = Arrays.deepToString(trescPliku.toArray());

		for (Entry<String, Integer> para: histogramSlow(tekst).entrySet()) {
			System.out.println(para.getKey() + " : " + para.getValue());
		}
	}
}
