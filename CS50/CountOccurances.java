import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

class CountOccurances {

    public static void count(String text){
        String trimString = text
            .replaceAll(" ", "")
            .replaceAll(",", "");
        System.out.println(text.length());
        Map<Character, Long> char_count = new HashMap<>();
        for (int i = 0; i < trimString.length(); i++){
            char value = trimString.charAt(i);
            if(!char_count.containsKey(value)){
                long count = trimString
                    .chars()
                    .filter(ch -> ch == value)
                    .count();
                char_count.put(value, count);
            }
        }
        System.out.println(char_count.toString());
    }

    public static boolean palindrome(String text){
        int pointerA = 0,  pointerB = text.length()-1;
        while(pointerA < pointerB){
            if (text.charAt(pointerA) != text.charAt(pointerB)){
               return false;
            }
            pointerA ++;
            pointerB --;
        }
        return true;
    }

    public static List<String> palindromesInlongString(String text){
        List<String> palindromes = new ArrayList<>();
        int left = 0, right = 0;
        for(int position = 0; position< text.length()-1; position++){
            left = position-1;
            right = position+1;
            while(left>0 & right< text.length()-1){
                String cut = text.substring(left-1, right);
                // System.out.println(cut + " from " + left + " " + right);
                if(palindrome(cut)){
                    palindromes.add(cut);
                    System.out.println(cut);
                }
                left--;
                right++;
            }
        }
        return palindromes;
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String  text = sc.next();
        sc.close();
        List palindromes = palindromesInlongString(text);
        // if(palindrome(text)){
        //     System.out.println(text + " is a palindrome");
        // }else{
        //     System.out.println(text + " is not a palindrome");
        // }
        // count("be or not to be, that is the question");
    }
}