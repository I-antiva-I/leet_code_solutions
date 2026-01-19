# LeetCode #1399 | Count Largest Group | [EASY]

class Solution 
{

    /**
     * @param Integer $n
     * @return Integer
     */
    function countLargestGroup($n)
    {

        $sum_groups = [];

        for ($i=1; $i<=$n; $i++)
        {
            $value = $i;
            $digit_sum = 0;

            while($value != 0)
            {
                $digit = $value % 10;
                $digit_sum += $digit;
                $value = intdiv($value, 10);
            }

            if (array_key_exists($digit_sum, $sum_groups))
            {
                array_push($sum_groups[$digit_sum], $i);
            }
            else
            {
                $sum_groups[$digit_sum] = [];
                array_push($sum_groups[$digit_sum], $i);
            }
        }

        $largest_sg = 0;
        $largest_sg_count = 0;

        foreach ($sum_groups as $sg)
        {
            if (sizeof($sg) > $largest_sg)
            {
                $largest_sg = sizeof($sg);
                $largest_sg_count = 1;
            }
            else if (sizeof($sg) == $largest_sg)
            {
                $largest_sg_count += 1;
            }
        }

        return $largest_sg_count;
    }
}