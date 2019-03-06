#!/bin/sh

sort 045_result.txt | uniq --count | sort --numeric-sort --reverse > "045_all.txt"
grep "^する\s" 045_result.txt | sort | uniq --count | sort --numeric-sort --reverse > "045_する.txt"
grep "^見る\s" 045_result.txt | sort | uniq --count | sort --numeric-sort --reverse > "045_見る.txt"
grep "^与える\s" 045_result.txt | sort | uniq --count | sort --numeric-sort --reverse > "045_与える.txt"