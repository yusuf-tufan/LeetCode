class Solution(object):
    def countNegatives(self, grid):
        new_list=[]
        for i in grid:
            for c in i:
                if c<0:
                    new_list.append(c)

        return len(new_list)