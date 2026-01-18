# LeetCode #1544 | Make The String Great | [EASY]

class Solution
{
    /**
     * @param String $s
     * @return String
     */
    function makeGood($s)
    {
        $stack = [];
        $n = strlen($s);

        for ($i = 0; $i < $n; $i++)
        {
            $char = $s[$i];

            if (!empty($stack))
            {
                if (abs(ord(end($stack)) - ord($char)) == 32)
                {
                    array_pop($stack);
                    continue;
                }
            }

            $stack[] = $char;
        }

        return implode('', $stack);   
    }
}