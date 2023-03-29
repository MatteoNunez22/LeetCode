import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> reminders = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++) {
            int rem = target - nums[i];
            if (reminders.containsKey(rem)) {
                int[] array = {reminders.get(rem), i};
                return array;
            }
            reminders.put(nums[i], i);
        }
        
        return null;
    }
}