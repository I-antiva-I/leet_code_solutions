# LeetCode #1523 | Count Odd Numbers in an Interval Range | [EASY]

class Solution 
{

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countOdds($low, $high)
    {
        return intdiv(($high - $low + 1), 2) + ($high % 2) * ($low % 2);
    }
}