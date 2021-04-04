public class Main {
	//Konwersja miedzy dowolnymi systemami liczbowymi.
	public static int naDec(String liczba, int podstawa) {
		int wartoscDec = 0;

		for (int i = liczba.length() - 1; i >= 0; i--) {

			if (liczba.charAt(i) >= 'A' && liczba.charAt(i)<'Z') {
				wartoscDec += (liczba.charAt(i) - 'A' + 10) * Math.pow(podstawa, (liczba.length() - 1 - i));
			} else {
				wartoscDec += (liczba.charAt(i) - '0') * Math.pow(podstawa, (liczba.length() - 1 - i));
			}
		}

		return wartoscDec;
	}

	public static String zmianaPodstawy(String liczba, int podstawa, int nowaPodstawa) {

		if (podstawa > (10 + 'Z' - 'A')) {
			return "";
		}

		int wartoscDec = naDec(liczba, podstawa);
		podstawa = nowaPodstawa;
		liczba = "";

		while (wartoscDec > 0) {
			int reszta = wartoscDec % podstawa;
			wartoscDec /= podstawa;

			char nowyZnak = (char)('0' + reszta);

			if (nowyZnak > '9') {
				nowyZnak = (char)('A' + (nowyZnak - '9') - 1);
			}

			liczba += nowyZnak;
		}

		return new StringBuilder(liczba).reverse().toString();
	}

	public static void test1() {
		String liczba = "4301";
		String wynik = "1003031";

		assert wynik.equals(zmianaPodstawy(liczba, 10, 4));
	}

	public static void main(String[] args) {

		test1();
	}

}
