# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        maxArea = (right - left) * min(height[left], height[right])
        leftUpdated = False
        rightUpdated = False
        area = 0
        while left < right:
            if leftUpdated and height[left] > height[left - 1]:
                leftUpdated = False
                area = (right - left) * min(height[left], height[right])
            if rightUpdated and height[right] > height[right + 1]:
                rightUpdated = False
                area = (right - left) * min(height[left], height[right])
            if area > maxArea:
                maxArea = area
            if height[left] > height[right]:
                right -= 1
                rightUpdated = True
            else:
                left += 1
                leftUpdated = True
        return maxArea

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(obj.maxArea(heights))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
