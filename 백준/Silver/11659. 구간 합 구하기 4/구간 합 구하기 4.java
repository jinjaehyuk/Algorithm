import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int arr[] = new int[n];
        int dp[] = new int[n+1];
        int sum = 0;
        for(int i=0; i<arr.length; i++){
            arr[i] = sc.nextInt();
            sum += arr[i];
            dp[i+1] = sum;
        }
        for(int k =0; k<m; k ++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            System.out.println(dp[j] - dp[i-1]);
        }
    }
} 