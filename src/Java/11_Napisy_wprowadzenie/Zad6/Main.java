public class Main {
	//Otrzymujesz napis. Zamien litery a na znaki zapytania.
	public static String zamienV1(String napis) {

		String wynik = "";
		
		for (var znak: napis.toCharArray()) {
			if (znak == 'a') {
				wynik += '?';
			}
			else {
				wynik += znak;
			}
		}
		
		return wynik;
	}

	public static String zamienV2(String napis) {
		return napis.replaceAll("a", "?");	
	}

	public static void test1() {
		String napis = "pacZka!";
		String wynik = "p?cZk?!";

		assert zamienV1(napis).equals(wynik);
	}

	public static void test2() {
		String napis = "pacZka!";
		String wynik = "p?cZk?!";

		assert zamienV2(napis).equals(wynik);
	}

	public static void main(String[] args) {
		test1();
		test2();
	}
}
