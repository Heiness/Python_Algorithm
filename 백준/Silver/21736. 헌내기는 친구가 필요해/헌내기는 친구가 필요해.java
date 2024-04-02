import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M, ans, sr, sc;
	static char[][] grid;
	static int[] dr = {-1, 0, 1, 0}, dc = {0, -1, 0, 1};
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}
	
	static void dfs(int r, int c) {
		if(grid[r][c] == 'P') 
			ans++;
		
		grid[r][c] = 'X';
		
		for(int d = 0; d < 4; d++) {
			int newR = r + dr[d], newC = c + dc[d];
			if(isIn(newR, newC) && grid[newR][newC] != 'X')
				dfs(newR, newC);
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken()); grid = new char[N][M];
		for(int i = 0; i < N; i++) {
			String s = br.readLine();
			for(int j = 0; j < M; j++) {
				grid[i][j] = s.charAt(j);
				if(grid[i][j] == 'I') {
					sr = i;
					sc = j;
					grid[i][j] = 'O';
				}
			}
		}
		
		dfs(sr, sc);
		
		System.out.println(ans == 0? "TT" : ans);
		
		br.close();
	}

}