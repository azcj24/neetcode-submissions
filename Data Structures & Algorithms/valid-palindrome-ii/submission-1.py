class Solution:
    def validPalindrome(self, s: str) -> bool:
        # indicate where to start left and right
        l = 0
        # index starts at 0 , e.g. s = cars 
        # index is 0c,1a,2r,3s
        # if you just get len(s) it will give you 4, but there is no index 4 in cars
        # that's why you need -1 to make 4-1 to give you index 3
        r = len(s) -1
        # create a loop until it is met
        while l < r:
            # how to move down the string if the left and right character do not match
            if s[l] != s[r]:
                skip_l = s[l+1:r+1] #[1:5]
                skip_r = s[l:r] #[0:5]
            #we want to include the position of r so we have to r+1 otherwise it will stop before r 
                # check if it matches/ palindrome or not
                return (skip_l == skip_l[::-1]) or (skip_r == skip_r[::-1])
             # if doesnt match skip the if block and move the pointers to run the loop again
            l = l+1
            r = r-1
            # return True because if l and r has met each other it is a palindrome,
            # otherwise it wouldnt have met
        return True
        

        

       
        
        
