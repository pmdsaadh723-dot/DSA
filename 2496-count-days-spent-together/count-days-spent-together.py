class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        start = max(self.countDays(arriveAlice), self.countDays(arriveBob))
        end = min(self.countDays(leaveAlice), self.countDays(leaveBob))

        return max(0, end - start + 1)

    def countDays(self, date):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(date[:2])
        day = int(date[3:])
        dayCount = 0

        for i in range(month - 1):
            dayCount += days[i]

        return dayCount + day


# i/p:arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# o/p:3
# i/p:arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# o/p:0