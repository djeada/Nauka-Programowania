
import java.util.regex.Pattern;

/*
Czy podnapis nalezy do napisu.
*/

public class Main {
	
	public static boolean czyNalezyV1(String napis, String podnapis) {
	    return napis.matches("(?i).*" + Pattern.quote(podnapis) + ".*");
	}
	
	public static boolean czyNalezyV2(String napis, String podnapis) {
	    return napis.indexOf(podnapis) != -1; 
	}

    public static void main(String[] args) {
    	
    	String napis = "Mozart gra na skrzypcach";
    	String podnapis = "skrzyp";
    	
    	assert  czyNalezyV1(napis, podnapis);
    	assert  czyNalezyV2(napis, podnapis);

    	napis = "Lezy jerzy na wiezy";
    	podnapis = "nan";
    	
    	assert  !czyNalezyV1(napis, podnapis);
    	assert  !czyNalezyV2(napis, podnapis);
    	
    }

}
