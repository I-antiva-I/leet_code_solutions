# LeetCode #1656 | Design an Ordered Stream | [EASY]

class OrderedStream
{
    private array $values;
    private int $size;
    private int $streamStart;

    /**
     * @param Integer $n
     */
    function __construct($n)
    {
        $this->values = array();
        $this->values = array_fill(0, $n, null);
        $this->size = $n;
        $this->streamStart = 0;
    }
  
    /**
     * @param Integer $idKey
     * @param String $value
     * @return String[]
     */
    function insert($idKey, $value) 
    {
        $this->values[$idKey-1] = $value;
        $result = [];

        if ($idKey-1 == $this->streamStart) 
        {
            for ($i = $idKey-1; $i < $this->size; $i++)
            {   
                if ($this->values[$i] !== null)
                {
                    array_push($result, $this->values[$i]);
                }
                else
                {
                    $this->streamStart = $i;
                    break;
                }
            }
        }
       
        return $result;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * $obj = OrderedStream($n);
 * $ret_1 = $obj->insert($idKey, $value);
 */