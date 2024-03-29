import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static long N, M, maxCounter = Long.MIN_VALUE;
	static long[] counter;
	
	static boolean check(long x) {
		long m = 0;
		for(int i = 0; i < N; i++) {
			m += x / counter[i];
			if(m >= M)
				return true;
		}
		return false;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Long.parseLong(st.nextToken()); M = Long.parseLong(st.nextToken());
		counter = new long[(int)N];
		for(int i = 0; i < N; i++) {
			counter[i] = Long.parseLong(br.readLine());
			maxCounter = Math.max(maxCounter, counter[i]);
		}
			
		//100000000000000
		
		long left = 0;
		long right = M * maxCounter;
		//F T
		while(left + 1 < right) {
			long mid = (left + right) / 2;
			if(check(mid)) {
				right = mid;
			}else {
				left = mid;
			}
		}
		System.out.println(right);
	}
}