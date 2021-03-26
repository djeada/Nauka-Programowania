public class GlobalMembers {
	//Otrzymujesz zdanie. Znajdz znaki znajdujace
	//sie na pozycjach bedacych liczbami pierwszymi.

	public static boolean czyPierwsza(int n) {

		if ((n % 2) == 0 && n != 2) {
			return false;
		}

		for (int i = 3; i<= Math.sqrt((double) n); i += 2) {
			if ((n % i) == 0) {
				return false;
			}
		}

		return true;
	}

	public static ArrayList<Character> znaki(final String napis) {

		ArrayList<Character> znaki = new ArrayList<Character> ();

		for (int i = 0; i<napis.length(); i++) {
			if (czyPierwsza(i)) {
				znaki.add(napis.charAt(i));
			}
		}

		return new ArrayList<Character> (znaki);
	}

	public static void test1() {
		String napis = "Kaczka lubi wiosne.";
		ArrayList<Character> wynik = new ArrayList<Character> (Arrays.asList('a', 'c', 'z', 'a', 'l', ' ', 'i', 'e'));
		assert znaki(napis) == wynik;
	}

	public static void main(String[] args) {
		test1();
	}

}