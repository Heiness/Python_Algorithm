import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;
        StringBuilder sb = new StringBuilder();
        while (true) {
            s = br.readLine();
            if (s.equals(".")) break;
            sb.append(solution(s)).append("\n");
        }
        System.out.println(sb);
    }

    static String solution(String s){
        Deque<Character> st = new ArrayDeque<>();

        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);

            if(c=='(' || c=='[') st.offer(c);
            else if(c==')'){
                if(st.isEmpty() || st.peekLast()!='(') return "no";
                else if(st.peekLast()=='(') st.pollLast();
            }
            else if(c==']'){
                if(st.isEmpty() || st.peekLast()!='[') return "no";
                else if(st.peekLast()=='[') st.pollLast();
            }
        }
        if(st.isEmpty()) return "yes";
        else return "no";
    }
}