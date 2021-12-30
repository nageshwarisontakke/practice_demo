
def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
list1 = [23, 21, 5, 43, 83, 231, 72]
print("Largest element is:", myMax(list1))


def findLargest(arr1):
    secondLargest = arr1[0]
    largest = arr1[0]
    for i in range(len(arr1)):
        if arr1[i] > largest:
            largest = arr1[i]

    for i in range(len(arr1)):
        if arr1[i] > secondLargest and arr1[i] != largest:
            secondLargest = arr1[i]

    return secondLargest

arr1=[23, 21, 5, 43, 83, 231, 72]
print(findLargest(arr1))

import json
student_details = {
    "student_name":"abc", "age":"17",
    "Subjects":[ "Physics", "Chemistry", "Mathematics","Computer Science", "Hindi","English"] }
stud=json.dumps(student_details)
print(stud)