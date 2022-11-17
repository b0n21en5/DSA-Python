class stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        try:
            return self.arr.pop(-1)
        except:
                pass

    def top(self):
        try:
            return self.arr[-1]
        except:
            pass

    def size(self):
        return len(self.arr)

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class exp_tree:
    
    def __init__(self,postfix_exp):
        self.exp = postfix_exp
        self.root = None
        self.createTree(self.exp)

    def isOperator(self, char):
        optr = [' ', '-', '*', '/', '^']

        if char in optr:
            return True
        return False

    def createTree(self, exp):
        s = stack()

        self.root = node(exp[-1])

        s.push(self.root)

        for i in "".join(reversed(exp[:-1])):
            curr_node = s.top()
            if not curr_node.right:
                temp = node(i)
                curr_node.right = temp
                if self.isOperator(i):
                    s.push(temp)
            else:
                temp = node(i)
                curr_node.left = temp
                s.pop()
                if self.isOperator(i):
                    s.push(temp)

    def inOrder(self,head):
        if head.left:
            self.inOrder(head.left)
            
        print(head.data,end=" ")
        if head.right:
            self.inOrder(head.right)

    def infixExp(self):
        self.inOrder(self.root)
        print()


if __name__=="__main__":
    postfixExp = "ab ef*g*-"
    et = exp_tree(postfixExp)
    et.infixExp()