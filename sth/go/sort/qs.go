func sortColors(nums []int)  {
    n := len(nums) -1 
    qs(nums, 0, n)
    
}

func qs(nums []int, p, r int) {
    if p < r {
        q := partition(nums, p, r)
        qs(nums, p, q-1)
        qs(nums, q+1, r)
    }
}

func partition(nums []int, p, r int) int {
    x := nums[r]
    i := p-1
    
    for j:=p; j<r; j++ {
        if nums[j] < x {
            i++
            nums[i], nums[j] = nums[j], nums[i]
        }
    }
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i+1
    
}
