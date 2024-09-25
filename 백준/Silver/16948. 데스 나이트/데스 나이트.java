import java.util.*;
import java.io.*;

public class Main {
    static int ey;
    static int ex;
    static int[][] graph;
    static int[] dy = {2,2,0,0,-2,-2}; static int[] dx = {1,-1,2,-2,1,-1};
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        graph = new int[N][N];

        st = new StringTokenizer(br.readLine());
        int sy = Integer.parseInt(st.nextToken());
        int sx = Integer.parseInt(st.nextToken());
        ey = Integer.parseInt(st.nextToken());
        ex = Integer.parseInt(st.nextToken());

        bfs(sy,sx);
    }

    static void bfs(int a, int b){
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {a,b});

        while(!q.isEmpty()) {
            int[] now = q.poll();
            int y = now[0];
            int x = now[1];

            if (y == ey && x == ex) {
                System.out.println(graph[ey][ex]);
                return;
            }

            for (int i = 0; i < 6; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= ny && ny < graph.length && 0 <= nx && nx < graph.length && graph[ny][nx] == 0) {
                    q.offer(new int[]{ny, nx});
                    graph[ny][nx] = graph[y][x] + 1;
                }
            }
        }
        System.out.println(-1);
    }
}