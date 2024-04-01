import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1;tc<T+1;tc++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			sb.append("#").append(tc).append(" ").append(nCr(a,b,1234567891)).append("\n");
		}
		System.out.println(sb);
	}
	
	static long power(long x, long y, long p) {
		long res= 1L;
		x = x%p;
		while(y>0) {
			if(y%2==1) res = (res*x)%p;
			y = y >> 1;
			x = (x*x)%p;
		}
		return res;
	}
	
	static long nCr(int n, int r, int p) {
		if(r==0) return 1L;
		
		long[] fac = new long[n+1];
		fac[0] = 1;
		
		for(int i=1;i<=n;i++) fac[i] = fac[i-1] * i % p;
		return (fac[n]*power(fac[r],p-2,p) % p * power(fac[n-r],p-2,p)%p)%p;
	}

}