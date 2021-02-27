
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

//Helper class added by C++ to Java Converter:

package tangible;

//----------------------------------------------------------------------------------------
//	Copyright © 2006 - 2021 Tangible Software Solutions, Inc.
//	This class can be used by anyone provided that the copyright notice remains intact.
//
//	This class provides the ability to convert basic C++ 'cin' behavior.
//----------------------------------------------------------------------------------------
public final class ConsoleInput
{
	private static boolean goodLastRead = false;
	public static boolean lastReadWasGood()
	{
		return goodLastRead;
	}

	public static String readToWhiteSpace(boolean skipLeadingWhiteSpace)
	{
		String input = "";
		char nextChar;
		while (Character.isWhitespace(nextChar = (char)System.in.read()))
		{
			//accumulate leading white space if skipLeadingWhiteSpace is false:
			if (!skipLeadingWhiteSpace)
			{
				input += nextChar;
			}
		}
		//the first non white space character:
		input += nextChar;

		//accumulate characters until white space is reached:
		while (!Character.isWhitespace(nextChar = (char)System.in.read()))
		{
			input += nextChar;
		}

		goodLastRead = input.length() > 0;
		return input;
	}

	public static String scanfRead()
	{
		return scanfRead(null, -1);
	}

	public static String scanfRead(String unwantedSequence)
	{
		return scanfRead(unwantedSequence, -1);
	}

	public static String scanfRead(String unwantedSequence, int maxFieldLength)
	{
		String input = "";

		char nextChar;
		if (unwantedSequence != null)
		{
			nextChar = '\0';
			for (int charIndex = 0; charIndex < unwantedSequence.length(); charIndex++)
			{
				if (Character.isWhitespace(unwantedSequence.charAt(charIndex)))
				{
					//ignore all subsequent white space:
					while (Character.isWhitespace(nextChar = (char)System.in.read()))
					{
					}
				}
				else
				{
					//ensure each character matches the expected character in the sequence:
					nextChar = (char)System.in.read();
					if (nextChar != unwantedSequence.charAt(charIndex))
						return null;
				}
			}

			input = (new Character(nextChar)).toString();
			if (maxFieldLength == 1)
				return input;
		}

		while (!Character.isWhitespace(nextChar = (char)System.in.read()))
		{
			input += nextChar;
			if (maxFieldLength == input.length())
				return input;
		}

		return input;
	}
}