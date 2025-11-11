# LeetCode #2739 | Total Distance Traveled | [EASY]

class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """

        # First addition happens on 5 consumed, other on 4 consumed (because 1 is refilled)
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10

        # (+) Alternative solution
        """
        distance = 0
        usedFuel = 0

        while (mainTank != 0):
            mainTank -= 1
            usedFuel += 1
            distance += 10
           
            if ((usedFuel == 5) and (additionalTank != 0)):
                usedFuel = 0
                additionalTank -= 1
                mainTank += 1
        
        return distance
        """