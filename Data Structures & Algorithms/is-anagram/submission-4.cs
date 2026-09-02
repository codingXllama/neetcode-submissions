public class Solution {
    public bool IsAnagram(string s, string t) {
    //   if (s.Length != t.Length)
    //   {
    //     return false;
    //   }
    //   else {
    //     char[] sArray  = s.ToCharArray();
    //     char[] tArray =  t.ToCharArray();
    //     Array.Sort(sArray);
    //     Array.Sort(tArray);
    //     string sortedA=new string(sArray);
    //     string sortedB= new string (tArray);
    //     if (sortedA != sortedB)
    //     {
    //       return false;
    //     }

    //   }
    //   return true;
    // 

    if (s.Length != t.Length) return false;
    else
    {
        char[] firstStringArray = s.ToCharArray();
        char[] secondStringArray = t.ToCharArray();

        //Sorting both arrays
        Array.Sort(firstStringArray);
        Array.Sort(secondStringArray);
        int i;
        for (i = 0; i < firstStringArray.Length; i++)
        {
            if (firstStringArray[i] != secondStringArray[i]) return false;

        }

    }
    return true;

    }


}
