package hw1;

import hw2.ClockRadio;

public class TravelerTest {
	public static void main(String[] args)
	{
		City paris = new City("Paris", 75);
		City rome = new City("Rome", 50);
		
		Traveler t = new Traveler(500, paris);
		
		System.out.println("Get City Name Test");
		System.out.println("Expecting: 'Paris'");
		System.out.println("Result: " + t.getCurrentCity());
		System.out.println(" ");
		
		System.out.println("Get Journal Test");
		System.out.println("Expecting: 'Paris(start)'");
		System.out.println("Result: " + t.getJournal());
		System.out.println(" ");
		
		t.visit(rome, 2);
		
		System.out.println("Get Current City Test");
		System.out.println("Expecting: 'Rome'");
		System.out.println("Result: " + t.getCurrentCity());
		System.out.println(" ");
		
		System.out.println("Get Journal Test");
		System.out.println("Expecting: 'Paris(start), Rome(2)'");
		System.out.println("Result: " + t.getJournal());
		System.out.println(" ");
		
		t = new Traveler(500, paris);
		
		System.out.println("Get City Name Test");
		System.out.println("Expecting: 'Paris'");
		System.out.println("Result: " + t.getCurrentCity());
		System.out.println(" ");
		
		System.out.println("Get Journal Test");
		System.out.println("Expecting: 'Paris(start)'");
		System.out.println("Result: " + t.getJournal());
		System.out.println(" ");
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '500'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		t.visit(rome, 2);
		
		System.out.println("Get Current City Test");
		System.out.println("Expecting: 'Rome'");
		System.out.println("Result: " + t.getCurrentCity());
		System.out.println(" ");
		
		System.out.println("Get Journal Test");
		System.out.println("Expecting: 'Paris(start), Rome(2)'");
		System.out.println("Result: " + t.getJournal());
		System.out.println(" ");
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '400'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		t.visit(paris, 7);
		
		System.out.println("Get Current City Test");
		System.out.println("Expecting: 'Paris'");
		System.out.println("Result: " + t.getCurrentCity());
		System.out.println(" ");
		
		System.out.println("Get Journal Test");
		System.out.println("Expecting: 'Paris(start), Rome(2), Paris(7)'");
		System.out.println("Result: " + t.getJournal());
		System.out.println(" ");
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '25'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		System.out.println("Get Total Nights in Train Station Test");
		System.out.println("Expecting: '2'");
		System.out.println("Result: " + t.getTotalNightsInTrainStation());
		System.out.println(" ");
		
		t.visit(paris, 7);
		
		System.out.println("Get Current City Test");
		System.out.println("Expecting: 'Paris'");
		System.out.println("Result: " + t.getCurrentCity());
		System.out.println(" ");
		
		System.out.println("Get Journal Test");
		System.out.println("Expecting: 'Paris(start), Rome(2), Paris(7), Paris(7)'");
		System.out.println("Result: " + t.getJournal());
		System.out.println(" ");
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '25'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		System.out.println("Get Total Nights in Train Station Test");
		System.out.println("Expecting: '9'");
		System.out.println("Result: " + t.getTotalNightsInTrainStation());
		System.out.println(" ");
		
		t.sendPostcardsHome(1);
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '21'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		t.sendPostcardsHome(12);
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '1'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		
		System.out.println("Are You Technically SOL Test");
		System.out.println("Expecting: 'true'");
		System.out.println("Result: " + t.isSOL());
		System.out.println(" ");
		
		t.callHomeForMoney();
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '181'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
		
		t.callHomeForMoney();
		
		System.out.println("Get Current Funds Test");
		System.out.println("Expecting: '181'");
		System.out.println("Result: " + t.getCurrentFunds());
		System.out.println(" ");
	}
}