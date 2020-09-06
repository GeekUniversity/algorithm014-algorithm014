from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        all_list = defaultdict(list)
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                all_list[word[:i] + "*" + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(length):
                intermid_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in all_list[intermid_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        queue.append((word, level + 1))
                        visited[word] = True
                all_list[intermid_word] = []
        return 0