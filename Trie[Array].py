## Trie Implementation using array, Only lowercase charater(s) are allowed in input
## Use insert(string) function to insert string in trie
## Use search_prefix(string) to search prefix in trie

class Trie_Node:
    def __init__(self):
        self.Arr = [False]*26
        self.stop = False

    def __str__(self):
        return str(self.Arr)

Root = Trie_Node()

def insert(string,weight):
    current = Root
    current.weight = weight
    for c in string:
        i = ord(c)-97
        if current.Arr[i] == False:
            current.Arr[i] = Trie_Node()
        current = current.Arr[i]
        current.weight = weight
    current.stop = True

def get_rec(current,string,stack,ans):
    if current.stop:
        ans.append(''.join(stack))
    n = 0
    for i in current.Arr:
        if i == False:
            pass
        else:
            stack.append(chr(n+97))
            get_rec(i,string,stack,ans) 
        n+=1
    return stack.pop(-1)   

def search_prefix(string):
    string = string.lower()
    current = Root
    stack = []
    for c in string:
        i = ord(c)-97
        if current.Arr[i] == False:
            return False;
        current = current.Arr[i]
        stack.append(c)
    ans = []
    get_rec(current,string,stack,ans)
    return ans;
    
if __name__ == "__main__":
    S = 'Trie is an efficient information reTrieval data structure Using Trie search complexities can be brought to optimal limit If we store keys in binary search tree a well balanced BST will need time proportional to'
    S = S.lower().split()
    for i in S:
        insert(i,10)
    print(search_prefix('ef'))
