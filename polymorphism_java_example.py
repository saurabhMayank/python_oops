package com.ramesh.ood.concepts.polymorphism;

//---------------------------------------
//--- STEP 00 - WHAT IS POLYMORPHISM? 
//---------------------------------------

///** 
// * Polymorphism = single interface multiple implementations.
// * In the below example -> Payment interface is implemented by CardPayment class and CashPayment Class
// * So object of Payment Interface, can be of Card or Cash payment -> decided on runtime -> Need not re-initialise two payment objects
// * for two classes -> saving lot of space
// *
// * Access objects of different types through the same interface
// * Each type can provide its own independent implementation of this interface.
	
// * Compile time Polymorphism -> Method overloading
// * multiple methods within the same class that `use the same name`
// * Methods should differ in -> 
	// * different number of parameters, one method accepting 2 and another one accepting 3 parameters
	// * types of the parameters need to be different, one method accepting a String and another one accepting a Long
// * Due to the different sets of parameters, each method has a different signature. 


	
// * Run time Polymorphism -> Method Overriding
// * a subclass can override a method of its superclass, enabling the developer of the subclass 
// to customize or completely replace the behavior of that method
	
// * Both methods implemented by the super- and subclasses share the same name and parameters. 
// However, they provide different functionality.

/**
	


//---------------------------------------
//--- STEP 01 - UNDERSTAND POLYMORPHISM BY SIMPLE EXAMPLE
//---------------------------------------

/**
 * Test class - If variable is initialized with super type (Payment), then it gives you flexibility to assign any new implementation of that type
 * (i.e. CashPayment, CreditPayment).
 * 
 * @author tirthalp
 * 
 */
public class Polymorphism {

	public static void main(String[] args) {
		// Here the runtime polymorphism fundamental is not applied, as it is of single CashPayment form
		CashPayment c = new CashPayment();
		c.pay();

		// Now the initialization is done using runtime polymorphism and it can have many forms at runtime
		// Single payment "p" instance can be used to pay by cash and credit card
		Payment p = new CashPayment();
		p.pay(); // Pay by cash

		p = new CreditPayment();
		p.pay(); // Pay by creditcard
	}

}

/**
 * This represents payment interface
 * 
 * @author tirthalp
 * 
 */
interface Payment {
	public void pay();
}

/**
 * Cash IS-A Payment type
 * 
 * @author tirthalp
 * 
 */
class CashPayment implements Payment {

	// method overriding
	@Override
	public void pay() {
		System.out.println("This is cash payment");
	}

}

/**
 * Creditcard IS-A Payment type
 * 
 * @author tirthalp
 * 
 */
class CreditPayment implements Payment {

	// method overriding
	@Override
	public void pay() {
		System.out.println("This is credit card payment");
	}

}
