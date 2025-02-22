class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        circleStudentsCount, squareStudentsCount = 0, 0

        for i in students:
            if i == 0:
                circleStudentsCount += 1
            else:
                squareStudentsCount += 1
        
        for s in sandwiches:
            if s == 0 and circleStudentsCount == 0:
                return squareStudentsCount
            
            if s == 1 and squareStudentsCount == 0:
                return circleStudentsCount

            if s == 0:
                circleStudentsCount -= 1
            else:
                squareStudentsCount -= 1
            
        return 0