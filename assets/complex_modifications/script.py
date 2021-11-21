import json

left_shift_keys_to_disable = "qwertasdfgzxcvb"
right_shift_keys_to_disable = "yuiophjkl;nm,./"

keys = [left_shift_keys_to_disable, right_shift_keys_to_disable]
directions = ['left', 'right']

config = {
    "title": "Shift Training Wheels",
}

def manipulator(key, direction):
    main = {
        "type": "basic",
        "from": {
            "key_code": key,
            "modifiers": {
                "mandatory": [
                    "left_shift" if (direction == 'left') else "right_shift"
                ]
            }
        },
        "to": {
            "key_code": "vk_none"
        }
    }
    return main

def rule(keys, direction):
    rule = {
        "description": f"Use the correct {direction} shift keys",
        "manipulators": [manipulator(key, direction) for key in keys]
    }
    return rule

config['rules'] = [rule(keys[i], directions[i]) for i in range(2)]
with open('shift-training-wheels.json', 'w') as file:
    json.dump(config, file, indent=4)

