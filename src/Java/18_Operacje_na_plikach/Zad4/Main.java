import java.io.*;

public class Main {
	//Otrzymujesz napis reprezentujący sciezke pliku tekstowego.
	//Wczytaj i wypisz tresc pliku.

	public static void wypiszPlik(final String sciezka) {

		File plik = new File(sciezka);

		if (plik.exists()) {
			try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(plik), "UTF-8"))) {
				String line = null;
				while ((line = br.readLine()) != null) {
					System.out.println(line);
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			System.out.println("Plik nie istnieje.");
		}
	}

	public static void main(String[] args) {

		final String sciezka = "test.txt";
		wypiszPlik(sciezka);

	}

}
