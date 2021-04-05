import java.util.*;
import java.io.*;
import java.nio.file.*;

public class Main
{
	//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke pliku tekstowego.
	//Drugi wiersz tekstu. Dodaj wiersz na poczatku pliku.

	public static ArrayList<String> wczytajPlik(final String sciezka)
	{

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

	public static void zapiszNaPoczatku(final String sciezka, final String dane)
	{

		var trescPliku = wczytajPlik(sciezka);
		var tekst = dane + Arrays.deepToString(trescPliku.toArray());
		
		try {
			Files.write( Paths.get(sciezka), tekst.getBytes());
		} catch (IOException e) {
			System.out.println("Blad zapisu do pliku.");
		}
	}

	public static void main(String[] args)
	{

		final String sciezka = "folder/test.txt";
		zapiszNaPoczatku(sciezka, "Hej \n");

	}

}
