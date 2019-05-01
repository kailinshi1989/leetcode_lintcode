"""
假设从站点 i 出发，到达站点 k 之前，依然能保证油箱里油没见底儿，从k 出发后，见底儿了。
那么就说明 diff[i] + diff[i+1] + ... + diff[k] < 0，而除掉diff[k]以外，从diff[i]开始的累加都是 >= 0的。
也就是说diff[i] 也是 >= 0的，这个时候我们还有必要从站点 i + 1 尝试吗？
仔细一想就知道：车要是从站点 i+1出发，到达站点k后，甚至还没到站点k，油箱就见底儿了，因为少加了站点 i 的油。。。

因此，当我们发现到达k 站点邮箱见底儿后，i 到 k 这些站点都不用作为出发点来试验了，肯定不满足条件，
只需要从k+1站点尝试即可！因此解法时间复杂度从O(n2)降到了 O(2n)。之所以是O(2n)，
是因为将k+1站作为始发站，车得绕圈开回k，来验证k+1是否满足。
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas) - 1
        end = 0
        total = gas[start] - cost[start]
        while end < start:
            if total < 0:
                start -= 1
                total += gas[start] - cost[start]
            else:
                total += gas[end] - cost[end]
                end += 1
        return start if total >= 0 else -1
