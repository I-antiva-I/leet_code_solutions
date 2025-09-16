# LeetCode #0195 | Tenth Line | [EASY]

### Soulution #1 ###
# awk 'NR==10 {print; exit}' file.txt

### Soulution #2 ### 
sed -n '10p' file.txt

### Soulution #3 ###
: <<COMMENT
count=0
input_file="file.txt"

while IFS= read -r line; do
  ((count++))
  if [[ $count -eq 10 ]]; then
    echo "$line"
    break
  fi
done < "$input_file"
COMMENT

### WON'T WORK ###
# head -n 10 "file.txt" | tail -n 1