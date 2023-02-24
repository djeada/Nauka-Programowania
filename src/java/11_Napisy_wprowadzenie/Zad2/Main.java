import java.util.*;

public class Main {
	//Dla otrzymanego napisu oraz znaku,
	//znajdz liczbe wystapien znaku w napisie.

	//Zlozonosc Czasowa O(n)
	//Zlozonosc Pamieciowa O(1)
	public static int policzZnakV1(final String slowo, final char znak) {

		int licznik = 0;

		for (char x: slowo.toCharArray()) {
			if (x == znak) {
				licznik++;
			}
		}

		return licznik;
	}

	public static void test1() {
		String napis = "adam";
		char znak = 'a';
		int wynik = 2;

		assert policzZnakV1(napis, znak) == wynik;
	}

	public static void main(String[] args) {
		test1();
	}

}
