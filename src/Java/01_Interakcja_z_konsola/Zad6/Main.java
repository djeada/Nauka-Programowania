public class Main {
	public static void main(String[] args) {

		//Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

		System.out.print("podaj wielkosc w kilogramach:");
		System.out.print("\n");

		int kilogramy;
		kilogramy = Integer.parseInt(System.console().readLine());
		int gramy = kilogramy * 1000;

		System.out.print(kilogramy);
		System.out.print(" kg to ");
		System.out.print(gramy);
		System.out.print(" g.");
		System.out.print("\n");

		//Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

		System.out.print("podaj wielkosc w calach:");
		System.out.print("\n");

		float cal;
		cal = Float.parseFloat(System.console().readLine());
		float cm = cal / 2.54;

		System.out.print(cal);
		System.out.print(" cal to ");
		System.out.print(cm);
		System.out.print(" cm.");
		System.out.print("\n");

		//Pobierz ilosc sekund i przelicz na godziny.

		System.out.print("podaj ilosc sekund:");
		System.out.print("\n");

		float sekundy;
		sekundy = Float.parseFloat(System.console().readLine());
		float godziny = sekundy / 3600;

		System.out.print(sekundy);
		System.out.print(" sekund to ");
		System.out.print(godziny);
		System.out.print(" godzin");
		System.out.print("\n");

		//Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 

		System.out.print("podaj liczbe w euro:");
		System.out.print("\n");

		float euro;
		euro = Float.parseFloat(System.console().readLine());
		float zloty = euro * 4.40;

		System.out.print(euro);
		System.out.print(" euro to ");
		System.out.print(zloty);
		System.out.print(" zlotych");
		System.out.print("\n");

		//Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada. 

		System.out.print("podaj miare kata w stopniach:");
		System.out.print("\n");

		float katStopnie;
		katStopnie = Float.parseFloat(System.console().readLine());
		float katRad = katStopnie * 0.0174532;

		System.out.print(katStopnie);
		System.out.print(" stopni to ");
		System.out.print(katRad);
		System.out.print(" radianow.");
		System.out.print("\n");

		//Pobierz temperature w stopniach Farenheita i wypisz 
		//ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 

		System.out.print("podaj temperature w Farenheitach:");
		System.out.print("\n");

		float tempF;
		tempF = Float.parseFloat(System.console().readLine());
		float tempC = (tempF - 32) * 5 / 9;
		float tempK = tempC - 273;

		System.out.print(tempF);
		System.out.print(" F to ");
		System.out.print(tempC);
		System.out.print(" C i ");
		System.out.print(tempK);
		System.out.print(" K");
		System.out.print("\n");

	}

}
