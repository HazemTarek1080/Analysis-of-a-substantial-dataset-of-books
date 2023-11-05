# prints a header row for the output 
echo "id  title  total_books_count"  

# reads series.json file, extract each record of the JSON and for each record create a new object with id, title and total_books_count by summing the books_count values from the works array
# then it joins the values using "|" as delimiter
cat series.json | jq -s -r '.[] | {id: .id, title: .title, total_books_count: [(.works[] | .books_count | tonumber)] | add} | [.id, .title, .total_books_count] | join(";")' |               

# sort in descending order by the 3rd element (total_books_count)  using ";" as field separator
sort -t ";" -k3 -nr | 

 # extract the first 5 
head -n 5 |

# formatting output into columns, always using ";" as delimiter"
column -t -s ";" 

