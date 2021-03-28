public class Main {
	public static bool czyPierwsza(int n) {

		if ((n % 2) == 0 && n != 2) {
			return false;
		}

		for (int i = 3; i<= Math.sqrt((double) n); i += 2) {
			if ((n % i) == 0) {
				return false;
			}
		}

		return true;
	}

	public static void liczbyPierwszeV1(int n) {
		for (int i = 2; i<= n; i++) {
			if (czyPierwsza(i) != 0) {
				System.out.print(i);
				System.out.print(" ");
			}
		}
	}

	public static void sitoEratostenesa(int[] pierwsze, int liczba) {
		for (int p = 2; p<= liczba; p++) {
			if (pierwsze[p] == -1) {
				continue;
			}

			int n = 2;

			for (int i = p * n; i<= liczba; n++, i = p * n) {
				pierwsze[i] = -1;
			}
		}
	}

	public static void liczbyPierwszeV2(int liczba) {

		int[] pierwsze = new int[liczba + 1];

		sitoEratostenesa(pierwsze, liczba);

		for (int i = 2; i<= liczba; i++) {
			if (pierwsze[i] == 0) {
				System.out.print(i);
				System.out.print(" ");
			}
		}
	}

	public static void main(String[] args) {

		int a = 15;

		liczbyPierwszeV1(a);

		System.out.print("\n");
		liczbyPierwszeV2(a);

	}

}
