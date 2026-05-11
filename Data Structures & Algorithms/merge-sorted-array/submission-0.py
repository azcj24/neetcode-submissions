class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_last_index = m-1 #40
        nums2_last_index = n-1  #2
        total_last_index = (m+n) -1 #0

        # set 3 pointers that point at the last value of nums1 and nums2 (biggest)
        # and one point at nums1 last placeholder

        while nums2_last_index >= 0:
            # index cannot be smaller than 0
            # with nums1[nums1_last_index] is finding the nums1[position]'s value
            if nums1_last_index >= 0 and nums1[nums1_last_index] > nums2[nums2_last_index]:
                nums1[total_last_index] = nums1[nums1_last_index]
                nums1_last_index -= 1

            else:
                nums1[total_last_index] = nums2[nums2_last_index]
                nums2_last_index -= 1
            total_last_index -= 1
        # set loop so it stop when all done <>><



        