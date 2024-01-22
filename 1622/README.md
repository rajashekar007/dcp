This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".



Solution:

We can do a sliding window, where we increase the window size from right till we see at most k unique characters & we shrink the window from the left if we go beyond k characters.