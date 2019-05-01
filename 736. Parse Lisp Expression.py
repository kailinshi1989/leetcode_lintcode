# "(let x 2 (mult x 5))"
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        d = {}
        curExpr = ['']
        parentExpr = []

        def evaluate(curExpr):
            if curExpr[0] in ('add', 'mult'):
                tmp = map(int, map(getVal, curExpr[1:]))
                return str(tmp[0] + tmp[1] if curExpr[0] == 'add' else tmp[0] * tmp[1])
            else: #let
                for i in range(1, len(curExpr) - 1, 2):
                    if curExpr[i + 1]:
                        d[curExpr[i]] = getVal(curExpr[i + 1])
                return getVal(curExpr[-1]) # 不需要let赋值，直接返回最后一个数

        def getVal(x):
            return d.get(x, x)

        for c in expression:
            if c == '(':
                if curExpr[0] == 'let':
                    evaluate(curExpr)
                parentExpr.append((curExpr, dict(d))) # dict深度拷贝
                curExpr = ['']
            elif c == ' ':
                curExpr.append('')
            elif c == ')':
                val = evaluate(curExpr)
                curExpr, d = parentExpr.pop()
                curExpr[-1] += val
            else:
                curExpr[-1] += c
        return int(curExpr[0])