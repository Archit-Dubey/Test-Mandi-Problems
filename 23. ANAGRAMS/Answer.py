from collections import defaultdict
 
def printAnagramsTogether(words):
    groupedWords = defaultdict(list)
 
    # Put all anagram words together in a dictionary
    # where key is sorted word
    for word in words:
        groupedWords["".join(sorted(word.upper()))].append(word)
 
    # Print all anagrams together
    groupedWords=list(groupedWords.values())
    for x in range(0,len(groupedWords)-1):
        print(groupedWords[x],end=" ")
    print(groupedWords[-1]) 
 
 
if __name__ == "__main__":  
    arr = input().strip().split()
    printAnagramsTogether(arr)

