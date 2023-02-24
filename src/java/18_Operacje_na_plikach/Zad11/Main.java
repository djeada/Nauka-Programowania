import java.io.*;
import java.nio.file.*;

public class Main {

	public static String rozszerzenie(String fileName) {
		char ch;
		int len;
		if (fileName == null ||
			(len = fileName.length()) == 0 ||
			(ch = fileName.charAt(len - 1)) == '/' || ch == '\\' ||
			ch == '.')
			return "";
		int dotInd = fileName.lastIndexOf('.'),
			sepInd = Math.max(fileName.lastIndexOf('/'), fileName.lastIndexOf('\\'));
		if (dotInd<= sepInd)
			return "";
		else
			return fileName.substring(dotInd + 1).toLowerCase();
	}

	public static String nazwaPliku(final String sciezka) {
		File plik = new File(sciezka);
		return plik.getName();
	}

	public static void skopiujPlik(final String sciezka, final String sciezkaDocelowa) {
		var zrodlo = (new File(sciezka)).toPath();
		var cel = (new File(sciezkaDocelowa)).toPath();

		System.out.println(zrodlo);
		System.out.println(cel);
		try {
			Files.copy(zrodlo, cel);

		} catch (IOException e) {
			System.out.println("Blad przy kopiowaniu.");
		}
	}

	public static void zamienPliki(final String sciezkaA, final String sciezkaB) {

		File tempPlik;
		try {
			tempPlik = File.createTempFile("temp", "." + rozszerzenie(sciezkaA));
			String tempSciezka = tempPlik.getAbsolutePath();
			tempPlik.delete();

			skopiujPlik(sciezkaA, tempSciezka);
			(new File(sciezkaA)).delete();

			skopiujPlik(sciezkaB, sciezkaA);
			(new File(sciezkaB)).delete();

			skopiujPlik(tempSciezka, sciezkaB);
			(new File(tempSciezka)).delete();

		} catch (IOException e) {
			System.out.println("Blad przy tworzeniu pliku tymczasowego.");

		}

	}

	public static void main(String[] args) {

		final String sciezkaA = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder/test.txt";
		final String sciezkaB = System.getProperty("user.dir") + System.getProperty("file.separator") + "folder2/test.txt";
		zamienPliki(sciezkaA, sciezkaB);

	}

}
