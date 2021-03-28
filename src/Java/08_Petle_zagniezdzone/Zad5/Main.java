public class Main {
	//Napisz funkcje, ktora dla otrzymanej liczby
	//wypisze litere X, o wysokosci rownej 
	//otrzymanej liczbie.

	public static void literaX(int n) {

		for (int y = 0; y<n; y++) {
			for (int x = 0; x<n; x++) {
				if (y == x || x == (n - 1 - y)) {
					System.out.print("*");
				} else {
					System.out.print(" ");
				}
			}
			System.out.print("\n");
		}
	}

	public static void main(String[] args) {

		int a = 5;
		literaX(a);

	}

}
