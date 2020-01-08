# Read from the file file.txt and output all valid phone numbers to stdout.
"""
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.
You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
You may also assume each line in the text file must not contain leading or trailing white spaces.
"""

# Memory Usage: 3.1 MB - all equal

# Runtime: 8 ms
egrep -x '(\([0-9]{3}\) [0-9]{3}\-[0-9]{4}|[0-9]{3}\-([0-9]){3}\-[0-9]{4})' file.txt

# Runtime: 8 ms
grep -w '\(^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}\)\|\(^([0-9]\{3\})\s[0-9]\{3\}\-[0-9]\{4\}\)' file.txt

# Runtime: 0 ms
grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt

# Runtime: 0 ms
grep '^\(([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}\|[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}\)$' file.txt