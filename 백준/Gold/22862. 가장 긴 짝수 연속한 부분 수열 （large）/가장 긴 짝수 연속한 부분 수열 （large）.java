import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main {
	static class Odd{
		int oddNum;
		int leftEvenNum;
		int rightEvenNum;
	}
	static int[] arr;
	static int N, K, s, e, oddCnt, ans = Integer.MIN_VALUE;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken()); K = Integer.parseInt(st.nextToken()); arr = new int[N]; 
		st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i < N; i++) 
			arr[i] = Integer.parseInt(st.nextToken());
		
		s = 0;
		e = 0;
		oddCnt = arr[0] % 2 == 0 ? 0 : 1;
		while(true) {
			//ans = Math.max(ans, e - s + 1 - oddCnt);
			if(oddCnt > K) {
				if(arr[s++] % 2 == 1)
					oddCnt--;
			}else {
				ans = Math.max(ans, e - s + 1 - oddCnt);
				if(++e >= N)
					break;
				
				if(arr[e] % 2 == 1)
					oddCnt++;
			}
		}
		
		System.out.println(ans);
		
	}
}