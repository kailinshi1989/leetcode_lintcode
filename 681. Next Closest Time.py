class Solution(object):
    def nextClosestTime(self, time):
        list = []
        for c in time:
            if c != ':' and int(c) not in list:
                list.append(int(c))
        list = sorted(list)

        result = time

        for i in xrange(len(result) - 1, -1, -1):
            if result[i] == ':':
                continue
            num = int(result[i])
            pos = list.index(num)
            if pos == len(list) - 1:
                result = result[:i] + str(list[0]) + result[i + 1:]
            else:
                next = list[pos + 1]
                if i == 4 and next <= 9:
                    result = result[:i] + str(next) + result[i + 1:]
                    return result
                elif i == 3 and next <= 5:
                    result = result[:i] + str(next) + result[i + 1:]
                    return result
                elif i == 1 and ((result[i - 1] != '2' and next <= 9) or
                                 (result[i - 1] == '2' and next <= 4)):
                    result = result[:i] + str(next) + result[i + 1:]
                    return result
                elif i == 0 and next <= 2:
                    result = result[:i] + str(next) + result[i + 1:]
                    return result
                result = result[:i] + str(list[0]) + result[i + 1:]
        return result