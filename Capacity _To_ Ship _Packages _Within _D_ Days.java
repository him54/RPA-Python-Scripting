import java.util.*;
class Solution {
    public static boolean PossibleCase(int[] weights, int mid, int days){
        int n = weights.length;
        int day = 1;
        int sum = 0;
        for(int i = 0; i<n; i++)
        {
            sum += weights[i];
            if(sum > mid)
            {
                day++;
                sum = weights[i];
            }
        }
        return day <= days;
    }
    public int shipWithinDays(int[] weights, int days) {
        int n = weights.length;
        int max = 0;
        int sum = 0;
        for(int weight : weights)
        {
           sum += weight;
           max = Math.max(max, weight);
        }
        
        if(n == days)
        {
            return max;
        }
        int low = max; // Set the limit
        int high = sum;
        int res = 0;
        while(low <= high) // Binary search 
        {
            int mid = low +  (high - low) / 2; //The calculation is modified to avoid integer overflow errors.
            if(PossibleCase(weights, mid, days) == true)
            {
                res = mid;
                high = mid - 1; // low will be decrease
            }
            else
            {
                low = mid + 1; // low will be increase
            }
        }
        return res;
    }
}
