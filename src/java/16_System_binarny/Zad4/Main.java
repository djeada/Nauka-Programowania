import java.util.*;

/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.

a) Oblicz z ilu zer sklada sie binarna reprezentacja otrzymanej liczby.
b) Oblicz z ilu jedynek sklada sie binarna reprezentacja otrzymanej liczby.
*/

public class Main {

	public static int zera(int n) {
		int licznik = 0;
		while (n > 0) {
			if (n % 2 == 0) {
				licznik++;
			}
			n /= 2;
		}
		return licznik;
	}

	public static int jedynki(int n) {
		int licznik = 0;
		while (n > 0) {
			if (n % 2 == 1) {
				licznik++;
			}
			n /= 2;
		}
		return licznik;
	}

	public static void test1() {
		int a = -2;
		int oczekiwane = 0;
		int wynik = zera(a);
		assert (wynik == oczekiwane);
	}

	public static void test2() {
		int a = 3;
		int oczekiwane = 2;
		int wynik = jedynki(a);
		assert (wynik == oczekiwane);
	}

	public static void test3() {
		int a = 3;
		int oczekiwane = 0;
		int wynik = zera(a);
		assert (wynik == oczekiwane);
	}

	public static void test4() {
		int a = 7;
		int oczekiwane = 3;
		int wynik = jedynki(a);
		assert (wynik == oczekiwane);
	}

	public static void main(String[] args) {
		test1();
		test2();
		test3();
		test4();
	}
}
