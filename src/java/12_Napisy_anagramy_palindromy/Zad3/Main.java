import java.util.Arrays;

/*
Czy napisy sa swoimi anagramami?
*/

public class Main {

	public static boolean czyAnagramyV1(String napisA, String napisB) {

		if (napisA.length() != napisB.length())
			return false;

		char[] tablicaA = napisA.replaceAll("\\s", "").toLowerCase().toCharArray();
		char[] tablicaB = napisB.replaceAll("\\s", "").toLowerCase().toCharArray();

		Arrays.sort(tablicaA);
		Arrays.sort(tablicaB);

		return Arrays.equals(tablicaA, tablicaB);
	}

	public static boolean czyAnagramyV2(String napisA, String napisB) {

		if (napisA.length() != napisB.length())
			return false;

		adamint[] licznik = new int[256];
		char[] tablicaA = napisA.replaceAll("\\s", "").toLowerCase().toCharArray();
		char[] tablicaB = napisB.replaceAll("\\s", "").toLowerCase().toCharArray();

		for (int i = 0; i<tablicaA.length; i++) {
			licznik[tablicaA[i]]++;
			licznik[tablicaB[i]]--;
		}

		for (int x: licznik)
			if (x != 0)
				return false;

		return true;
	}

	public static void main(String[] args) {

		String napisA = "adam";
		String napisB = "mada";

		assert czyAnagramyV1(napisA, napisB);
		assert czyAnagramyV2(napisA, napisB);

		napisA = "myszyszka";
		napisB = "szyszynka";

		assert!czyAnagramyV1(napisA, napisB);
		assert!czyAnagramyV2(napisA, napisB);

	}

}
