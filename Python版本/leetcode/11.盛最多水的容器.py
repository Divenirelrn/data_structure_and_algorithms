class Solution:
    def maxArea(self, height: List[int]) -> int:
        len_h = len(height)
        l, r = 0, len_h - 1

        max_v = 0
        while l < r:
            v = min(height[l], height[r]) * (r - l)

            if v > max_v:
                max_v = v

            if height[l] <= height[r]:
                h = height[l]
                l += 1
                while l < len_h - 1 and height[l] <= h:
                    l += 1
            else:
                h = height[r]
                r -= 1
                while r > 0 and height[r] <= h:
                    r -= 1

        return max_v

"""
为什么移动短边没有意义：
    设x为左高度,y为右高度, x < y, t为二者之间的距离
    则 v = min{x, y} * t
    
    若x不动，y往左移一步，设新的高度为y_new, 新的距离为v_new
    则v_new = min{x, y_new} * v_new
    若 y_new <= y, 则 min{x, y_new} <= min{x, y} 
    (min{x, y} = x, 若y_new >= x, 则min{x, y_new} = x, 则min{x,y_new} = min{x, y};
    若y_new < x, 则min{x, y_new} = y_new < x = min{x, y})
    若y_new > y, 则 min{x, y_new} = x = min{x, y}
    
    而 t_new < t,
    因此 v_new < v, 保持低边不变，移动高边，没有意义
"""