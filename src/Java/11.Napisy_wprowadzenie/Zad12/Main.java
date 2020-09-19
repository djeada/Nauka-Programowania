/*
Usun spacje ze zdania.
*/


public class Main {


    public static String usunSpacjeV1(String zdanie) {
        return zdanie.replaceAll("\\s", "");
    }

    public static void main(String[] args) {
    	
    	String zdanie = "lezy jezy na wierzy";
    	String wynik = "lezyjezynawierzy";
    	
    	assert usunSpacjeV1(zdanie).equals(wynik);
    	
    	zdanie = "";
    	wynik = "d";
    	
    	assert usunSpacjeV1(zdanie).equals(wynik);
    	

    }

}
