import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Otrzymujesz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc
		//udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu. 

		System.out.print("Podaj: stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego kredytu");
		System.out.print("\n");

		float stopa;
		int lata;
		int kredyt;
		
		Scanner s = new Scanner(System.in);
		
		stopa = Float.parseFloat(s.nextLine());
		lata = Integer.parseInt(s.nextLine());
		kredyt = Integer.parseInt(s.nextLine());

		float r = (float) (stopa / 12 * 0.01);
		int n = lata * 12;

		float rata = (float) (kredyt * r * Math.pow((1 + r), n) / (Math.pow((1 + r), n) - 1));
		float calkKosz = rata * n;

		System.out.printf("rata mieieczna to ");
		System.out.printf("%.2f", rata);
		System.out.printf("\n");
		System.out.printf("calkowity koszt to ");
		System.out.printf("%.2f", calkKosz);
		System.out.printf("\n");

	}
}
