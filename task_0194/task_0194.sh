# LeetCode #0194 | Transpose File | [MEDIUM]

# NR - variable indicating the number of records (current line number) that's accumulated across multiple files read.
# FNR is similar to NR, but is reset for each file read.
# NF - a variable indicating the number of fields (number of "columns") on an input line.

awk '{
    for (i = 1; i <= NF; i++) 
    {
        if (NR == 1) {
            table[i] = $i;
        }
        else 
        {
            table[i] = table[i] " " $i
        }
    }
}
END {
    for (i = 1; table[i] != ""; i++) 
    {
        print table[i]
    }
}
' file.txt
