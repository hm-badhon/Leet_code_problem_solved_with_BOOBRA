# class Solution(object):
#     def findJudge(self,n, trust):
#         unique_items = set()
#         trust_Others = [fst_elmt[0] for fst_elmt in trust if fst_elmt[0] not in unique_items and not unique_items.add(fst_elmt[0])]
#         # print('trust_Others people ',trust_Others)
#         judge =[]
#         all_people = [i for i in range(1,n+1)]
#         # print('Number of all_ people',all_people)
#         for i in range(1,n+1):
#             if n == len(trust_Others):
#                 # print('Allthe people who trust each other')
#                 return -1 
#             else:
#                 for i in all_people:
#                     if i not in trust_Others: 
#                         # print('This is judge and also not trsut others',i)
#                         judge.append(i)
#             return judge[0]

# # Example usage:
# solution = Solution()
# n = 3
# # trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
# # trust =[[1,2]] 
# trust =[[1,3],[2,3]]
# # trust =  [[1,3],[2,3],[3,1]]
# result = solution.findJudge(n, trust)
# print(result)


class Solution(object):
    def findJudge(self, n, trust):
        trusted_count = [0] * (n + 1) 
        print(trusted_count) # Initialize an array to count how many people trust each person
        for a, b in trust:
            trusted_count[a] -= 1  # Decrement the count if a trusts someone
            trusted_count[b] += 1  # Increment the count if b is trusted by someone
        print(trusted_count)
        for i in range(1, n + 1):
            if trusted_count[i] == n - 1:  # Check if a person is trusted by all others
                return i
        
        return -1  # Return -1 if no judge is found

# Example usage:
solution = Solution()
n = 3
trust = [[1,2],[2,3]]
result = solution.findJudge(n, trust)
print(result)
