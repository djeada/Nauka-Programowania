import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranych dwoch liczb, powinny zostac wyswietlone:

		System.out.print("Podaj dwie liczby: \n");
		
		int a;
		int b;
		
		Scanner s = new Scanner(System.in);

		a = Integer.parseInt(s.nextLine());
		b = Integer.parseInt(s.nextLine());

		if (b<a) {
			int pom = a;
			a = b;
			b = pom;
		}

		//wszystkie liczby naturalne większe od mniejszej pobranej 
		//liczby i jednoczesnie mniejsze od wiekszej pobranej liczby.  
		for (int i = a + 1; i<b; i++) {
			System.out.print(i);
			System.out.print(" ");
		}

		System.out.print("\n");

		//wszystkie liczby naturalne podzielne przez 3 
		//wieksze od mniejszej pobranej liczby i jednoczesnie 
		//mniejsze od wiekszej pobranej liczby.
		for (int i = a + 1; i<b; i++) {
			if (i % 3 == 0) {
				System.out.print(i);
				System.out.print(" ");
			}
		}
	}
}
