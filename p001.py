'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
'''


class Solution():
    def primalSum(self, max):
        sum = 0
        for x in range(0, max):
            if (x % 3) == 0 or (x % 5) == 0:
                sum += x
        return sum

    def optimizedSum(self, max):
        three_sum = 3 * (max // 3) * ((max // 3) + 1) // 2
        five_sum = 5 * (max // 5) * ((max // 5) + 1) // 2

        gcd = 15 * (max // 15) * ((max // 15) + 1) // 2

        total_sum = (three_sum + five_sum) - gcd

        print(total_sum)


test = Solution()
print(test.primalSum(1000))
print(test.optimizedSum(1000))
