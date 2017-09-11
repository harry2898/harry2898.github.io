package lab2;

public class Atom{
	public Atom(int givenProtons, int givenNeutrons, int givenElectrons){
		
		int getAtomicMass()
		{
			int AtomicMass = givenProtons + givenNeutrons;
			return AtomicMass;
		}

		int getAtomicCharge()
		{
			int AtomicCharge = givenProtons - givenElectrons;
			return AtomicCharge;
		}
		public void decay()
		{
			int givenProtons = givenProtons - 2;
			int givenNeutrons = givenNeutrons - 2;
		}
	}
}