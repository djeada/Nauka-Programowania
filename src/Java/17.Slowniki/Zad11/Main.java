import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/*
Sprawdz czy slowniki sa identyczne.
*/

public class Main {
	  		  
	   public static <A, B> boolean czyIdentyczneV1(Map<String, int[]> slownikA, Map<String, int[]> slownikB) {

        if (slownikA.size() != slownikB.size())
           return false;

        return slownikA.entrySet().stream()
                .allMatch(e -> Arrays.equals(e.getValue(), slownikB.get(e.getKey())));
    }
	    
    public static void main(String[] args) {
    	Map<String, int[]> slownikA = new HashMap<String, int[]>() {{
	        put("a", new int[] {2, 3, 5});
    		put("b", new int[] {-3, 7, 1});
		    put("c", new int[] {-8, -4, 3});
		    put("x", new int[] {11, 2, 7});
		}};
				
		Map<String, int[]> slownikB = new HashMap<String, int[]>() {{
	        put("a", new int[] {2, 3, 5});
    		put("b", new int[] {3, 7, 1});
		    put("c", new int[] {-8, -4, 3});
		    put("x", new int[] {11, 2, 7});
		}};
		
		Map<String, int[]> slownikC = new HashMap<String, int[]>() {{
	        put("a", new int[] {2, 3, 5});
    		put("b", new int[] {-3, 7, 1});
		    put("c", new int[] {-8, -4, 3});
		    put("x", new int[] {11, 2, 7});
		}};
		    		    		
		assert !czyIdentyczneV1(slownikA, slownikB);
		assert czyIdentyczneV1(slownikA, slownikC);
		assert !czyIdentyczneV1(slownikC, slownikB);

    }

}

