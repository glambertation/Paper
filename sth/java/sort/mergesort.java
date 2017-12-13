class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length -1;
        mergesort(nums, 0, n);
    }
    
    private void mergesort(int[] nums, int p, int r){
        if (p < r){
            int q = (p + r)/2;
            mergesort(nums, p, q); // 这里是先拆到很小，再从小merging到大，和qs相反
            mergesort(nums, q+1, r);
            merging(nums, p, q, r);
        }
    }
    
    private void merging(int[] nums, int p, int q, int r){
        int l1 = q - p + 1;
        int l2 = r - q;

        int[] left = new int[l1+1];
        int[] right = new int[l2+1];
        
        int begin1 = 0;
        int begin2 = 0;
        for (int i = p; i <= q; i++){
            left[begin1] = nums[i];
            begin1++;
        }
        left[l1] = Integer.MAX_VALUE;
        for (int j = q+1; j <= r; j++){
            right[begin2] = nums[j];
            begin2++;
        }
        right[l2] = Integer.MAX_VALUE;
        
        int j = 0;
        int i = 0;
        int m = p;
        for (int k = p; k <= r; k++){
            if (left[i] < right[j]){
                nums[m] = left[i];
                m++;
                i++;
            }
            else{
                nums[m] = right[j];
                m++;
                j++;
            }
        }
        
        
    }
}
