class Eertree:
    def __init__(self, s):
        self.s = s
        n = len(s)
        # nodes: each node = dict {next: {}, length: int, sufflink: int}
        self.nodes = [{'next': {}, 'len': -1, 'suff': 0}, {'next': {}, 'len': 0, 'suff': 0}]
        self.num = 2
        self.suff = 1  # current max suffix palindrome (index)
        for i, ch in enumerate(s):
            self._add_letter(i)

    def _add_letter(self, pos):
        ch = self.s[pos]
        cur = self.suff
        while True:
            curlen = self.nodes[cur]['len']
            if pos - 1 - curlen >= 0 and self.s[pos - 1 - curlen] == ch:
                break
            cur = self.nodes[cur]['suff']
        if ch in self.nodes[cur]['next']:
            self.suff = self.nodes[cur]['next'][ch]
            return
        # create new node
        self.nodes.append({'next': {}, 'len': self.nodes[cur]['len'] + 2, 'suff': 0})
        self.num += 1
        new_idx = self.num - 1
        self.nodes[cur]['next'][ch] = new_idx
        if self.nodes[new_idx]['len'] == 1:
            self.nodes[new_idx]['suff'] = 1
            self.suff = new_idx
            return
        # set suffix link for new node
        temp = self.nodes[cur]['suff']
        while True:
            if pos - 1 - self.nodes[temp]['len'] >= 0 and self.s[pos - 1 - self.nodes[temp]['len']] == ch:
                self.nodes[new_idx]['suff'] = self.nodes[temp]['next'][ch]
                break
            temp = self.nodes[temp]['suff']
        self.suff = new_idx

    def distinct_palcount(self):
        # exclude the two root nodes
        return self.num - 2

# Example
if __name__ == "__main__":
    s = "ababa"
    t = Eertree(s)
    print("Distinct palindromic substrings:", t.distinct_palcount())  # a, b, aba, bab, ababa => 5
