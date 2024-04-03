import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int R, C, N;
	static int[][] grid;
	static int[] dr = {-1, 0, 1, 0}, dc = {0, -1, 0, 1};
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		R = Integer.parseInt(st.nextToken()); C = Integer.parseInt(st.nextToken()); N = Integer.parseInt(st.nextToken());
		grid = new int[R][C];
		
		for(int i = 0; i < R; i++) {
			String s = br.readLine();
			for(int j = 0; j < C; j++) {
				if(s.charAt(j) == 'O') {
					grid[i][j] = 2;
				}else {
					grid[i][j] = 0;
				}
			}
		}
		
		int aa = 1;
		
		N--;

		for(int time = 1; time <= N; time++) {
			
			List<int[]> bombs = new ArrayList<>();
			//폭탄 시간초 줄이면서 폭발하는 폭탄 넣기
			for(int i = 0; i < R; i++)
				for(int j = 0; j < C; j++)
					if(grid[i][j] >= 1) 
						if(--grid[i][j] == 0)
							bombs.add(new int[] {i, j});
			
			aa = 1;
			//폭탄 설치 todo
			for(int i = 0; i < R; i++)
				for(int j = 0; j < C; j++)
					if(grid[i][j] == 0)
						grid[i][j] = 3;
			
			aa = 1;
			//폭발시키기
			for(int[] bomb : bombs) {
				int r = bomb[0], c = bomb[1];
				grid[r][c] = 0;
				for(int d = 0; d < 4; d++) {
					int newR = r + dr[d], newC = c + dc[d];
					if(isIn(newR, newC)) {
						grid[newR][newC] = 0;
					}
				}
			}
			aa = 1;
		}
		
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(grid[i][j] > 0) {
					sb.append('O');
				}else {
					sb.append('.');
				}
			}
			sb.append('\n');
		}
		System.out.println(sb);
	}

}