package com.ramesh.ood.concepts.abstraction;

//---------------------------------------
//--- STEP 00 - WHAT IS ABSTRACTION & ENCAPSULATION? 
//---------------------------------------


/**
Abstraction in layman terms (from chatgpt)
Abstraction is a concept in software engineering that involves reducing complexity by hiding unnecessary details and focusing on essential features. 
It allows us to create simplified models of complex systems, which can be easier to understand, use, and maintain.
Think of abstraction like a TV remote control. When you use a remote control, you don't need to know how the TV works or how the signal 
is transmitted to change the channel. You simply press a button and the TV responds. The remote control abstracts away the complex details of the 
TV system, allowing you to interact with it in a simple and intuitive way.
Similarly, in software engineering, we use abstraction to hide complex implementation details and focus on essential features. 
For example, we might create a high-level interface for a database system that allows us to perform simple operations like adding, deleting, 
or querying records, without needing to know the details of how the data is stored or managed.
Abstraction also allows us to create modular, reusable components that can be used in different contexts. By separating out the essential 
features of a system and hiding the implementation details, we can create components that are more flexible, adaptable, and maintainable.
Overall, abstraction is an important concept in software engineering that helps us to manage complexity and create systems that are easier 
to understand, use, and maintain.

**/

///** 
// * Abstraction = Looking only at the information that is relevant at the time. 
// *
// * Abstraction is the process or result of generalization by reducing the information content of a concept or an observable phenomenon, 
// * typically in order to retain only information which is relevant for a particular purpose. It is starting point of design.
// * Functional abstraction - means that a function can be used without taking into account how the function is implemented. 
// * Data Abstraction - means that data can be used without taking into account how the data are stored.
// */

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
public class Abstraction {

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
