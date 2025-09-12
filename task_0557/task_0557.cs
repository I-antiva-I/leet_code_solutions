// LeetCode #0557 | Reverse Words in a String III | [EASY]

public class Solution
{ 
    public string ReverseWords(string s) 
    {
        char[] str = s.ToCharArray();
        int left = 0;

        for (int right = 0; right < s.Length; right++)
        {
            if ((s[right] == ' ') || (right+1 == s.Length))
            {   
                int offset = (right+1 == s.Length) ? 0 : 1;
                
                for (int pivot = 0; pivot < (right-offset-left) / 2 + (right-offset-left) % 2; pivot++)
                {
                    (str[left+pivot], str[right-pivot-offset]) =
                        (str[right-pivot-offset], str[left+pivot]);
                }

                left = right+1;
            }
        }
        
        return new string(str);
    }
}