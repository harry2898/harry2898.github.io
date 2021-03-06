package lab2;

public class Atom{
	
	private int protons;
	
	private int neutrons;
	
	private int electrons;
	
	public Atom(int givenProtons, int givenNeutrons, int givenElectrons)
	{
		
		protons = givenProtons;
		
		neutrons = givenNeutrons;
		
		electrons = givenElectrons;
	}
	
	int getAtomicMass()
		{
		int atomicMass = protons + neutrons;
		return atomicMass;
	}

	int getAtomicCharge()
	{
		int atomicCharge = protons - electrons;
		return atomicCharge;
	}
	public void decay()
	{
		int givenProtons = protons - 2;
		int givenNeutrons = neutrons - 2;
	}
}