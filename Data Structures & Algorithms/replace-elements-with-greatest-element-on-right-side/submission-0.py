class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        output = []
        for i in range(len(arr)-1):
            subarray = arr[i+1:len(arr)]
            output.append(max(subarray))
            print(subarray)
        
        print(output)

        output.append(-1)

        return output

        