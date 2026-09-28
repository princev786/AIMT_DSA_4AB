abstract class Animal{
    abstract void sound();
    void eat(){
        System.out.println("Eating time .....");
    }
}
class Pigeon extends Animal{
    void sound(){
        System.out.println("Pigeon is Singing...");
    }
    void fly(){
        System.out.println("flying...");
    }
}
class ABC{
    public static void main(String[] args) {
        Pigeon p = new Pigeon();
        p.sound();
        p.fly();
    }
}