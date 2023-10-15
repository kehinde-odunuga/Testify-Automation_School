package Tasks;

public class Task6 {
    public static void main(String[] args) {

        // Write a code to reverse the string DEMOCRACY and get the word COME out of it.

        String originalWord = "DEMOCRACY";
        String reversedWord = "";

        // function to reverse originalWord
        for (int i = 0; i < originalWord.length(); i++) {
            reversedWord = originalWord.charAt(i) + reversedWord;
        }

        // print the word COME at a particular index
        System.out.println(reversedWord.substring(4, 8));
    }
}
