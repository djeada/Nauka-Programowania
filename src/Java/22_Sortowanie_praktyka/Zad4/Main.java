import java.util.Arrays;
import java.util.Comparator;

/*
Posortuj tablice napisow wzgledem dlugosci.
*/

public class Main {

	public static void sortujWzgledemDlugosciV1(String[] napisy) {

		Arrays.sort(napisy, (String s1, String s2) -
			> (-1) * Integer.compare(s1.length(), s2.length()));
	}

	public static void sortujWzgledemDlugosciV2(String[] napisy) {

		Arrays.sort(napisy, Comparator.comparingInt(String::length).reversed());

	}

	public static String[] sortujWzgledemDlugosciV3(String[] napisy) {

		return Arrays.stream(napisy)
			.sorted(Comparator.comparingInt(String::length).reversed())
			.toArray(String[]::new);
	}

	public static void main(String[] args) {

		String[] napisy = new String[] {
			"Lezy", "jerzy", "na", "wiezyczce"
		};
		String[] wynik = new String[] {
			"wiezyczce", "jerzy", "Lezy", "na"
		};

		sortujWzgledemDlugosciV1(napisy);
		assert Arrays.equals(napisy, wynik);

		napisy = new String[] {
			"Lezy", "jerzy", "na", "wiezyczce"
		};
		sortujWzgledemDlugosciV2(napisy);
		assert Arrays.equals(napisy, wynik);

		napisy = new String[] {
			"Lezy", "jerzy", "na", "wiezyczce"
		};
		assert Arrays.equals(sortujWzgledemDlugosciV3(napisy), wynik);
	}

}
