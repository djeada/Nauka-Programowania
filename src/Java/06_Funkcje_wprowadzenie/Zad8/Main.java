public class Main {
	//Napisz funkcje realizujaca zaokraglanie ilorazu bez uzycia '/' i '%'.

	public static int podziel(int a, int b) {

		int znak = 1;
		int licznik = 0;

		if (b == 0) {
			return numeric_limits<Integer> .signaling_NaN();
		}

		if (a == 0) {
			return 0;
		}

		if (a<0) {
			znak = -1;
			a = -a;
		}

		if (b<0) {
			znak *= -1;
			b = -b;
		}

		if (znak == 1) {
			licznik = 0;
			while (a >= b) {
				a -= b;
				licznik += 1;
			}
		} else {
			licznik = 1;
			while (a > b) {
				a -= b;
				licznik += 1;
			}
		}

		return licznik * znak;
	}

	public static void main(String[] args) {
		System.out.print("Podaj dwie liczby: ");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());
		int b;
		b = Integer.parseInt(System.console().readLine());

		System.out.print("iloraz pierwszej przez druga to: ");
		System.out.print(podziel(a, b));
		System.out.print("\n");

	}

}
