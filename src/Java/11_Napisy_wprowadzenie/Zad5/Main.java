import java.util.*;

public class Main {
	//Otrzymujesz napis oraz liczbe k.
	//a) wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
	public static void wypiszPoziomo(final String napis, int k) {

		for (int i = 0; i<napis.length(); i += k) {
			System.out.print(napis.charAt(i));
			System.out.print(", ");
		}

		System.out.print("\n");
	}

	//b) wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.
	public static void wypiszPionowo(final String napis, int k) {
		for (int i = 0; i<napis.length(); i += k) {
			System.out.print(napis.charAt(i));
			System.out.print("\n");
		}
	}

	public static void main(String[] args) {
		String napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
		int k = 3;
		wypiszPoziomo(napis, k);
		wypiszPionowo(napis, k);

	}
}
