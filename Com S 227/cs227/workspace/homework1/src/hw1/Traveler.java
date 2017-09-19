package hw1;

/**
 * This class implements a traveler that can visit cities.
 * @author Harrison Helgevold
 *
 */
public class Traveler {
	
	/**
	 * An instance variable that stores the amount of money the traveler has remaining.
	 */
	private int moneyLeft;
	
	/**
	 * An instance variable that stores the name of the current city the traveler is in.
	 */
	private String currentCity;
	
	/**
	 * An instance variable that stores the journal of the traveler; which lists where
	 * and for how long the traveler has been.
	 */
	private String journal;
	
	/**
	 * An instance variable that stores the cost of one postcard.
	 */
	private int postcardCost;
	
	/**
	 * An instance variable that stores the number of postcards sent home since the last
	 * time you called home for money.
	 */
	private int postcardsSent;
	
	/**
	 * An instance variable that stores the number of nights the traveler has stayed
	 * in a train station.
	 */
	private int nightsInTrainStation;
	
	/**
	 * An instance variable that stores the fixed value for the calculation of how much money
	 * a traveler can get if they call home.
	 */
	public static final int SYMPATHY_FACTOR = 30;
	
	/**
	 * A constructor that constructs a traveler with a specified amount of money and starting city.
	 * Additionally the value of each instance variable is calculated.
	 * @param initialFunds How much money the traveler starts with.
	 * @param initialCity The city in which the traveler starts.
	 */
	public Traveler(int initialFunds, City initialCity)
	{
		moneyLeft = initialFunds;
		currentCity = initialCity.getName();
		journal = (initialCity.getName() + "(start)");
		postcardCost = initialCity.costToSendPostcard();
		nightsInTrainStation = 0;
		postcardsSent = 0;
	}
	
	/**
	 * A method that returns the name of the current city the traveler is in.
	 * @return The name of the city the traveler is in.
	 */
	public String getCurrentCity()
	{
		return currentCity;
	}
	
	/**
	 * A method that returns the amount of money the traveler has remaining.
	 * @return The amount of money the traveler has remaining.
	 */
	public int getCurrentFunds()
	{
		return moneyLeft;
	}
	
	/**
	 * A method that returns the journal of the traveler.
	 * @return The traveler's journal.
	 */
	public String getJournal()
	{
		return journal;
	}
	
	/**
	 * A method that calculates whether or not the traveler is SOL.
	 * @return "true" if the traveler is SOL and "false" if the traveler is not SOL.
	 */
	public boolean isSOL()
	{
		if (moneyLeft < postcardCost)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	 * A method that returns the number of nights the traveler has spent in a train station.
	 * @return The number of nights the traveler has spent in a train station.
	 */
	public int getTotalNightsInTrainStation()
	{
		return nightsInTrainStation;
	}
	
	/**
	 * A method that moves the traveler to a new city, and updates the instance variables "currentCity",
	 * "journal", "moneyLeft", and "costToSendPostcard".
	 * Additionally, the method calculates how many nights the traveler will have to spend in a train station.
	 * @param c The city the traveler wants to visit.
	 * @param numNights The number of nights the traveler wants to stay in the city.
	 */
	public void visit(City c, int numNights)
	{
		currentCity = c.getName();
		journal = journal + ", " + c.getName() + "(" + numNights + ")";
		postcardCost = c.costToSendPostcard();
		
		/* Calculates how much money the traveler will have left, and how many 
		 * nights the traveler will spend in a train station
		 */
		int cityCost = c.lodgingCost();
		int possibleMoneyLeft = moneyLeft - cityCost * numNights;
		if (possibleMoneyLeft < 0)
		{
			while (possibleMoneyLeft < 0)
			{
				nightsInTrainStation = nightsInTrainStation + 1;
				possibleMoneyLeft = possibleMoneyLeft + c.lodgingCost();
			}
			moneyLeft = possibleMoneyLeft;
		}
		else
		{
			moneyLeft = possibleMoneyLeft;
			
		}
	}
	
	/**
	 * A method that sends a specified number of postcards home. If the cost to send the 
	 * specified number of postcards exceeds the amount of money the traveler has remaining; 
	 * the max number of postcards will be sent that leave the traveler with at least
	 * zero dollars.
	 * @param howMany The number of postcards the traveler wants to send home.
	 */
	public void sendPostcardsHome(int howMany)
	{
		int possibleMoneyLeft = moneyLeft - howMany * postcardCost;
		int numCouldntSend = 0;
		if (possibleMoneyLeft < 0)
		{
			while (possibleMoneyLeft < 0)
			{
				numCouldntSend = numCouldntSend + 1;
				possibleMoneyLeft = possibleMoneyLeft + postcardCost;
			}
			moneyLeft = possibleMoneyLeft;
			postcardsSent = postcardsSent + (howMany - numCouldntSend);
		}
		else
		{
			moneyLeft = possibleMoneyLeft;
			postcardsSent = postcardsSent + howMany;
		}
	}
	
	/**
	 * A method in which the traveler calls home for money. The amount of money the traveler
	 * receives is equal to the fixed "SYMPATHY_FACTOR" instance variable multiplied by the 
	 * "postcardsSent" instance variable. After calling home the instance variable
	 * "postcardsSent"'s value is reset back to 0.
	 */
	public void callHomeForMoney()
	{
		moneyLeft = moneyLeft + SYMPATHY_FACTOR * postcardsSent;
		postcardsSent = 0;
	}
}









