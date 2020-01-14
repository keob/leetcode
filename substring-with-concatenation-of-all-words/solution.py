from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return list()

        from collections import defaultdict, deque, Counter

        s_len, word_len = len(s), len(words[0])
        words_total_len = word_len * len(words)
        loopring = defaultdict(deque)
        count = Counter(words)
        res = list()

        for start in range(word_len):
            loopring.clear()
            end = start

            while start + words_total_len <= s_len:
                word = s[end:end+word_len]
                end += word_len
                if word in count:
                    queue = loopring[word]
                    queue.append(end)
                    while queue[0] < start:
                        queue.popleft()
                    if len(queue) > count[word]:
                        start = queue.popleft()
                    if start+words_total_len == end:
                        res.append(start)
                else:
                    start = end

        return res
