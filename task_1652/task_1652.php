# LeetCode #1652 | Defuse the Bomb | [EASY]

class Solution {

    /**
     * @param Integer[] $code
     * @param Integer $k
     * @return Integer[]
     */
    function decrypt($code, $k) 
    {
        $remember = $code;
        $n = count($code);

        for ($i = 0; $i < $n; $i++)
        {
            $code[$i] = 0;
            
            if ($k > 0)
            {
                for ($j = 1; $j <= $k; $j++)
                {
                    $code[$i] += $remember[(($i + $j) % $n)];
                }
            }
            if ($k < 0)
            {
                for ($j = 1; $j <= -$k; $j++)
                {   
                    $code[$i] += $remember[($n + $i - $j) % $n];
                }
            }
        }

        return $code;
    }
}