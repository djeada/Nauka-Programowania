import java.util.*;
import java.io.*;

public class Main {
	//Otrzymujesz napis reprezentujacy sciezke pliku tekstowego.
	//Kazdy wiersz pliku reprezentuja adres ip. Posortuj adresy ip i zapisz je w liscie.

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

	public static void sortujAdresyIp(ArrayList<String> ip) {
		Collections.sort(ip, (a, b) -> {
			int[] aOct = Arrays.stream(a.split("\\.")).mapToInt(Integer::parseInt).toArray();
			int[] bOct = Arrays.stream(b.split("\\.")).mapToInt(Integer::parseInt).toArray();
			int r = 0;
			for (int i = 0; i<aOct.length && i<bOct.length; i++) {
				r = Integer.compare(aOct[i], bOct[i]);
				if (r != 0) {
					return r;
				}
			}
			return r;
		});
	}

	public static void main(String[] args) {

		final String sciezka = "/home/adam/Documents/Programming/Nauka-programowania/src/Java/18_Operacje_na_plikach/folder/adresy_ip.txt";
		var ip = wczytajPlik(sciezka);
		sortujAdresyIp(ip);
		System.out.println(Arrays.deepToString(ip.toArray()));

	}

}
