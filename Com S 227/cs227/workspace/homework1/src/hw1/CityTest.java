package hw1;

public class CityTest {
	public static void main(String[] args)
	{
		City c = new City("Paris", 75);
		
		System.out.println("Get City Name Test");
		System.out.println("Expecting: 'Paris'");
		System.out.println("Result: " + c.getName());
		System.out.println(" ");

		System.out.println("Get Lodging Cost Test");
		System.out.println("Expecting: '75'");
		System.out.println("Result: " + c.lodgingCost());
		System.out.println(" ");

		System.out.println("Get Postcard Cost Test");
		System.out.println("Expecting: '4'");
		System.out.println("Result: " + c.costToSendPostcard());
		System.out.println(" ");
		
		System.out.println("Get Max Length of Stay Test");
		System.out.println("Expecting: '6'");
		System.out.println("Result: " + c.maxLengthOfStay(500));
		System.out.println(" ");
		
		System.out.println("Get Max Number of Postcards Test");
		System.out.println("Expecting: '12'");
		System.out.println("Result: " + c.maxNumberOfPostcards(50));
		System.out.println(" ");
	}
}
