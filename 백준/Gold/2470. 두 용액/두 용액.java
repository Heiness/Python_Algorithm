import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[] ans = new int[3];
	static List<Integer> minus = new ArrayList<>();
	static List<Integer> plus = new ArrayList<>();
	
	static int binarySearch(int v) {
		// left < v && right >= v
		if(v <= plus.get(0)) {
			return 0;
		}else if(plus.get(plus.size() - 1) < v) {
			return plus.size() - 1;
		}
		
		int left = 0;
		int right = plus.size() - 1;
		while(left + 1 < right) {
			int mid = (left + right) / 2;
			if(plus.get(mid) < v) {
				left = mid;
			}else {
				right = mid;
			}
		}
		return right;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for(int i = 0 ; i < N; i++) {
			int a = Integer.parseInt(st.nextToken());
			if(a < 0) {
				minus.add(a);
			}else {
				plus.add(a);
			}
		}
		ans[2] = Integer.MAX_VALUE;
		
		minus.sort((i1, i2) -> Integer.compare(i1,i2));
		plus.sort((i1, i2) -> Integer.compare(i1,i2));
		int aa = 1;
		
		if(minus.size() == 0) {
			ans[0] = plus.get(0);
			ans[1] = plus.get(1);
		}else if(plus.size() == 0) {
			ans[0] = minus.get(minus.size() - 2);
			ans[1] = minus.get(minus.size() - 1);
		}else {
			if(plus.size() > 1) {
				if(ans[2] > Math.abs(plus.get(0) + plus.get(1))) {
					ans[0] = plus.get(0);
					ans[1] = plus.get(1);
					ans[2] = Math.abs(plus.get(0) + plus.get(1));
				}
			}
			if(minus.size() > 1) {
				if(ans[2] > Math.abs(minus.get(minus.size() - 2) + minus.get(minus.size() - 1))) {
					ans[0] = minus.get(minus.size() - 2);
					ans[1] = minus.get(minus.size() - 1);
					ans[2] = Math.abs(minus.get(minus.size() - 2) + minus.get(minus.size() - 1));
				}
			}
			
			for(int m : minus) {
				int p = -m;
				int right = binarySearch(p);
				
				if(right == 0) {
					if(ans[2] > Math.abs(m + plus.get(0))) {
						ans[0] = m;
						ans[1] = plus.get(0);
						ans[2] = Math.abs(m + plus.get(0));
					}
				}else if(right == plus.size() - 1) {
					if(ans[2] > Math.abs(m + plus.get(plus.size() - 1))) {
						ans[0] = m;
						ans[1] = plus.get(plus.size() - 1);
						ans[2] = Math.abs(m + plus.get(plus.size() - 1));
					}
				}else {
					if(ans[2] > Math.abs(m + plus.get(right))) {
						ans[0] = m;
						ans[1] = plus.get(right);
						ans[2] = Math.abs(m + plus.get(right));
					}
					if(ans[2] > Math.abs(m + plus.get(right - 1))) {
						ans[0] = m;
						ans[1] = plus.get(right - 1);
						ans[2] = Math.abs(m + plus.get(right - 1));
					}
				}
			}
		}
		
		
		System.out.println(ans[0] + " " + ans[1]);
		br.close();
	}

}