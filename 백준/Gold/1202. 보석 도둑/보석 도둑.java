import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
	static class Dia implements Comparable<Dia>{
		int m;
		int v;
		@Override
		public int compareTo(Dia o) {
			return -Integer.compare(v, o.v);
		}
		public Dia(int m, int v) {
			super();
			this.m = m;
			this.v = v;
		}
		@Override
		public String toString() {
			return "" + "m:" + m + "/v:" + v;
		}
		
		
		
	}
	static int N, K;
	static long ans;
	static List<Dia> dias = new ArrayList<>();
	static TreeMap<Integer, Integer> bags = new TreeMap<>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken()); K = Integer.parseInt(st.nextToken());
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			dias.add(new Dia(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		
		for(int i = 0; i < K; i++) {
			int b = Integer.parseInt(br.readLine());
			if(bags.containsKey(b)) {
				bags.replace(b, bags.get(b) + 1);
			}else {
				bags.put(b, 1);
			}
		}
		dias.sort(new Comparator<Dia>() {

			@Override
			public int compare(Dia o1, Dia o2) {
				return -Integer.compare(o1.v, o2.v);
			}
			
		});
		int aa = 1;
		
		for(Dia d : dias) {
			Map.Entry<Integer, Integer> entry = bags.ceilingEntry(d.m);
			if(entry != null && entry.getValue() > 0) {
				ans += d.v;
				if(entry.getValue() == 1) {
					bags.remove(entry.getKey());
				}else {
					bags.replace(entry.getKey(), entry.getValue() - 1);
				}
			}
		}
		
		System.out.println(ans);
		br.close();
	}

}