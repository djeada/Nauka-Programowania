/*
Odwroc wszystkie napisy w zdaniu.
Znaki powinny zostac zamienione miejscami dla kazdego napisu z osobna.
Napisy oddzielone sa spacjami, nie zmieniaj ich kolejnosci.
*/

import java.util.stream.Collectors;
import java.util.regex.Pattern;

public class Main {

	public static String odwrocNapisyV1(String napis) {

		String[] slowa = napis.split(" ");
		StringBuilder odwrocony = new StringBuilder();

		for (String word: slowa) {

			StringBuilder reverseWord = new StringBuilder();

			for (int i = word.length() - 1; i >= 0; i--) {
				reverseWord.append(word.charAt(i));
			}

			odwrocony.append(reverseWord).append(" ");
		}

		return odwrocony.toString().trim();
	}

	public static String odwrocNapisyV2(String napis) {
		return Pattern.compile(" +").splitAsStream(napis)
			.map(w -> new StringBuilder(w).reverse())
			.collect(Collectors.joining(" "));
	}

	public static void main(String[] args) {

		String napis = "Cameron Diaz";
		String wynik = "noremaC zaiD";
		
		assert odwrocNapisyV1(napis).equals(wynik);
		assert odwrocNapisyV2(napis).equals(wynik);

	}

}
