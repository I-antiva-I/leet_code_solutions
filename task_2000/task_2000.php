# LeetCode #2000 | Reverse Prefix of Word | [EASY]

class Solution
{
    /**
     * @param String $word
     * @param String $ch
     * @return String
     */
    function reversePrefix($word, $ch) 
    {
        $stack = [];

        for ($i = 0; $i < strlen($word); $i++)
        {
            $stack[] = $word[$i];
            if ($word[$i] === $ch)
            {
                return implode('', array_reverse($stack)) . substr($word, $i+1);
            }
        }
        
        return $word;
    }
}