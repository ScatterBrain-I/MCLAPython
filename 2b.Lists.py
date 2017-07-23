dayCourses = ['Yoga', 'Calc', 'History']
eveCourses = ['python']
allCourses = dayCourses + eveCourses

print "Day Courses: %s" % dayCourses
print "Evening Courses: %s" % eveCourses
print "All Courses: %s" % allCourses

dayCourses.insert(1, 'Philosophy')

print "Day Courses: %s" % dayCourses

del dayCourses[2]
print "Day Courses: %s" % dayCourses

eveCourses[0] = 'Introduction to Python'
print "Evening Courses: %s" % eveCourses

songPt1 = ['Mary', 'had', 'a']
songPt2 = ['little', 'lamb']
song = songPt1 + (songPt2 * 3)

print song

for items in songPt1:
    temp = items
    print temp 