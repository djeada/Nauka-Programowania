/*
Najdluzszy wspolny przedrostek.
*/

public class Main {
	  
	public static String najdluzszyWspolnyPrzedrostekV1(String[] napisy) {

			if (napisy.length == 0)
				return null;
		
	        if (napisy.length != 1) {
	        	
		        int firstLen = napisy[0].length();
		        
		        for (int prefixLen = 0; prefixLen < firstLen; prefixLen++) {
	
		            char ch = napisy[0].charAt(prefixLen);
		            
		            for (String napis : napisy)
		            	if (prefixLen >= napis.length() || napis.charAt(prefixLen) != ch)
		                    return napis.substring(0, prefixLen);
		        }
	        }

	        return napisy[0];
	    }


    public static void main(String[] args) {
    	
    	String[] napisy = {"abc", "abcadlo", "abcde", "abcr", "abcdolen", "abcdef"};
    	String wynik = "abc";
    	    	
    	assert najdluzszyWspolnyPrzedrostekV1(napisy).equals(wynik);

    	
    }

}
