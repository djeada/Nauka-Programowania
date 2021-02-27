
public class Main
{
	public static void main(String[] args)
	{


		//Prawo wylacznego srodka
		System.out.print("Prawo wylacznego srodka");
		System.out.print("\n");
		boolean p = false;
		System.out.print("dla p majacego wartosc logiczna ");
		System.out.print(p);
		System.out.print(" wyrazenie p v ~p ma wartosc logiczna ");
		System.out.printf("%b", (p || !p));
		System.out.printf("%b", "\n");
		p = true;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " wyrazenie p v ~p ma wartosc logiczna ");
		System.out.printf("%b", (p || !p));
		System.out.printf("%b", "\n");

		//Zasada niesprzecznosci
		System.out.printf("%b", "\nZasada niesprzecznosci");
		System.out.printf("%b", "\n");
		p = false;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ");
		System.out.printf("%b", !(p && !p));
		System.out.printf("%b", "\n");
		p = true;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ");
		System.out.printf("%b", !(p && !p));
		System.out.printf("%b", "\n");

		//Przemiennosc koniunkcji
		System.out.printf("%b", "\nPrzemiennosc koniunkcji");
		System.out.printf("%b", "\n");
		p = false;
		boolean q = false;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
		System.out.printf("%b", ((p && q) == (q && p)));
		System.out.printf("%b", "\n");
		p = true;
		q = false;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
		System.out.printf("%b", ((p && q) == (q && p)));
		System.out.printf("%b", "\n");
		p = false;
		q = true;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
		System.out.printf("%b", ((p && q) == (q && p)));
		System.out.printf("%b", "\n");
		p = true;
		q = true;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
		System.out.printf("%b", ((p && q) == (q && p)));
		System.out.printf("%b", "\n");

		//Przemiennosc alternatywy
		System.out.printf("%b", "\nPrzemiennosc alternatywy");
		System.out.printf("%b", "\n");
		p = false;
		q = false;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ");
		System.out.printf("%b", ((p || q) == (q || p)));
		System.out.printf("%b", "\n");
		p = true;
		q = false;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ");
		System.out.printf("%b", ((p || q) == (q || p)));
		System.out.printf("%b", "\n");
		p = false;
		q = true;
		System.out.printf("%b", "dla p majacego wartosc logiczna ");
		System.out.printf("%b", p);
		System.out.printf("%b", " oraz q majacego wartosc logiczna ");
		System.out.printf("%b", q);
		System.out.printf("%b", " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ");
		System.out.printf("%b", ((p || q) == (q || p)));
		System.out.printf("%b", "\n");
	}
}