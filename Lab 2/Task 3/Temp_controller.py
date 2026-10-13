def temp_control(temp, current, previous):
    if not current:
        target_mode = "Off"
    elif temp < 18:
        target_mode = "Heat"
    elif temp > 26:
        target_mode = "Cool"
    else:
        target_mode = "Eco"
        
    command_needed = target_mode != previous
    
    return target_mode, command_needed

test_cases = [
    {
        "name": "Start of heating",
        "temperature": 17,
        "occupied": True,
        "previous_mode": None
    },
    {
        "name": "Repeated heating percept",
        "temperature": 17,
        "occupied": True,
        "previous_mode": "Heat"
    },
    {
        "name": "Lower exact boundary",
        "temperature": 18,
        "occupied": True,
        "previous_mode": "Heat"
    },
    {
        "name": "Upper exact boundary",
        "temperature": 26,
        "occupied": True,
        "previous_mode": "Eco"
    },
    {
        "name": "Mode transfer to cool",
        "temperature": 27,
        "occupied": True,
        "previous_mode": "Eco"
    },
    {
        "name": "Empty room",
        "temperature": 22,
        "occupied": False,
        "previous_mode": "Eco"
    },
    {
        "name": "Repeating empty-room percept",
        "temperature": 22,
        "occupied": False,
        "previous_mode": "Off"
    }
]

for case in test_cases:
    target, command_needed = temp_control( case["temperature"], case["occupied"], 
    case["previous_mode"] )

    print(case["name"])
    print("Previous mode:", case["previous_mode"])
    print( "Percept:", "temperature =", case["temperature"], "occupied =", case["occupied"] )
    print("Target mode:", target)
    print( "Outcome:", "SEND COMMAND" if command_needed else "NO COMMAND" )
    print("-" * 45)
