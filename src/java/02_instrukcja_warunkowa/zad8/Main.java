/*
Tytul: Warunek trojkata.
Tresc: Dla trzech pobranych od uzytkownika dlugosci bokow sprawdz, czy mozna z nich zbudowac trojkat. Jednostki sa umowne.
Dane wejsciowe: Trzy liczby naturalne oznaczajace dlugosci bokow trojkata.
Dane wyjsciowe: Komunikat o mozliwosci lub niemozliwosci zbudowania trojkata.
Przyklad:
Dla pobranych liczb: 1, 2 oraz 3, powinna zostac wypisana informacja, ze nie mozna zbudowac trojkata z podanych bokow.

*/
import java.util.*;

public class Main {
	public static void main(String[] args) {

		//Pobierz od uzytkownika trzy dlugosci bokow i sprawdz, 
		//czy mozna z nich zbudowac trojkat.

		System.out.print("podaj trzy liczby:\n");

		int a;
		int b;
		int c;

		Scanner s = new Scanner(System.in);

		a = Integer.parseInt(s.nextLine());
		b = Integer.parseInt(s.nextLine());
		c = Integer.parseInt(s.nextLine());

		if (a + b > c && b + c > a && a + c > b) {
			System.out.print("z podanych bokow mozna zbudowac trojkat\n");
		} else {
			System.out.print("z podanych bokow nie mozna zbudowac trojkata\n");
		}
	

