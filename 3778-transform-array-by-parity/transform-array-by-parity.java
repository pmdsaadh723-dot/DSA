class Solution {
    public int[] transformArray(int[] nums) {
        int[] r = new int[nums.length];
        int rp = r.length-1;
        for(int c : nums) {
            if(c % 2 == 1) r[rp--] = 1;
        }
        return r;
    }
}