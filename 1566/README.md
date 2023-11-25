This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana"


Solution:

It's a classic problem of Longest Common Substring between s & reverse(s).
or taking each character(s) as the center and checking how far on each side would match
to make it a palindrome
TimeComplexity: O(N^2)