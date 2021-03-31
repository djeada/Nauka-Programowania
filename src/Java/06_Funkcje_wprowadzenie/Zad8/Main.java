import java.util.*;

public class Main {
	//Napisz funkcje realizujaca zaokraglanie ilorazu bez uzycia '/' i '%'.

	public static int podziel(int a, int b) {

		int znak = 1;
		int licznik = 0;

		if (b == 0) {
			return (int) Float.NaN;
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
		
		System.out.print("Podaj dwie liczby: \n");
		
		Scanner s = new Scanner(System.in);

		int a = Integer.parseInt(s.nextLine());
		int b = Integer.parseInt(s.nextLine());

		System.out.print("iloraz pierwszej przez druga to: " + podziel(a, b) + "\n");

	}
}
