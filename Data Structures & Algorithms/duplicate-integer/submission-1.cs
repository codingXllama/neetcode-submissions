public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> Collection =new HashSet<int>();
        
      foreach (int item in nums)
    {
        if (Collection.Contains(item))
        {
            return true;
        }
        else
        {
            Collection.Add(item);
        }
    }

    return false;




        

return false;
    }
}