public class GlobalMembers {
	//Otrzymujesz napis. Zamien litery a na znaki zapytania.
	public static void zamienV1(String napis) {

		for (var znak: napis) {
			if (znak == 'a') {
				znak = '?';
			}
		}
	}

	public static void zamienV2(String napis) {
		replace(napis.iterator(), napis.end(), 'a', '?');
	}

	public static void test1() {
		String napis = "pacZka!";
		String wynik = "p?cZk?!";

		zamienV1(napis);
		assert napis.equals(wynik);
	}

	public static void test2() {
		String napis = "pacZka!";
		String wynik = "p?cZk?!";

		zamienV2(napis);
		assert napis.equals(wynik);
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}