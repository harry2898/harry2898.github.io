package lab2;

public class AtomTest {
	public static void main(String[] args){
		
		Atom Uranium238;
		Uranium238 = new Atom(92, 146, 92);
		
		Uranium238.getAtomicMass();
		System.out.println(Uranium238.getAtomicMass());
		
		Uranium238.getAtomicCharge();
		System.out.println(Uranium238.getAtomicCharge());
		
		Uranium238.decay();

		Uranium238.getAtomicMass();
		System.out.println(Uranium238.getAtomicMass());
		
		Uranium238.getAtomicCharge();
		System.out.println(Uranium238.getAtomicCharge());
	}
}
