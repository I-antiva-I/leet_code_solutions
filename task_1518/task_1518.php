# LeetCode #1518 | Water Bottles | [EASY]

class Solution {

    /**
     * @param Integer $numBottles
     * @param Integer $numExchange
     * @return Integer
     */
    function numWaterBottles($numBottles, $numExchange) 
    {   
        $totalBottles = $numBottles + intdiv($numBottles-1, $numExchange-1);
        return $totalBottles;

        # (?) Alternative solution: simulation.
        /*
        $emptyBottles = 0;
        $totalBottles = 0;

        while($numBottles != 0)
        {
            $totalBottles += $numBottles;
            $emptyBottles += $numBottles;
            $numBottles = intdiv((int) $emptyBottles, (int) $numExchange);
            $emptyBottles = $emptyBottles % $numExchange;
        }

        return $totalBottles;
        */
    }
}