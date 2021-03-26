public class GlobalMembers {
	//Otrzymujesz napis reprezuntajacy zdanie.
	//Podziel zdanie na slowa skladowe.
	//Znaki interpunkcyjne nie sa liczone jako slowa.

	public static void wyczysc(String napis) {
		var it = napis.iterator();

		while (it != napis.end()) {
			if (ispunct( * it)) {
				napis = napis.substring(0, it);
			} else {
				it++;
			}
		}
	}

	public static void slowaV1(String napis) {
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				wyczysc(slowo);
				if (!slowo.empty()) {
					System.out.print(slowo);
					System.out.print("\n");
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			wyczysc(slowo);
			if (!slowo.empty()) {
				System.out.print(slowo);
				System.out.print("\n");
			}
		}
	}

	public static void main(String[] args) {
		String napis = "We think in generalities, but we live in details";
		slowaV1(napis);
	}

}