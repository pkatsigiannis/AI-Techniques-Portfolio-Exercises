import json

CURRENT_YEAR = 2026

with open("kr.json", "r", encoding="utf-8") as file:
    kb = json.load(file)


def get_frame(name):
    if name in kb["instances"]:
        return kb["instances"][name]
    if name in kb["classes"]:
        return kb["classes"][name]
    return None


def get_parent(name):
    frame = get_frame(name)

    if frame is None:
        return None

    if "instance_of" in frame:
        return frame["instance_of"]

    if "isa" in frame:
        return frame["isa"]

    return None


def find_slot(name, slot):
    frame = get_frame(name)

    if frame is None:
        return None

    slots = frame.get("slots", {})

    if slot in slots:
        value = slots[slot]

        # class slot format: {"type": ..., "value": ...}
        if isinstance(value, dict):
            if "value" in value:
                return value["value"]
            if "default" in value:
                return value["default"]
            if "derivation" in value:
                return value["derivation"]

        # instance slot format: "Batman_Returns", 1958, etc.
        return value

    parent = get_parent(name)

    if parent is None:
        return None

    return find_slot(parent, slot)


def age_of(name):
    birth_date = find_slot(name, "birth_date")

    if birth_date is None:
        return None

    return CURRENT_YEAR - birth_date


print("Does Val Kilmer fly?", find_slot("Val_Kilmer", "can_fly"))
print("How many legs does Tobias Maguire have?", find_slot("Tobias_Maguire", "legs"))
print("How old is Michelle Pfeiffer?", age_of("Michelle_Pfeiffer"))

robert = get_frame("Robert_Downey")
print("What character does Robert Downey play?", "Not Found" if robert is None else find_slot("Robert_Downey", "played"))