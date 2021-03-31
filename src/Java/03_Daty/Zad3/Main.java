public class Main {
	public static void main(String[] args) {

		//Czy rok jest przestepny?

		System.out.print("Podaj rok:\n");

		Scanner s = new Scanner(System.in);
		int rok = Integer.parseInt(s.nextLine());

		if (rok % 4 == 0) {

			if (rok % 100 == 0) {
				if (rok % 400 == 0) {
					System.out.print("rok jest przestepny\n");
				} else {
					System.out.print("rok nie jest przestepny\n");
				}
			} else {
				System.out.print("rok jest przestepny\n");
			}
		} else {
			System.out.print("rok nie jest przestepny\n");
		}
	}
}
