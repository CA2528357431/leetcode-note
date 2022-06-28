import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        heap = []
        time = 0
        # 目的在于让课程最多（得分），用时最少（为后续留出空间）
        for d,e in courses:
            # 考虑新课之前，最佳总时间是total
            if time+d<=e:
                time+=d
                heapq.heappush(heap, -d)
                # 加入该课程也能完成
            else:
                # 如果新课程无法直接插入
                if heap and heap[0]*(-1)>d:
                    # 如果就课程中最耗时的课比新课耗时，就换掉
                    time = time-heap[0]*(-1)+d
                    heapq.heappop(heap)
                    heapq.heappush(heap, -d)
        return len(heap)
    # https://leetcode-cn.com/problems/course-schedule-iii/solution/ke-cheng-biao-iii-by-leetcode-solution-yoyz/
