"""
Time: O(nlog(n))
Space: O(n)

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""


def canAttendMeetings(self, intervals):
    intervals.sort(key=lambda i: i.start)
    return all(intervals[i-1].end <= intervals[i].start
               for i in range(1, len(intervals)))


def canAttendMeetings2(self, intervals):
    intervals.sort(key=lambda i: i.start)
    return all(i.end <= j.start for i, j in zip(intervals, intervals[1:]))
