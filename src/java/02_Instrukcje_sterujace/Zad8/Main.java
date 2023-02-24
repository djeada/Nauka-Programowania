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
	
