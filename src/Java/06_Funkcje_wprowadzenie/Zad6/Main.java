public class Main {
	//Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

	public static int sumaCyfr(int a) {
		int suma = 0;

		while (a > 0) {
			suma += (a % 10);
			a /= 10;
		}

		return suma;
	}

	public static void main(String[] args) {
		System.out.print("Podaj liczbe: \n");
		
		Scanner s = new Scanner(System.in);

		int a = Integer.parseInt(s.nextLine());

		System.out.print("Suma cyfr liczby to: " + sumaCyfr(a) + "\n");

	}

}
