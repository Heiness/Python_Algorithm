import java.io.*;
import java.util.*;

import javax.security.auth.login.AccountLockedException;

public class Main {
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String T = br.readLine();
		String P = br.readLine();
		
		KMP(T,P);
	}
	
	static void KMP(String T, String P) {
		// 파이 배열 구하기
		int[] piArr = new int[P.length()];
		int i = 0;
		for(int j=1;j<P.length();j++) {
			while(i>0 && P.charAt(i)!=P.charAt(j)) i = piArr[i-1];
			if(P.charAt(i)==P.charAt(j)) piArr[j]=++i;
		}
		
		// 패턴 존재 여부 확인
		List<Integer> result = new ArrayList<>();
		i = 0;
		for(int j=0;j<T.length();j++) {
			while(i>0 && P.charAt(i) != T.charAt(j)) i = piArr[i-1];
			if(P.charAt(i)==T.charAt(j)) {
				if(++i==P.length()) {
					result.add(j-i+2);
					i = piArr[i-1];
				}
			}
		}
		
		sb.append(result.size()).append("\n");
		for(int n: result) sb.append(n).append(" ");
		System.out.println(sb);
	}
}