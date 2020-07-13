class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur_node = self.root
        for ch in word:
            cur_node = cur_node.children[ch]
        cur_node.is_word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root

        def helper(node, _word, index):
            if index == len(_word):
                return node.is_word

            cur_node = node
            ch = _word[index]
            if ch == ".":
                for _node in cur_node.children.values():
                    if helper(_node, _word, index+1):
                        return True
                return False
            else:
                cur_node = cur_node.children.get(ch)
                if not cur_node:
                    return False
                return helper(cur_node, _word, index+1)

        return helper(cur_node, word, 0)
