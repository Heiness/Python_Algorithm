
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] arr;
	static int N, M, R;
	static int midN, midM;
	
	static void swapMN() {
		int temp = N;
		N = M;
		M = temp;
		temp = midN;
		midN = midM;
		midM = temp;	
	}
	
	static int[][] upDown() {
		int[][] tmp = new int[N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				tmp[i][j] = arr[Math.abs(N - i - 1)][j];
			}
		}
		return tmp;
	}
	
	static int[][] leftRight() {
		int[][] tmp = new int[N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				tmp[i][j] = arr[i][Math.abs(M - j - 1)];
			}
		}
		return tmp;
	}
	
	static int[][] rotateToRight(){
		int[][] tmp = new int[M][N];
		for(int i = 0; i < M; i++) {
			for(int j = 0; j < N; j++) {
				tmp[i][j] = arr[N - j - 1][i]; // 1, 4 => 1, 1
			}
		}
		swapMN();
		return tmp;
	}
	
	static int[][] rotateToLeft(){
		int[][] tmp = new int[M][N];
		for(int i = 0; i < M; i++) {
			for(int j = 0; j < N; j++) {
				tmp[i][j] = arr[j][M - i - 1];
			}
		}
		swapMN();
		return tmp;
	}
	
	static int[][] rotateLumpRight(){
		int[][] tmp = new int[N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(i < midN && j < midM) {
					tmp[i][j] = arr[midN + i][j];
				}else if(i < midN && j >= midM) {
					tmp[i][j] =  arr[i][j - midM];
				}else if(i >= midN && j >= midM) {
					tmp[i][j] = arr[i - midN][j];
				}else if(i >= midN && j < midM) {
					tmp[i][j] = arr[i][midM + j];
				}else {
					throw new IllegalStateException();
				}
			}
		}
		return tmp;
	}
	
	static int[][] rotateLumpLeft(){
		int[][] tmp = new int[N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(i < midN && j < midM) {
					tmp[i][j] = arr[i][midM + j];
				}else if(i < midN && j >= midM) {
					tmp[i][j] = arr[midN + i][j];
				}else if(i >= midN && j >= midM) {
					tmp[i][j] = arr[i][j - midM];
				}else if(i >= midN && j < midM) {
					tmp[i][j] = arr[i - midN][j];
				}else {
					throw new IllegalStateException();
				}
			}
		}
		return tmp;
	}
	
	static void rotate(int c) {
		int[][] tmp;
		switch(c) {
		case 1:
			tmp = upDown();
			break;
		case 2:
			tmp = leftRight();
			break;
		case 3:
			tmp = rotateToRight();
			break;
		case 4:
			tmp = rotateToLeft();
			break;
		case 5:
			tmp = rotateLumpRight();
			break;
		case 6:
			tmp = rotateLumpLeft();
			break;
		default:
			throw new IllegalStateException();
		}
		arr = tmp;
	}
	
	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("res/_240208/input_16953.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken()); R = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		midN = N / 2; midM = M / 2;
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int q = 0; q < R; q++) {
			int c = Integer.parseInt(st.nextToken());
			rotate(c);
		}
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				sb.append(arr[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
			

	}

}
