public class Main {
	/*
	Silnia.	
	*/

	public static int silniaV1(int n) {

		if (n == 0 || n == 1) {
			return 1;
		}

		return n * silniaV1(n - 1);
	}

	public static void test1() {
		int n = 3;
		int wynik = 6;

		assert silniaV1(n) == wynik;
	}

	public static void main(String[] args) {
		test1();

	}

}
