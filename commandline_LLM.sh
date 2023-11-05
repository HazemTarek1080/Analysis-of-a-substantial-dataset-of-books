
echo -e "id title total_books_count"
jq -r 'select(.id and .title and .works) | {id: .id, title: .title, total_books_count: (.works | map(.books_count | tonumber) | add)}' series.json | \
    jq -s 'sort_by(-.total_books_count) | .[:5] | .[] | "\(.id)|\(.title)|\(.total_books_count)"' | sed 's/"//g' | column -t -s "|"