package Tasks.Task19C;

public class ClassB extends ClassA{

    String name = "Anderson";

    public static void main(String[] args) {
        ClassB object = new ClassB();
        object.newName();
    }

    public void newName(){
        System.out.println("Class A value is: "+super.name +" \nClass B value is: "+ name);
    }
}
