def marks( mark,complete_documents,attendance,assignment ):
    if mark < 70:
        return "FAIL", "Score is below 70"
    elif not complete_documents:
        return "FAIL", "Required documents are incomplete"
    elif attendance < 75:
        return "FAIL", "Attendance is below 75%"
    elif not assignment:
        return "FAIL", "Required assignment was not submitted"
    else:
        return "PASS", "All four conditions are satisfied"

test_cases = [
    {
        "name": "Test 1 - Pass",
        "input": (85, True, 90, True),
        "expected": "PASS"
    },
    {
        "name": "Test 2 - Fail because of attendance",
        "input": (82, True, 74, True),
        "expected": "FAIL"
    },
    {
        "name": "Test 3 - Fail because of assignment",
        "input": (88, True, 90, False),
        "expected": "FAIL"
    },
    {
        "name": "Test 4 - Threshold",
        "input": (70, True, 80, True),
        "expected": "PASS"
    }
]

for case in test_cases:
    mark, complete_documents, attendance, assignment = case["input"]

    actual, reason = marks( mark, complete_documents, attendance, assignment )

    print(case["name"])
    
    print( "Input: mark = ", mark, "Documents = ", complete_documents, "attendance = ", attendance, " %, "
        , " assignment_submitted = ", assignment )
        
    print("Expected result: ", case["expected"] )
    print("Actual result: ",actual)
    print("Reason: ", reason )
    print("-" * 50)
