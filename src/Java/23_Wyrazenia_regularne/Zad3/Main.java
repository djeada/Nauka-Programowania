/*
 Sprawdz czy napis sklada sie wylacznie z cyfr.
 */


public class Main {

   public static boolean tylkoCyfryV1(String slowo) {

 	  for (char ch : slowo.toCharArray()) {
            if (!Character.isDigit(ch))
                return false;
        }
        
        return true;
    }

    public static boolean tylkoCyfryV2(String slowo) {
        return slowo.matches("[0-9]+");
    }

    public static boolean tylkoCyfryV3(String slowo) {

        return !slowo.chars()
                .anyMatch(n -> !Character.isDigit(n));
    }

    public static void main(String[] args) {
    	
    	String napis = "111342";
    	
    	assert tylkoCyfryV1(napis);
    	assert tylkoCyfryV2(napis);
    	assert tylkoCyfryV3(napis);
    	
    	napis = "1adf2";
    	
    	assert !tylkoCyfryV1(napis);
    	assert !tylkoCyfryV2(napis);
    	assert !tylkoCyfryV3(napis);

    }

}
