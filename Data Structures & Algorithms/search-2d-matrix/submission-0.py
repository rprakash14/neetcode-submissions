class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            subarr = matrix[mid]

            if target < subarr[0]:
                end = mid - 1
            
            elif target > subarr[-1]:
                start = mid + 1
            else:
                #in subarr, do bin search 
                start1 = 0
                end1 = len(subarr) - 1

                while start1 <= end1:
                    mid1 = (start1 + end1)//2

                    if target < subarr[mid1]:
                        end1 = mid1 - 1
                    elif target > subarr[mid1]:
                        start1 = mid1 + 1
                    elif target == subarr[mid1]:
                        return True
                return False
        return False

        