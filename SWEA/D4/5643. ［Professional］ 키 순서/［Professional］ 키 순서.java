import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static int T, N, M, ans;
	static List<Integer>[] fow, rev;
	static int[] fowCnt, revCnt;
	
	static int dfs(int x, List<Integer>[] g, boolean[] visit) {
		visit[x] = true;
		int res = 1;
		for(int y : g[x]) 
			if(!visit[y])
				res += dfs(y, g, visit);
		return res;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine()); M = Integer.parseInt(br.readLine()); ans = 0;
			fow = new List[N + 1]; for(int i = 1; i <= N; i++) fow[i] = new ArrayList<>();
			rev = new List[N + 1]; for(int i = 1; i <= N; i++) rev[i] = new ArrayList<>();
			fowCnt = new int[N + 1]; revCnt = new int[N + 1];
			for(int q = 0; q < M; q++) {
				StringTokenizer st = new StringTokenizer(br.readLine(), " ");
				int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
				fow[a].add(b);
				rev[b].add(a);
			}
			
			for(int i = 1; i <= N; i++) {
				fowCnt[i] = dfs(i, fow ,new boolean[N + 1]);
				revCnt[i] = dfs(i, rev, new boolean[N + 1]);
				int bb = 1;
				if(fowCnt[i] + revCnt[i] == N + 1)
					ans++;
			}
			int aa = 1;
			sb.append('#').append(tc).append(' ').append(ans).append('\n');
		}
		System.out.println(sb);
		br.close();
	}

}