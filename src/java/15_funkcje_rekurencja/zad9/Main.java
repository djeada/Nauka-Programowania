import java.util.*;

public class Main {

	public static boolean czyElfickieSlowoV1(String slowo, String elf) {
		return czyElfickieSlowoV1(slowo, elf, 0);
	}
	public static boolean czyElfickieSlowoV1(String slowo) {
		return czyElfickieSlowoV1(slowo, "elf", 0);
	}
	/*
	Napisz funkcje, ktora sprawdzi czy otrzymane slowo jest elfickie. 
	Elfickie slowo to takie, w ktorym co najmniej raz wystepuje kazda 
	z liter slowa elf.
	*/

	public static boolean czyElfickieSlowoV1(String slowo, String elf, int i) {

		if (i >= slowo.length()) {
			return false;
		}

		char litera = slowo.charAt(i);

		if (elf.indexOf(litera) != -1) {
			elf = elf.replace(Character.toString(litera), "");

			if (elf.isEmpty()) {
				return true;
			}
		}

		return czyElfickieSlowoV1(slowo, elf, i + 1);
	}

	public static void test1() {
		String slowo = "reflektor";
		boolean wynik = true;

		assert czyElfickieSlowoV1(slowo) == wynik;
	}

	public static void test2() {
		String slowo = "elzbieta";
		boolean wynik = false;

		assert czyElfickieSlowoV1(slowo) == wynik;
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
