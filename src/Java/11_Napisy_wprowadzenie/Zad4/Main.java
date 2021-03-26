public class GlobalMembers {
	//Otrzymujesz napis. Zamien wszystkie
	//male litery na wielkie.

	//Zlozonosc Czasowa O(n)
	//Zlozonosc Pamieciowa O(1)
	public static void naWielkieV1(String slowo) {

		for (var znak: slowo) {
			if (znak >= 97 && znak<= 122) {
				znak -= 32;
			}
		}
	}

	//Zlozonosc Czasowa O(n)
	//Zlozonosc Pamieciowa O(1)
	public static void naWielkieV2(String slowo) {

		for (var znak: slowo) {
			if (Character.isLowerCase(znak)) {
				znak = Character.toUpperCase(znak);
			}
		}
	}

	//Zlozonosc Czasowa O(n)
	//Zlozonosc Pamieciowa O(1)
	public static void naWielkieV3(String slowo) {
		transform(slowo.iterator(), slowo.end(), slowo.iterator(), toupper);
	}

	public static void test1() {
		String napis = "pacZka!";
		String wynik = "PACZKA!";

		naWielkieV1(napis);
		assert napis.equals(wynik);
	}

	public static void test2() {
		String napis = "pacZka!";
		String wynik = "PACZKA!";

		naWielkieV2(napis);
		assert napis.equals(wynik);
	}

	public static void test3() {
		String napis = "pacZka!";
		String wynik = "PACZKA!";

		naWielkieV3(napis);
		assert napis.equals(wynik);
	}

	public static void main(String[] args) {
		test1();
		test2();
		test3();
	}

}