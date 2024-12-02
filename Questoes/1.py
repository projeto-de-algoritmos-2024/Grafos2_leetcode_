public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] z = new int[2];
        for(int x=0;x < nums.Length; x++){
            for(int y=0;y < nums.Length;y++){
                if(x!=y){
                    if(nums[x]+nums[y]==target){
                        z[0]=x;
                        z[1]=y;
                    } 
                }
            }
        }
        return z;
    }
}
