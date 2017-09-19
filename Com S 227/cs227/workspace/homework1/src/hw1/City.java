package hw1;

/**
 * This class implements a city that a traveler can visit.
 * @author Harrison Helgevold
 *
 */
public class City {
	
	/**
	 * An instance variable that stores the name of the city.
	 */
	private String cityName;
	
	/**
	 * An instance variable that stores the cost per night to stay in the city.
	 */
	private int cityCost;
	
	/**
	 * An instance variable that stores the cost of one postcard.
	 */
	private int postcardCost;
	
	/**
	 * An instance variable that that holds the fixed percentage for the calculation of the 
	 * cost of one postcard.
	 */	
	public static final double RELATIVE_COST_OF_POSTCARD = 	0.05;
	
	/**
	 * A constructor that constructs a city with a specified name and cost per night to stay.
	 * Additionally, the cost of one postcard is calculated.
	 * @param givenName The name of the city.
	 * @param givenLodgingCost The cost per night to stay in the city.
	 */
	public City(String givenName, int givenLodgingCost)
	{
		cityName = givenName;
		
		cityCost = givenLodgingCost;
		
		/*  
		 * Calculates the cost of one postcard for the city; then stores it as
		 * the instance variable "postcardCost".
		 */
		double rawPostcardCost = cityCost * RELATIVE_COST_OF_POSTCARD;
		postcardCost = (int) Math.round(rawPostcardCost);
	}
	
	/**
	 * A method that returns the name of the city.
	 * @return The name of the city.
	 */
	public String getName()
	{
		return cityName;
	}
	
	/**
	 * A method that returns the cost to stay in the city for one night.
	 * @return The cost to stay in the city for one night.
	 */
	public int lodgingCost()
	{
		return cityCost;
	}
	
	/**
	 * A method that returns the cost of one postcard.
	 * @return The cost of one postcard.
	 */
	public int costToSendPostcard()
	{
		return postcardCost;
	}
	
	/**
	 * A method that calculates the max number of nights a traveler can stay in a city with
	 * their remaining funds.
	 * @param funds The amount of money a traveler has left.
	 * @return The max number of nights a traveler can stay in the city.
	 */
	public int maxLengthOfStay(int funds)
	{
		int maxNightsLeft = funds / cityCost;
		return maxNightsLeft;
	}
	
	/**
	 * A method that calculates the max number of postcards a traveler
	 * can send with their remaining funds.
	 * @param funds The amount of money a traveler has left.
	 * @return The max number of postcards a traveler can send.
	 */
	public int maxNumberOfPostcards(int funds)
	{
		int maxPostcards = funds / postcardCost;
		return maxPostcards;
	}
	
}
