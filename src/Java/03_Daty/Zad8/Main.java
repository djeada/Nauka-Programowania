
public class Main
{
	public static void main(String[] args)
	{

		/*Niech data bedzie dana w formacie DD/MM/CCYY :
		DD - dzien
		MM - miesiac
		CC - stulecie
		YY - rok 
	
		A = CC/4 - 2*CC - 1 
		B = 5*YY/4
		C = 26*(MM + 1)/10
	
		Dzien = (A + B + C + DD) mod 7
		*/

		System.out.print("Podaj dzien:");
		System.out.print("\n");
		int DD;
		DD = Integer.parseInt(System.console().readLine());

		System.out.print("Podaj miesiac:");
		System.out.print("\n");
		int MM;
		MM = Integer.parseInt(System.console().readLine());

		System.out.print("Podaj rok:");
		System.out.print("\n");
		int rok;
		rok = Integer.parseInt(System.console().readLine());

		int CC = rok / 100;
		int YY = rok % 100;

		int A = (CC / 4) - 2 * CC - 1;
		int B = 5 * YY / 4;
		int C = 26 * (MM + 1) / 10;

		int wynik = (A + B + C + DD) % 7;

		switch (wynik)
		{
			case 1:
				System.out.print("pierwszym dniem tygodnia jest poniedzialek");
				System.out.print("\n");
				break;

			case 2:
				System.out.print("drugim dniem tygodnia jest wtorek");
				System.out.print("\n");
				break;

			case 3:
				System.out.print("trzecim dniem tygodnia jest sroda");
				System.out.print("\n");
				break;

			case 4:
				System.out.print("czwartym dniem tygodnia jest czwartek");
				System.out.print("\n");
					 break;

			case 5:
				System.out.print("piatym dniem tygodnia jest piatek");
				System.out.print("\n");
				break;

			case 6:
				System.out.print("szostym dniem tygodnia jest sobota");
				System.out.print("\n");
				break;

			case 7:
				System.out.print("siodmym dniem tygodnia jest niedziela");
				System.out.print("\n");
				break;

			default:
				System.out.print("bledne dane");
				System.out.print("\n");

		}

	}


}