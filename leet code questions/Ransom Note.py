"""
QUESTION:  Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

#SOLUTION:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote)==0 or len(magazine)==0) or (len(magazine)<len(ransomNote)):  #checking if given swtrings are empty and checking the length of magazine not less than the length of ransomNote 
            return False
        else:
            s_len = len(ransomNote)
            ans = True
            for j in range(0,len(ransomNote)):
                if(ransomNote[j] not in magazine):    # inding weather every charecter pressent in ransomNote is present in magazine or not , if not returning false
                    return False
                elif(magazine.count(ransomNote[j])<ransomNote.count(ransomNote[j])):   #checking the number of repeated characters present in ransomeNote are greater than the magazine , if not return false
                    return False
        return True  # finally returning true
