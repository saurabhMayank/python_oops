# here we are going to give, class vs abstract class vs interfaces
# just for the sake of understanding -> example will be in java

interface Cognition{
  void doProgramming();
}
interface Motor{
  void write();
  void bite();
}
interface Brain extends Cognition, Motor{
  //the logic behind extends here is we cannot
  //implement anything in an interface
  int number = 1;
}
abstract class Body{
  //Totally valid
}
abstract class clothes extends Body{
  abstract void whatDoYouLike( String type );
}
//As in the next class I don't plan to implement everything so I //have to leave it as abstract
abstract class LivingBeing extends Clothes implements Brain{
  void bite(){
    System.out.println( "I know how to do that, ghaawww" );
  }
  void whatDoYouLike( String type ){
    System.out.println( "I like to wear a" + type );
  }
}
//Now I am planning to implement all the abstract methods so time to //switch to a concrete class
class Human extends LivingBeing{
  void write(){
    System.out.println( "I will write a medium post !" );
  }
  void doProgramming(){
    System.out.println( "I would love to code !!" );
  }
}
class Dog extends LivingBeing{
  void write(){
    System.out.println( "Woof Woof ??" );
  }
void doProgramming(){
    System.out.println( "Woof Woof ??" );
  }
}
