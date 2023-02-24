import java.util.*;

public class Main {
	/*
	Usun duplikaty.
	*/

	public static List<Integer> usunDuplikatyV1(List<Integer> lista) {

		List<Integer> wynik = new ArrayList<Integer> ();

		for (int x: lista)
			if (!wynik.contains(x))
				wynik.add(x);

		return wynik;
	}

	public static List<Integer> usunDuplikatyV2(List<Integer> lista) {

		List<Integer> wynik = new ArrayList<Integer> ();
		Set<Integer> zbior = new HashSet<>();

		for (int x: lista)
			if (zbior.add(x))
				wynik.add(x);

		return wynik;
	}

	public static void main(String[] args) {

		List<Integer> lista = new ArrayList<>(Arrays.asList(2, 1, 2, 2, 3, 3));
		List<Integer> wynik = new ArrayList<>(Arrays.asList(2, 1, 3));

		assert usunDuplikatyV1(lista).equals(wynik);
		assert usunDuplikatyV2(lista).equals(wynik);

	}

}
