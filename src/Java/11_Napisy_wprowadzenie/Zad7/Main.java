public class GlobalMembers {
	//Otrzymujesz napis. Zamien wszystkie znaki napisu
	//na odpowiadajace im numery w tablicy ASCII. Podmien
	//otrzymany napis na uzyskane numery oddzielone przecinkami.

	public static void zamienV1(tangible.RefObject<String> napis) {

		if (napis.argValue.length() == 0) {
			return;
		}

		String wynik = "";

		for (int numer: napis.argValue) {
			wynik += String.valueOf(numer) + ", ";
		}

		napis.argValue = wynik.substring(0, wynik.length() - 2);
	}

	public static void test1() {
		String napis = "pacZka!";
		String wynik = "112, 97, 99, 90, 107, 97, 33";

		tangible.RefObject<String> tempRef_napis = new tangible.RefObject<String> (napis);
		zamienV1(tempRef_napis);
		napis = tempRef_napis.argValue;
		assert napis.equals(wynik);
	}

	public static void test2() {
		String napis = "";
		String wynik = "";

		tangible.RefObject<String> tempRef_napis = new tangible.RefObject<String> (napis);
		zamienV1(tempRef_napis);
		napis = tempRef_napis.argValue;
		assert napis.equals(wynik);
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}

public final class RefObject<T> {
	public T argValue;
	public RefObject(T refArg) {
		argValue = refArg;
	}
}