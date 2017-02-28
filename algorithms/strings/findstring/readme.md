# Find Strings (25 points)

You are given `n` strings w1, w2, ……, wn. Let Si denote the set of strings
formed by considering all unique substrings of the string wi. A substring is
defined as a contiguous sequence of one or more characters in the string. More
information on substrings can be found here. Let `S` = {S1 U S2 U …. Sn} .i.e
‘S’ is a set of strings formed by considering all the unique strings in all sets
S1, S2, ….. Sn. You will be given many queries and for each query, you will be
given an integer `k`. Your task is to output the lexicographically kth smallest
string from the set `S`.


## Input:

The first line of input contains a single integer ‘n’, denoting the number of
strings. Each of the next ‘n’ lines consists of a string. The string on the ith
line (1<=i<=n) is denoted by wi and has a length mi. The next line consists of
a single integer ‘q’, denoting the number of queries. Each of the next ‘q’
lines consists of a single integer ‘k’.

Note: The input strings consist only of lowercase english alphabets ‘a’ - ‘z’.


## Output:

Output ‘q’ lines, where the ith line consists of a string which is the answer
to the ith query. If the input is invalid (‘k’ >  S   ), output “INVALID”
(quotes for clarity) for that case.


## Constraints:

1<=n<=50
1<=mi<=2000
1<=q<=500
1<=k<=1000000000 
