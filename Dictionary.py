student_data = {
    "id1": {"name" : "Sara", "class": "V", "subject_int": "english, math, science"},
    "id2": {"name" : "David", "class": "V", "subject_int": "english, math, science"},
    "id3": {"name" : "Sara", "class": "V", "subject_int": "english, math, science"},
    "id4": {"name" : "Surya", "class": "V", "subject_int": "english, math, science"},
}
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_keys=(details["name"], details["class"], details["subject_int"])
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id] = details
for k, v in result.items():
    print(k, ":", v)