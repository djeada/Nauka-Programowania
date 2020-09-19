import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/*
Sprawdz czy slowo jest palindromem.
*/

public class Main {

	   public static boolean czyPalindromV1(String str) {

	        int lewo = -1;
	        int prawo = str.length();

	        while (prawo-- > lewo++) {

	            if (str.charAt(lewo) != str.charAt(prawo))
	                return false;

	        }

	        return true;
	    }


	    public static boolean czyPalindromV2(String str) {
	        return str.equals(new StringBuilder(str).reverse().toString());
	    }

    public static void main(String[] args) {
    	
    	String slowo = "kajak";

    	assert czyPalindromV1(slowo);
    	assert czyPalindromV2(slowo);
    	
    	slowo = "Pan";
    	
     	assert !czyPalindromV1(slowo);
        assert !czyPalindromV2(slowo);


    }

}
