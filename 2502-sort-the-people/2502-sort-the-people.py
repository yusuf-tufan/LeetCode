class Solution(object):
    def sortPeople(self, names, heights):
        new_list=[]
        for k,v in zip(names,heights):
            new_list.append({k:v})
        sorted_dict=sorted(new_list,key= lambda d: list(d.values())[0],reverse=True)
        new_names=[]
        for i in range(len(sorted_dict)):
            for x in sorted_dict[i].keys():
                new_names.append(x)
        return new_names
