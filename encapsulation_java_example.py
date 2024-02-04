package com.ramesh.ood.concepts.encapsulation;

//---------------------------------------
//--- STEP 00 - WHAT IS ENCAPSULATION? 
//---------------------------------------



///**
// * Encapsulation = Data hiding mechanism.
// *
// * The process of binding or wrapping the data and the codes that operates on the data into a single entity. This keeps the data safe from 
// * outside interface and misuse. One way to think about encapsulation is as a protective wrapper that prevents code and data from being arbitrarily 
// * accessed by other code defined outside the wrapper. 
// * For example - if a field is declared private, it cannot be accessed by anyone outside the class, thereby hiding the fields within the class. 
// */

/**
In Layman terms Encapsulation (From Chat GPT)
Encapsulation is a concept in object-oriented programming that involves grouping together related data and functions into a single unit, called a class. 
This unit acts as a protective wrapper around the data and functions, preventing other parts of the program from accessing or modifying them directly.


Think of encapsulation like a gift box. The gift inside the box represents the data and functions in a class. 
The box itself represents the encapsulation,  or protection, around the gift.
By encapsulating the data and functions in a class, we can control how they are accessed and used. 

We can define specific methods, or functions, 
that can be used to access or modify the data, while keeping the data itself hidden from other parts of the program.
This has several benefits, including improved security, more efficient code, and easier maintenance.
Encapsulation also helps to prevent unintended side effects that can occur when data is accessed or modified directly.
Overall, encapsulation is an important concept in object-oriented programming that helps to improve the organization, efficiency, 
and security of software.						    
**/




//---------------------------------------
//--- STEP 01 - UNDERSTAND ENCAPSULATION BY EXAMPLE
//---------------------------------------

/**
 * 
 * Encapsulation goals of Person class
 * 
 * (1) The id and name parameters should not be accessible directly outside Person class - achieved by private declaration
 * 
 * (2) The id value can be assigned in Person class only and other class should not be able to change - not included setId() method
 * 
 * 
 */
class Person {

	private double id;
	private String name;

	public Person() {
		// Only Person class can access and assign
		id = Math.random();
		sayHello();
	}

	// This method is protected for giving access within Person class only
	private void sayHello() {
		System.out.println("Hello - " + getId());
	}

	public double getId() {
		return id;
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}

/**
 * Test class for Person
 * 
 * @author tirthalp
 * 
 */
public class Encapsulation {

	public static void main(String[] args) {

		Person p1 = new Person();
		p1.setName("Tirthal");
		/*
		 * Note: As id and name are encapsulated in Person class, those cannot be accessed directly here. Also there is no way to assign id in this
		 * class. Try to uncomment below code and you would find compile time error.
		 */
		// p1.id = "123";
		// p1.name = "this will give compile time error";
		// p1.sayHello(); // You can't access this method, as it is private to Person

		System.out.println("Person 1 - " + p1.getId() + " : " + p1.getName());
	}
}
