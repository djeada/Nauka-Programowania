import java.io.*;

public class Main {
	//Otrzymujesz napis reprezentujacy sciezke folderu.
	//Usun wszystkie pliki o rozmiarach wiekszych niż 10kB
	//znajdujacych sie w folderze oraz podfolderach.

	public static long rozmiarPliku(final String sciezka) {
		File plik = new File(sciezka);
		return plik.length();
	}

	public static void usunPliki(final String sciezka) {
		File folder = new File(sciezka);

		for (File plik: folder.listFiles()) {

			if (rozmiarPliku(plik.getAbsolutePath()) > 10000) {

				if (!plik.delete()) {
					System.out.println("Usuniecie pliku nie powiodlo sie.");
				}
			}
		}

	}

	public static void main(String[] args) {

		final String sciezka = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder";
		usunPliki(sciezka);
	}
}
