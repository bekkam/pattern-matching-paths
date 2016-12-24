# Pattern-Matching Paths 

## Problem 
### Description 

You've been given two lists: the first is a list of patterns, the second 
is a list of slash-separated paths. Your job is to print, for each path, 
the pattern which best matches that path. ("Best" is defined more 
rigorously below, under "Output Format".) 

A pattern is a comma-separated sequence of non-empty fields. For a 
pattern to match a path, every field in the pattern must exactly match 
the corresponding field in the path. (Corollary: to match, a pattern and 
a path must contain the same number of fields.) 

For example: the pattern `x,y` can only match the path `x/y`. Note, however, that leading and trailing slashes in paths should be ignored, thus `x/y` and `/x/y/` are equivalent. 

Patterns can also contain a special field consisting of a single 
asterisk, which is a wildcard and can match any string in the path. 
For example, the pattern `A,*,B,*,C` consists of five fields: three 
strings and two wildcards. It will successfully match the paths 
`A/foo/B/bar/C` and `A/123/B/456/C`, but not `A/B/C`, 
`A/foo/bar/B/baz/C`, or `foo/B/bar/C`. 

### Input Format 

The first line contains an integer, N, specifying the number of 
patterns. The following N lines contain one pattern per line. You may 
assume every pattern is unique. The next line contains a second integer, 
M, specifying the number of paths. The following M lines contain one 
path per line. Only ASCII characters will appear in the input. 

### Output Format 

For each path encountered in the input, print the best-matching 
pattern. The best-matching pattern is the one which matches the path 
using the fewest wildcards. 

If there is a tie (that is, if two or more patterns with the same number 
of wildcards match a path), prefer the pattern whose leftmost wildcard 
appears in a field further to the right. If multiple patterns' leftmost 
wildcards appear in the same field position, apply this rule recursively 
to the remainder of the pattern. 

For example: given the patterns `*,*,c` and `*,b,*,` and the path 
`/a/b/c/`, the best-matching pattern would be `*,b,*`. 

If no pattern matches the path, print `NO MATCH`. 

### Submission Requirements 

You should submit a working program, runnable from a command line, that 
reads from standard input and prints to standard output. In Unix 
parlance, for example, it should be runnable like this: 

`cat input_file | python your_program.py > output_file `

Of course, the actual command line may vary depending on the language 
you choose; your program file need not be executable on its own. 
However, it must read input directly from stdin and print to stdout. 

You may write your program in any of the following languages: 
JavaScript (Node.js) 
Python (2.7 or 3.x) 

### Extra Credit 
What's the algorithmic complexity of your program? In other words, how 
does its running time change as the number of patterns or number of 
paths increases? 

Would your program complete quickly even when given hundreds of 
thousands of patterns and paths? Is there a faster solution? 

Hint: although a correct program is sufficient, there is extra credit 
for an algorithm that's better than quadratic. Some of our test cases 
are very large. To pass them all, your program will need to be pretty 
fast! 

Example Input 
`6 `

`*,b,* `

`a,*,*` 

`*,*,c `

`foo,bar,baz `

`w,x,*,* `

`*,x,y,z `

`5 `

`/w/x/y/z/ `

`a/b/c `

`foo/ `

`foo/bar/ `

`foo/bar/baz/ `


Example Output 

`*,x,y,z `

`a,*,* `

`NO MATCH `

`NO MATCH `

`foo,bar,baz `

### Tips 

- Code correctness and quality matter more to us than algorithmic wizardry. Is your program easy to understand? Is it clearly organized and documented? Does it correctly handle all the edges cases? Imagine you are writing a library for other developers to use. How would that affect your design? 

- Your program's output must precisely match the expected output. Don't print extraneous or superfluous stuff to stdout. 

- The example input and output provided above fail to cover a large number of edge cases. To be sure your program is correct, you may want to supplement it with your own test cases. 

- Every line in the input ends with a Unix-style newline ("\n"). DOS-style CRLFs ("\r\n") are not used. 

- Each line in the output should end with a newline character (that includes the final one). As with the input, use Unix-style newlines.

## Solution

### Instructions
To run program, from the command line, type:
`cat input_file.txt | python pattern_matching_paths_final.py > output_file` 
This assumes you are in the same directory that houses `input_file.txt` (per the example in the instructions).

### Runtime
Big O notation looks at the efficiency of algorithms.
Here, the worst case runtime is likely searching for a matching pattern for each path.

If the number of paths is n, and the number of patterns is m, then I would guess the runtime is:
n (for path in paths) * m (for pattern in patterns of matching field count) * m (pattern.split) * [n * m] (because in order to test if 2 strings are identical, python must test each character in each string)

The program uses a nested dictionary to store patterns by field count (outer key) and by number of wilds (inner key).  By using a nested dictionary, the program avoids searching every pattern for each path - it only searches patterns of the requisite field count for each path, and it searches patterns in order of least number of wilds first.  

To minimize memory demands and improve performance, the program also makes use of itertools.  
### Assumptions
This program assumes ascii characters 0-41 wont appear in file names.  I'm not altogether clear on what characters are invalid across operating systems (I use windows, cygwin/posix, and mac osx so.. it's a bit murky), but it seems reasonable to assume such special characters wouldn't be valid filenames.

### Improvements
With more time, I would write tests for all of the above methods.  Alas, this code challenge arrived in the middle of an already jam-packed week, so I was not able to include these improvements.  