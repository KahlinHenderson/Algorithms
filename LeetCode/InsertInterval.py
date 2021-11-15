# Given an array of intervals insert a new interval into the array, merging
# whenever possible. Assume the intervals are sorted according to their 0th values.
def insert(intervals, newinterval):
    result = []
    i = 0
    while i < len(intervals) and newinterval[0] > intervals[i][1]:
        result += intervals[i]
        i += 1
    while i < len(intervals) and newinterval[1] > intervals[i][0]:
        newinterval = [min(newinterval[0], intervals[i][0]), max(newinterval[1],
                                           intervals[i][1])
                      ]
        i += 1
    result.append(newinterval)
    result.extend(intervals[i:])
    return result
