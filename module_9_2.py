first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#==============================================================================
first_result = [x for x in first_strings]
first_len = [len(x) for x in first_result if len(x) > 5]
#==============================================================================
second_result = [(first, second) for first in first_result for second in second_strings if len(first) == len(second)]
#==============================================================================
combo = first_strings + second_strings
third_result = [{stings: len(stings)} for stings in combo if len(stings) % 2 == 0]
#==============================================================================

print(first_len)
print(second_result)
print(third_result)