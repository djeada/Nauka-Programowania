import java.util.*;

public class Main {
	public static void main(String[] args) {
		//Pros uzytkownika o podanie liczby, dopoki 
		//nie zostanie podana liczba 7.

		int a = 0;
		Scanner s = new Scanner(System.in);
		
		while (a != 7) {
			System.out.print("Podaj liczbe: \n");
			a = Integer.parseInt(s.nextLine());
		}
	}
}
