/*
ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`
* ostatnia linia: `k`

### Wyjście

* Słownik po usunięciu par

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

*/
import java.util.*;

public class Main {

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

