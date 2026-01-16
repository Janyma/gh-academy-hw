class Scratch {
    public static void main(String[] args) {
        Solution singleNumber = new Solution();
        int a[] ={1, 7, 1, 2, 3, 2, 3};
        int result = singleNumber.singleNumber(a);
        System.out.println(result);
        
    }
}

class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int x : nums) {
            ans = ans ^ x;
        }
        return ans;
    }
}
