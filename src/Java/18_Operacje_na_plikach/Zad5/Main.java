import java.util.*;



package <missing>;

public class GlobalMembers
{
	//Otrzymujesz napis reprezentujacy sciezke pliku tekstowego.
	//Kazdy wiersz pliku reprezentuja adres ip. Posortuj adresy ip i zapisz je w liscie.

	public static ArrayList<String> wczytajPlik(final String sciezka)
	{

		ArrayList<String> tresc = new ArrayList<String>();
		try
		{
			String wiersz;
			std::ifstream plik = new std::ifstream(sciezka);
			plik.exceptions(std::ifstream.eofbit | std::ifstream.failbit | std::ifstream.badbit);

			while (plik != null)
			{
				getline(plik, wiersz);
				tresc.add(wiersz);
			}

			plik.close();
		}

		catch (RuntimeException e)
		{
			System.out.print("Error : ");
			System.out.print(e.getMessage());
			System.out.print("\n");
		}

		return new ArrayList<String>(tresc);
	}

	public static void sortujAdresyIp(ArrayList<String> ip)
	{
//C++ TO JAVA CONVERTER NOTE: 'auto' variable declarations are not supported in Java:
//ORIGINAL LINE: std::sort(ip.begin(), ip.end(), [](const auto& lhs, const auto& rhs)
//C++ TO JAVA CONVERTER TODO TASK: The 'Compare' parameter of std::sort produces a boolean value, while the Java Comparator parameter produces a tri-state result:
	Collections.sort(ip, (lhs, rhs) ->
	{
		ArrayList<Integer> oktetA = new ArrayList<Integer>();
		ArrayList<Integer> oktetB = new ArrayList<Integer>();

		var fun = (ArrayList<Integer> wektor, String slowo) ->
		{
			std::stringstream ss = new std::stringstream(slowo);

			for (int i; ss >> i;)
			{
				wektor.add(i);
				if (ss.peek() == '.')
				{
					ss.ignore();
				}
			}
		};

		fun(oktetA, lhs);
		fun(oktetB, rhs);

		if (oktetA == oktetB)
		{
			return false;
		}

		else if (oktetA.get(0) > oktetB.get(0))
		{
			return false;
		}

		else if (oktetA.get(0) < oktetB.get(0))
		{
			return true;
		}

		else if (oktetA.get(1) > oktetB.get(1))
		{
			return false;
		}

		else if (oktetA.get(1) < oktetB.get(1))
		{
			return true;
		}

		else if (oktetA.get(2) > oktetB.get(2))
		{
			return false;
		}

		else if (oktetA.get(2) < oktetB.get(2))
		{
			return true;
		}

		else if (oktetA.get(3) > oktetB.get(3))
		{
			return false;
		}

		else if (oktetA.get(3) < oktetB.get(3))
		{
			return true;
		}
	});
	}

	public static void main(String[] args)
	{

		final String sciezka = "folder/adresy_ip.txt";
		var ip = wczytajPlik(sciezka);
		sortujAdresyIp(ip);

	}

}