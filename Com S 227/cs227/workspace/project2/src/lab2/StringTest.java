package lab2;

public class StringTest {
	public static void main(String[] args){
		String message = "Hello, World!";
		System.out.println(message);
		
		int theLength = message.length();
		System.out.println(theLength);
		
		char theChar = message.charAt(0);
		System.out.println(theChar);
		
		theChar = message.charAt(1);
		System.out.println(theChar);
		
		theChar = message.charAt(12);
		System.out.println(theChar);
		
		String uppercase = message.toUpperCase();
		System.out.println(uppercase);
		
		String FirstFive = message.substring(0,5);
		System.out.println(FirstFive);
		
		String replace = message.replace("o","*");
		System.out.println(replace);
	}
}
