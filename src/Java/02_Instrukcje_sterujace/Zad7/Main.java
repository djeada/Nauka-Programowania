package test;
public class Main {
    public static void main(String[] args) {

        //Prawo wylacznego srodka
        System.out.print("Prawo wylacznego srodka");
        System.out.print(System.getProperty("line.separator"));
        boolean p = false;
        System.out.print("dla p majacego wartosc logiczna ");
        System.out.print(p);
        System.out.print(" wyrazenie p v ~p ma wartosc logiczna ");
        System.out.printf("%b", (p || !p));
        System.out.printf(System.getProperty("line.separator"));
        p = true;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" wyrazenie p v ~p ma wartosc logiczna ");
        System.out.printf("%b", (p || !p));
        System.out.printf(System.getProperty("line.separator"));

        //Zasada niesprzecznosci
        System.out.printf("\nZasada niesprzecznosci");
        System.out.printf(System.getProperty("line.separator"));
        p = false;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ");
        System.out.printf("%b", !(p && !p));
        System.out.printf(System.getProperty("line.separator"));
        p = true;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ");
        System.out.printf("%b", !(p && !p));
        System.out.printf(System.getProperty("line.separator"));

        //Przemiennosc koniunkcji
        System.out.printf("\nPrzemiennosc koniunkcji");
        System.out.printf(System.getProperty("line.separator"));
        p = false;
        boolean q = false;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
        System.out.printf("%b", ((p && q) == (q && p)));
        System.out.printf(System.getProperty("line.separator"));
        p = true;
        q = false;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
        System.out.printf("%b", ((p && q) == (q && p)));
        System.out.printf(System.getProperty("line.separator"));
        p = false;
        q = true;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
        System.out.printf("%b", ((p && q) == (q && p)));
        System.out.printf(System.getProperty("line.separator"));
        p = true;
        q = true;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ");
        System.out.printf("%b", ((p && q) == (q && p)));
        System.out.printf(System.getProperty("line.separator"));

        //Przemiennosc alternatywy
        System.out.printf("\nPrzemiennosc alternatywy");
        System.out.printf(System.getProperty("line.separator"));
        p = false;
        q = false;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ");
        System.out.printf("%b", ((p || q) == (q || p)));
        System.out.printf(System.getProperty("line.separator"));
        p = true;
        q = false;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ");
        System.out.printf("%b", ((p || q) == (q || p)));
        System.out.printf(System.getProperty("line.separator"));
        p = false;
        q = true;
        System.out.printf("dla p majacego wartosc logiczna ");
        System.out.printf("%b", p);
        System.out.printf(" oraz q majacego wartosc logiczna ");
        System.out.printf("%b", q);
        System.out.printf(" wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ");
        System.out.printf("%b", ((p || q) == (q || p)));
        System.out.printf(System.getProperty("line.separator"));
    }
}