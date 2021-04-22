'''
author: Md Omar Hasan
Interview Test
'''

from typing import List

class Solution:

    def findItnerary(self, tickets: List[List[str]]) -> List[str]:
        # here using the given list, the logic will iterate through the list and 
        # find the exact string to show the output
        final_list_output = []  # Initialize an empty list
        valid_string_append = '' # Initialize an empty string
        for i in range(len(tickets)):
            # check if the strings are smaller by lexical order, if found 
            # then append to a new list
            # otherwise no action needed
            if tickets[i][0] < tickets[i][1] == False:
                valid_string_append = tickets[i][0]
                final_list_output.append(valid_string_append)
            elif tickets[i][0] == tickets[i][1]:
                #  if the condition is true, it will pass
                pass
            else:
                valid_string_append = tickets[i][0]
                final_list_output.append(valid_string_append)
        
        return final_list_output    # return the final list


list_of_words = [['MUN','MAD'], ['PAR','MUN'], ['SFO', 'SJC'], ['MAD', 'SFO']]

solve = Solution()

print(solve.findItnerary(list_of_words))    # Print the final output

