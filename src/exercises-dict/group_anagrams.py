# =============================================================================
# Functions
# =============================================================================

def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Function that groups the anagrams in the array together using a hash table (dictionary).

    Args:
        strings (list[str]): input list of strings to group anagrams.

    Returns:
        list[list[str]]: list of lists of strings that are anagrams of each element list. 
    """
    anagram_dict = {}
    
    for string in strings:
        count = [0] * 26
        for char in string:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        anagram_dict[key] = anagram_dict.get(key, []) + [string]
        
    return list(anagram_dict.values())