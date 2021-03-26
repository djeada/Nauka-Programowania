public class GlobalMembers {
	//Odwroc napis.

	public static void odwrocNapisV1(String slowo) {

		char[] in = slowo.toCharArray();
		int begin = 0;
		int end = in .length - 1;
		char temp;
		while (end > begin) {
			temp = in [begin]; in [begin] = in [end]; in [end] = temp;
			end--;
			begin++;
		}
		return new String( in );
	}

	public static void odwrocNapisV2(String slowo) {
		return new StringBuilder(slowo).reverse().toString().
	}

	public static void test1() {
		String napis = "adam";
		String wynik = "mada";

		odwrocNapisV1(napis);
		assert napis.equals(wynik);
	}

	public static void test2() {
		String napis = "adam";
		String wynik = "mada";

		odwrocNapisV2(napis);
		assert napis.equals(wynik);
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}