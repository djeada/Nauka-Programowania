import java.util.BitSet;

public class Main {
	//Czy liczba jest palindromem?

	public static final int liczbaBitow = 8;

	public static boolean czyPalindromV1(int liczba) {
		BitSet bity = BitSet.valueOf(new long[] {
			liczba
		});

		for (int i = 0; i<liczbaBitow / 2 - 1; i++) {
			int val1 = bity.get(i) ? 1 : 0;
			int val2 = bity.get(liczbaBitow - 1 - i) ? 1 : 0;

			if ((val1 ^ val2) != 0) {
				return false;
			}
		}

		return true;
	}

	public static void test1() {
		int liczba = 231;
		assert czyPalindromV1(liczba);
	}

	public static void test2() {
		int liczba = 17;
		assert!czyPalindromV1(liczba);
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
