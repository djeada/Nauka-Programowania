public class Main {
	/*
	Liczby naturalne mniejsze rowne N.	
	*/

	public static String mniejszeLiczbyV1(int n) {

		if (n<0) {
			return "";
		}

		if (n == 0) {
			return String.valueOf(n);
		}

		return String.valueOf(n) + ", " + mniejszeLiczbyV1(n - 1);
	}

	public static void main(String[] args) {
		int n = 10;
		String wynik = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0";
		System.out.print(mniejszeLiczbyV1(n));
		System.out.print("\n");

	}

}
