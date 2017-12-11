class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length - 1;
        qs(nums, 0, n);   
    }
    
    private void qs(int[] nums, int p, int r){
        if (p < r){
            int q = patition(nums, p, r);
            qs(nums, p, q-1);
            qs(nums, q+1, r);
        }
    }
    
    private int patition(int[] nums, int p, int r){
        System.out.print(r);
        int x = nums[r];
        int i = p-1;
        for (int j=p; j<r; j++){
            if (nums[j] < x){
                i = i + 1;
                swap(nums, i, j);
            }    
        }
        swap(nums, i+1, r);
        return i+1;
    }
    
    private void swap(int[] nums, int a, int b){
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
