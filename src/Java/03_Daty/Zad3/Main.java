
public class Main
{
	public static void main(String[] args)
	{

		//Czy rok jest przestepny?

		System.out.print("Podaj rok:");
		System.out.print("\n");

		int rok;
		rok = Integer.parseInt(System.console().readLine());

		if (rok % 4 == 0)
		{

			if (rok % 100 == 0)
			{
				 if (rok % 400 == 0)
				 {
						System.out.print("rok jest przestepny");
						System.out.print("\n");
				 }
				  else
				  {
						System.out.print("rok nie jest przestepny");
						System.out.print("\n");
				  }
			}

			else
			{
				System.out.print("rok jest przestepny");
				System.out.print("\n");
			}
		}

		else
		{
			System.out.print("rok nie jest przestepny");
			System.out.print("\n");
		}

	}


}