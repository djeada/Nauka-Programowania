import java.util.*;

public class Main {
	public static void main(String[] args) {

		/*
		Otrzymujesz cene oraz wymiary pojedynczej plytki. Oblicz ile bedzie wynosila cena
		za podloge o podanych wymiarach. Podloga jest prostokatem, a plytka kwadratem
		*/

		System.out.print("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi");
		System.out.print("\n");

		int cena;
		int bokPlytki;
		int szerokoscPodlogi;
		int dlugoscPodlogi;

		Scanner s = new Scanner(System.in);
		cena = Integer.parseInt(s.nextLine());
		bokPlytki = Integer.parseInt(s.nextLine());
		szerokoscPodlogi = Integer.parseInt(s.nextLine());
		dlugoscPodlogi = Integer.parseInt(s.nextLine());

		int szerokoscKonieczna = szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki;
		int dlugoscKonieczna = dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki;

		int polePlytki = (int) Math.pow(bokPlytki, 2);
		int polePodlogi = szerokoscKonieczna * dlugoscKonieczna;

		float calkowityKoszt = cena * (float) polePodlogi / polePlytki;

		System.out.print("Dla plytki o dlugosci boku " + bokPlytki + " i ceny " + cena);
		System.out.print(" calkowity koszt wylozenia podlogi o wymiarach " + szerokoscPodlogi);
		System.out.print("x" + dlugoscPodlogi + " wynosi " + calkowityKoszt + "\n");

	}

}
