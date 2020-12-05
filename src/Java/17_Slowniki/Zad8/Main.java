import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static List<Character> policzPowtarzajaceSieZnakiV1(String slowo) {
    	
    	List<Character> listaZnakow = new ArrayList<Character>();
    	
        if (slowo != null) {
        	  Map<Character, Integer> histo = new HashMap<>();                

        	  for (char ch : slowo.toCharArray()) {
        		  
        		  histo.compute(ch, (k, v) -> (v == null) ? 1 : ++v);
        		  
        		  if (histo.get(ch) > 1 && !listaZnakow.contains(ch))
        			  listaZnakow.add(ch);
        	  }   
        }  
           
        return listaZnakow;
    }


    public static List<Character> policzPowtarzajaceSieZnakiV2(String slowo) {
    	List<Character> listaZnakow = new ArrayList<Character>();

        if (slowo != null) {
        	 Map<Character, Long> histo = slowo.chars()
                     .mapToObj(c -> (char) c)
                     .collect(Collectors.groupingBy(c -> c, Collectors.counting()));
        
	        for (Map.Entry<Character, Long> para : histo.entrySet())
	        	 if (para.getValue() > 1 && !listaZnakow.contains(para.getKey()))
	   			  	listaZnakow.add(para.getKey());
        }
        
        return listaZnakow;
    }

    public static void main(String[] args) {
        
        String zdanie = "Halo nazywam sie Pan";
    	List<Character> listaZnakow = Arrays.asList('a', ' ', 'n');

    	assert policzPowtarzajaceSieZnakiV1(zdanie).equals(listaZnakow);
    	assert policzPowtarzajaceSieZnakiV2(zdanie).equals(listaZnakow);

    }
}
