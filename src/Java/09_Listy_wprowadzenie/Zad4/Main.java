
/*
Znajdz najwieksza i najmniejsza wartosc w tablicy.
*/

public class Main {
	  		  
	public static int znajdzMaksV1(int[] tablica) {

		int maks = tablica[0];

		for (int elem : tablica)
			if (elem > maks)
				maks = elem;

		return maks;
	}

    public static int znajdzMaksV2(int[] tablica) {

        int maks = tablica[0];

        for (int elem : tablica)
            maks = Math.max(maks, elem);

        return maks;
    }
	    
    public static void main(String[] args) {
    	
    	int[] tablica = new int[]{3, 5, -7, 4, 9, -11, 2};
    	int wynik = 9;
    	    	
    	assert znajdzMaksV1(tablica) == wynik;
    	assert znajdzMaksV2(tablica) == wynik;
    	
    	tablica = new int[]{3, -2, 4, 29, -3, -40, 8, 5, -7, -1};
    	wynik = 29;
	    	
		assert znajdzMaksV1(tablica) == wynik;
		assert znajdzMaksV2(tablica) == wynik;
    	
    }

}
