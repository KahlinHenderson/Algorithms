# Let numCourses be the number of courses we want to take (courses 0,...,n-1) and let 
# prerequisites be a list of pairs where the oth value of the pair is a course we want to take
# and the 1st value of the pair is a prerequisite to that course. Write a function that 
# determines whether or not we can complete all of the courses. Note that if the function
# detects a cycle in the graph it is not possible to complete all of the courses.
def canFinish(numCourses, prerequisites):
    preMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    visitSet = Set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
            visitSet.remove(crs)
            preMap[crs] = []
        return True
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True
