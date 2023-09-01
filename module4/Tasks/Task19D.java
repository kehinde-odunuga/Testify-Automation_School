package Tasks;

public class Task19D {

    String name = "Delta";

    public static void main(String[] args) {
        Task19D name = new Task19D();
        name.printName("-Tango");
    }

    public void printName(String name){
        System.out.println(this.name + name);
    }
}


 //   THIS https://i.imgur.com/aRkRDPa.png You have a class with a method printName.
//   write a code in the printName method that will print the instance member which is "Delta"
//   and whatever name the user enter when invoking the method