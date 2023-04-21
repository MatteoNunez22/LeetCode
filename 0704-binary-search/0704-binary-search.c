int search(int* nums, int numsSize, int target){
    
    int l = 0;
    int r = numsSize - 1;
    int mid;
    
    while (l <= r) {
        mid = (r + l) / 2;
        if (nums[mid] < target) {
            l = mid + 1;
            
        } else if (nums[mid] > target) {
            r = mid - 1;
            
        } else {
            return mid;
        }
    }
    
    return -1;
}