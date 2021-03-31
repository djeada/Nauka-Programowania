import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Dla pobranych czterech liczb, znajdz najwieksza liczbe. 

		System.out.print("podaj cztery liczby:");
		System.out.print("\n");

		int a;
		int b;
		int c;
		int d;

		Scanner s = new Scanner(System.in);

		a = Integer.parseInt(s.nextLine());
		b = Integer.parseInt(s.nextLine());
		c = Integer.parseInt(s.nextLine());
		d = Integer.parseInt(s.nextLine());
		
		int maksAB = a > b ? a : b;
		int maksCD = c > d ? c : d;
		int maks = maksAB > maksCD ? maksAB : maksCD;

		System.out.print(maks);
		System.out.print("\n");

	}

}
