package Tasks;

import java.util.Scanner;

public class Task9B {
    public static void main(String[] args) {

        // Write a logic that takes in input from the user. It keeps printing "try again "until the user enters "testify"
        Scanner scanner = new Scanner(System.in);
        String userInput = "";

        while (!userInput.equalsIgnoreCase("testify")) {
            System.out.println("try again");
            userInput = scanner.nextLine();
        }
    }
}
