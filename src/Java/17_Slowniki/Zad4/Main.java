mport java.util.*;

public class Main {

	/*
	Usun ze slownika elementy o danej wartosci.
	*/

	public static void usunZeSlownikaV1(Map<String, Integer> slownik, int wartosc) {

		for (Iterator<Map.Entry<String, Integer>> it = slownik.entrySet().iterator(); it.hasNext();) {

			Map.Entry<String, Integer> entry = it.next();

			if (entry.getValue().equals(wartosc))
				it.remove();
		}
	}

	public static void test1() {
		Map<String, Integer> slownik = new HashMap<String, Integer> () {
			{
				put("aaa", 5);
				put("abc", 1);
				put("xxx", 5);
				put("cba", 3);
			}
		};

		Map<String, Integer> wynik = new HashMap<String, Integer> () {
			{
				put("abc", 1);
				put("cba", 3);
			}
		};

		int wartosc = 5;

		usunZeSlownikaV1(slownik, wartosc);

		assert slownik.equals(wynik);
	}

	public static void main(String[] args) {

		test1();
	}

}
