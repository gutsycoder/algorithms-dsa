# Word Ladder II :- https://leetcode.com/problems/word-ladder-ii/description/

## Problem Description

Given two words, `beginWord` and `endWord`, and a dictionary word list, find all the shortest transformation sequences from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Return a list of all possible shortest transformation sequences. Each sequence should be a list of strings representing the transformation sequence.

**Note:**
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume `beginWord` and `endWord` are non-empty and are not the same.

## Example

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

## Algorithm

The problem can be solved using a Breadth-First Search (BFS) approach. The idea is to perform a level-order traversal of the possible word transformations starting from the `beginWord` and reaching the `endWord`. Keep track of the transformations at each level to find the shortest sequences. Additionally, use a hash set to efficiently check whether a word is present in the word list.

1. Create a word set from the given word list for quick word existence checking.
2. Perform BFS by starting with the `beginWord` and exploring all possible transformations.
3. Keep track of the visited words to avoid loops and cycles.
4. Once the `endWord` is reached, append one of the paths in the answer 
5. Return the list of all shortest transformation sequences.

