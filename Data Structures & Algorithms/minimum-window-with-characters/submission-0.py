class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {} #what t requires
        windowCount = {} #whats currently inside our window in S

        r = 0
        l = 0

        smallest = float("inf") #smallest valid window we have found
        result = [-1, -1] #stores l and r of smallest window

        have = 0 #how many char requirements from t have we satisfied
        need = 0 #number of unique character requirements
        #have == need = current window is valid

        #going thru t
        while r < len(t):
            count[t[r]] = count.get(t[r], 0) + 1
            r += 1

        r = 0
        need = len(count) #number of keys in count, how many unique char requirements

        #going thru s
        while r < len(s):
            
            #add current char in s to our window
            windowCount[s[r]] = windowCount.get(s[r], 0) + 1

            #did the char i added fulfil the req?
            if s[r] in count and windowCount[s[r]] == count[s[r]]:
                have += 1

            #if current window is valid, try making it smaller
            while have == need:
                currentLength = r - l + 1

                #if current window is smaller than our smallest, save it
                if currentLength < smallest:
                    smallest = currentLength
                    result = [l, r] #stores the pointers for the smallest window size

                #remove the left char from our window
                windowCount[s[l]] = windowCount.get(s[l], 0) - 1

                #check if removing left char broke one of our requirements
                if s[l] in count and windowCount[s[l]] < count[s[l]]:
                    have -= 1

                #move left pointer to make window smaller
                l += 1

            #move right pointer to keep searching thru s
            r += 1

        #if smallest never changed, we never found a valid window
        if smallest == float("inf"):
            return ""

        #return the substring between the saved l and r pointers
        return s[result[0]:result[1] + 1]