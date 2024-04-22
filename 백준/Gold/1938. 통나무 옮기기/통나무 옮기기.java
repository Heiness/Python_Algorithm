import java.util.*;
import java.io.*;

public class Main {
	static class Train{
		int rOfHead;
		int cOfHead;
		int dir;
		//head의 위치와 기차의 방향
		public Train(int r, int c, int d) {
			super();
			this.rOfHead = r;
			this.cOfHead = c;
			this.dir = d;
		}
	}
	static int N, aa, ans;
	static int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1};//상 우 하 좌
	static char[][] grid;
	static boolean[][] isTree;
	static int[][][] visit;
	static Queue<Train> trainQ;
	static final int notVisit = Integer.MAX_VALUE;
	
	static boolean isIn(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}
	
	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("res/train.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine()); grid = new char[N][N]; isTree = new boolean[N][N]; visit = new int[4][N][N]; trainQ = new ArrayDeque<>();
		ans = Integer.MAX_VALUE;
		for(int i = 0; i < N; i++) {
			String s = br.readLine();
			for(int j = 0; j < N; j++) {
				grid[i][j] = s.charAt(j);
				if(grid[i][j] == '1')
					isTree[i][j] = true;
				else
					isTree[i][j] = false;
			}
		}
		
		for(int i = 0; i < N; i++)
			for(int j = 0; j < N; j++)
				for(int d = 0; d < 4; d++)
					visit[d][i][j] = Integer.MAX_VALUE;

		int sr = -1,sc = -1,sDir = -1;
		label : for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(grid[i][j] == 'B') {
					sr = i;
					sc = j;
					for(int d = 0; d < 4; d++) {
						int newI = i + dr[d], newJ = j + dc[d];
						if(isIn(newI, newJ) && grid[newI][newJ] == 'B') {
							sDir = d;
							break label;
						}
					}
					
				}
			}
		}
		
		aa = 1;
		trainQ.offer(new Train(sr, sc, sDir));
		visit[sDir][sr][sc] = 0;
		while(!trainQ.isEmpty()) {
			Train t = trainQ.poll();
			
			//상하좌우 움직이기
			for(int moveDir = 0; moveDir < 4; moveDir++) {
				boolean canGo = true;
				for(int delta = 0; delta < 3; delta++) {
					int trainR = t.rOfHead + delta* dr[t.dir], trainC = t.cOfHead + delta * dc[t.dir];
					int toR = trainR + dr[moveDir], toC = trainC + dc[moveDir];
					if(!isIn(toR, toC) || isTree[toR][toC])
						canGo = false;
				}
				
				if(canGo) {
					int newHeadR = t.rOfHead + dr[moveDir], newHeadC = t.cOfHead + dc[moveDir];
					if(visit[t.dir][newHeadR][newHeadC] >= Integer.MAX_VALUE) {
						visit[t.dir][newHeadR][newHeadC] = visit[t.dir][t.rOfHead][t.cOfHead] + 1;
						trainQ.offer(new Train(newHeadR, newHeadC, t.dir));
					}
				}
			}
			
			// 회전시키기
			int middleR = t.rOfHead + dr[t.dir], middleC = t.cOfHead + dc[t.dir];
			boolean canRotate = true;
			for(int i = middleR - 1; i <= middleR + 1; i++)
				for(int j = middleC - 1; j <= middleC + 1; j++)
					if(!isIn(i, j) || isTree[i][j])
						canRotate = false;
			
			if(canRotate) {
				for(int rotateDir = 0; rotateDir < 4; rotateDir++) {
					int newHeadR = middleR + dr[rotateDir], newHeadC = middleC + dc[rotateDir], newTrainDir = (rotateDir + 2) % 4;
					if(visit[newTrainDir][newHeadR][newHeadC] >= Integer.MAX_VALUE) {
						visit[newTrainDir][newHeadR][newHeadC] = visit[t.dir][t.rOfHead][t.cOfHead] + 1;
						trainQ.offer(new Train(newHeadR, newHeadC, newTrainDir));
					}
				}
			}
		}
		
		int er = -1, ec = -1, eDir = -1;
		label : for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(grid[i][j] == 'E') {
					er = i;
					ec = j;
					for(int d = 0; d < 4; d++) {
						int newI = i + dr[d], newJ = j + dc[d];
						if(isIn(newI, newJ) && grid[newI][newJ] == 'E') {
							eDir = d;
							break label;
						}
					}
				}
			}
		}
		
		aa = 1;
		
		ans = Math.min(ans, visit[eDir][er][ec]);
		int revDir = (eDir + 2) % 4;
		ans = Math.min(ans, visit[revDir][er + 2 * dr[eDir]][ec + 2 * dc[eDir]]);
		ans = ans == Integer.MAX_VALUE ? 0 : ans;
		System.out.println(ans);
		
		br.close();
	}
}