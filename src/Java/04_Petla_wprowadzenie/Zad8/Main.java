public class Main {
	public static void main(String[] args) {

		//Na farmie mamy a glow i b nog, znajdz liczbe kur oraz owieczek.

		System.out.print("Podaj dwie liczby: ");
		System.out.print("\n");
		int glowy;
		int nogi;
		glowy = Integer.parseInt(System.console().readLine());
		nogi = Integer.parseInt(System.console().readLine());

		for (int i = 0; i<glowy; i++) {
			int owce = glowy - i;
			if (2 * i + 4 * owce == nogi) {
				System.out.print(i + " " + owce + "\n");
				break;
			}
		}

	}

}
