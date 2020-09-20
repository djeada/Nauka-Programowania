import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/*
Posortuj slownik.
*/

public class Main {

	public static List<String>  sortujWzgledemKluczyV1(Map<String, Integer> slownik) {

		List<String> lista = new ArrayList<String>();

		for (String key: slownik.keySet())
			lista.add(key);
		
		Collections.sort(lista);
		
		return lista;
    }

	public static List<Integer>  sortujWzgledemWartosciV1(Map<String, Integer> slownik) {

		List<Integer> lista = new ArrayList<Integer>();

		for (String key: slownik.keySet())
			lista.add(slownik.get(key));
		
		Collections.sort(lista);
		
		return lista;
    }
	    
    public static void main(String[] args) {
    	Map<String, Integer> slownik = new HashMap<String, Integer>() {{
	        put("c", 3);
    		put("x", 5);
		    put("a", -2);
		    put("b", 4);
		}};
		
		List<String> wynikKlucze = Arrays.asList("a", "b", "c", "x");
		List<Integer> wynikWartosci = Arrays.asList(-2, 3, 4, 5);

		assert sortujWzgledemKluczyV1(slownik).equals(wynikKlucze);
		assert sortujWzgledemWartosciV1(slownik).equals(wynikWartosci);

    }

}
