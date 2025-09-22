class Solution(object):
    def reformatDate(self, date):
        months=['',"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date=date.split()
        mon=f"{months.index(date[1])}"
        if int(mon)<10:
            mon='-0'+mon
        else:
            mon='-'+mon
        date[1]=mon
        new_d = ''.join(filter(str.isdigit, date[0]))
        if len(date[0])==3:
            new_d=new_d.zfill(2)
        date[0]='-'+new_d
        date=date[::-1]
        date=''.join(date)
        return date