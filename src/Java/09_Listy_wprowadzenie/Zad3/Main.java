import java.util.stream.IntStream;

/*
Znajdz klucz w tablicy.
*/

public class Main {
	  
	 public static int znajdzKluczV1(int[] tablica, int klucz) {

	        for (int i = 0; i < tablica.length; i++)
	            if (tablica[i] == klucz) 
	                return i;
	        
	        return -1;
	    }

	    public static int znajdzKluczV2(int[] tablica, int klucz) {

	        return IntStream.range(0, tablica.length)
	                .filter(i -> klucz == tablica[i])
	                .findFirst()
	                .orElse(-1);
	    }
	    
    public static void main(String[] args) {
    	
    	int[] tablica = new int[]{3, 5, -7, 4, 9, -11, 2};
    	int klucz = 2;
    	int wynik = 6;
    	    	
    	assert znajdzKluczV1(tablica, klucz) == wynik;
    	assert znajdzKluczV2(tablica, klucz) == wynik;
    	
    	tablica = new int[]{3, -2, 4, 9, -3, -40, 8, 5, -7, -1};
    	klucz = 2;
    	wynik = -1;
    	    	
    	assert znajdzKluczV1(tablica, klucz) == wynik;
    	assert znajdzKluczV2(tablica, klucz) == wynik;
    	
    	
    }

}
