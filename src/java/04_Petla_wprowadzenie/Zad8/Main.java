import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Na farmie mamy a glow i b nog, znajdz liczbe kur oraz owieczek.

		System.out.print("Podaj dwie liczby: \n");
		int glowy;
		int nogi;
		
		Scanner s = new Scanner(System.in);

		glowy = Integer.parseInt(s.nextLine());
		nogi = Integer.parseInt(s.nextLine());

		for (int i = 0; i<glowy; i++) {
			int owce = glowy - i;
			if (2 * i + 4 * owce == nogi) {
				System.out.print(i + " " + owce + "\n");
				break;
			}
		}

	}

}
