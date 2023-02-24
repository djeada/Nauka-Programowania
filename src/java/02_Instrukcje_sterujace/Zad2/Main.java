import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla dwoch pobranych liczb, sprawdz czy pobrane liczby sa identyczne.

		System.out.print("podaj dwie liczby:\n");
		int a;
		int b;
		Scanner s = new Scanner(System.in);

		a = Integer.parseInt(s.nextLine());
		b = Integer.parseInt(s.nextLine());

		if (a == b) {
			System.out.print("liczby sa jednakowe\n");
		} else {
			System.out.print("liczby sa rozne\n");
		}
	}

}
