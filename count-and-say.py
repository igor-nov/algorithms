"""
Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221


Examples:
https://brilliant.org/wiki/look-and-say-sequence/
https://www.youtube.com/watch?v=_1Wp4Bww8Rs !!!
https://www.geeksforgeeks.org/look-and-say-sequence/
https://leetcode.com/problems/count-and-say/discuss/16044/Simple-Python-Solution
https://leetcode.com/problems/count-and-say/discuss/16471/9-line-solution-in-python - itertools.groupby
https://www.dcode.fr/conway-sequence
https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions

Runtime: 24 ms, faster than 90.32% of Python online submissions for Count and Say.

"""
class Solution(object):
    
     def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            res = '11'
            step = 2
            
            while step < n:
                cnt = 1
                tmp = ''
                res +='#' #extend boundaries in order to get last chank and go out of the range
                
                for i in xrange(1, len(res)):  
                    #print  i, res[i]                                        
                    if res[i-1] != res[i]:
                        #print 'lo %s res[lo] %s' % (lo, res[lo])
                        #print lo
                        #print '----'
                        #tmp += '%s%s' % (i-lo, res[lo])
                        tmp += '%s%s' % (cnt, res[lo])
                        #print 'tmp %s' % tmp
                        lo = i                        
                        cnt = 1
                    else:
                        cnt += 1                        
                        
                res = tmp                
                step += 1
 
            #print 'res %s' %res            
            return res
        
        
inp = 4
#Output: "1211"

inp = -1
#Output: 1

# inp = 1
# #Output: 1

# inp = 34
# #Output: "132113213221133112132123123112111311222112132113311213211231232112311311222112111312211311123113322112132113212231121113112221121321132132211231232112311321322112311311222113111231133221121113122113121113221112131221123113111231121123222112132113213221133122112231131122211211131221131112311332211213211321322113311213212322211231232112311321322112311311222113311213212322211231131122211311123113321112131221123113111231121123222112111312211312111322212321121113122113221113122112132113121113222112311311221112131221123113112211322112211213322112132113213221133112132123123112111312111312212231131122211311123113322112111312211312111322111213122112311311123112112322211213211321322113311213212312311211131122211213211331121321122112133221123123211231132132211231131122211331121321232221123113112221131112311322311211131122211213211331121321122112133221123113112221131112311332111213122112311311123112111331121113122112132113121113222112311311221112131221123113112211322112211213322112111312211312111...

# inp = 10
# inp = 6
# #"13211311123113112211"

res = Solution().countAndSay(inp)
print res
