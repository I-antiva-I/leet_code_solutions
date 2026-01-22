# LeetCode #1957 | Delete Characters to Make Fancy String | [EASY]

class Solution
{

    /**
     * @param String $s
     * @return String
     */
    function makeFancyString($s) 
    {
        if (strlen($s) < 3) {return $s;};

        $stack = [$s[0], $s[1]];
        $prevprev = $s[0];
        $prev = $s[1];

        for ($i = 2; $i < strlen($s); $i++)
        {
            if (($s[$i] == $prev) && ($s[$i] == $prevprev)) {continue;}
            else
            {
                $stack[] = $s[$i];
                $prevprev = $prev;
                $prev = $s[$i];
            }
        }

        return implode('', $stack); 
    }
}