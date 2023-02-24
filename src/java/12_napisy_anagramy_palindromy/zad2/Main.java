import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/*
Wszystkie permutacje.
*/

public class Main {

	public static Set<String> znajdzWszystkiePerumtacjeV1(String slowo) {

		return znajdzWszystkiePerumtacjeV1("", slowo);
	}

	private static Set<String> znajdzWszystkiePerumtacjeV1(String prefiks, String slowo) {

		Set<String> permutacje = new HashSet<>();

		int n = slowo.length();

		if (n == 0)
			permutacje.add(prefiks);

		else
			for (int i = 0; i<n; i++)
				permutacje.addAll(znajdzWszystkiePerumtacjeV1(prefiks + slowo.charAt(i), slowo.substring(i + 1, n) + slowo.substring(0, i)));

		return permutacje;
	}

	public static Stream<String> znajdzWszystkiePerumtacjeV2(String slowo) {

		return IntStream.range(0, slowo.length())
			.parallel()
			.boxed()
			.flatMap(i -> znajdzWszystkiePerumtacjeV2(slowo.substring(0, i) + slowo.substring(i + 1))
				.map(c -> slowo.charAt(i) + c)
			);
	}

	public static void main(String[] args) {

		String slowo = "Dora";
		Set<String> wynik = new HashSet<>(Arrays.asList("Droa", "Daor", "aDor", "aroD", "aDro", "aorD", "raDo", "roDa", "rDoa", "raoD", "aoDr", "arDo",
			"oraD", "oaDr", "orDa", "rDao", "oDar", "roaD", "oarD", "oDra", "Dora", "Daro", "Doar", "Drao"));

		assert znajdzWszystkiePerumtacjeV1(slowo).equals(wynik);
		assert znajdzWszystkiePerumtacjeV2(slowo).collect(Collectors.toSet()).equals(wynik);

	}

}
