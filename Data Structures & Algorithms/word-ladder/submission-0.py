class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        visited = {beginWord}
        q = deque([(beginWord, 1)])

        while q:
            cur_word, count = q.popleft()
            if cur_word == endWord:
                return count

            for i in range(len(cur_word)):
                for ch in "abcdefghijklmnopqrstuvwxwyz":
                    new_word = cur_word[:i]+ch+cur_word[i+1:]
                    if new_word in words and new_word not in visited:
                        q.append((new_word, count + 1))
                        visited.add(new_word)

        return 0


        