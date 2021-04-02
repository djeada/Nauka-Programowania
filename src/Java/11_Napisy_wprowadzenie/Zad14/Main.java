public class Main {
	//Otrzymujesz liczbę n. Zwroc napis skladajacy
	//sie z liczb naturalnych od 1 do n.

	public static String liczby(int n) {
		String wynik = "";

		for (int i = 1; i<= n; i++) {
			wynik += String.valueOf(i);
		}

		return wynik;
	}

	public static void test1() {
		int n = 5;
		String wynik = "12345";
		assert wynik.equals(liczby(n));
	}

	public static void test2() {
		int n = -1;
		String wynik = "";
		assert wynik.equals(liczby(n));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}
