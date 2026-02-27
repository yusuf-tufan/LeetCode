class Solution(object):
    def generateTag(self, caption):
        captionList=caption.split()
        sentence='#'
        for i in range(len(captionList)):
            if i==0:
                sentence+=captionList[i].lower()
            else:
                sentence+=captionList[i].capitalize()
        if len(sentence)>100:
            sentence=sentence[:100]
        return sentence