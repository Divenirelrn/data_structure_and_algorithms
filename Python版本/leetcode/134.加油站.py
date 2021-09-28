class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        i = 0
        while i < n:
            step = 0
            sumofgas, sumofcost = 0, 0

            while step < n:
                j = (i + step) % n
                sumofgas += gas[j]
                sumofcost += cost[j]
                if sumofgas < sumofcost:
                    break

                step += 1

            if step == n:
                return i
            else:
                i = i + step + 1

        return -1