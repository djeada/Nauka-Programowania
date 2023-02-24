import java.util.*;

public class Main {
	//Policz z ilu slow sklada sie zdanie.
	//Znaki interpunkcyjne nie sa liczone jako slowa.

	//Zlozonosc Czasowa O(n)
	//Zlozonosc Pamieciowa O(1)
	public static int policzSlowaV1(String slowo) {

		boolean spacja = true;
		int licznik = 0;

		for (var znak: slowo.toCharArray()) {
			if (Character.isWhitespace(znak)) {
				spacja = true;
			} else if (Character.isLetter(znak) && spacja) {
				licznik++;
				spacja = false;
			}
		}

		return licznik;
	}

	public static void test1() {
		String napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
		int wynik = 9;

		assert policzSlowaV1(napis) == wynik;
	}

	public static void main(String[] args) {
		test1();
	}

}
