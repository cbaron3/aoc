# Valid passport if:
    # Has all eight fields
    # Has all fields besides CID 

    # This means that CID is irrelevant -> Just need to check the seven fields

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def valid_passport(passport):
    valid = True
    for field in valid_fields:
        if field not in passport:
            valid = False
    return valid

passport_entry = ""
valid_count = 0
with open('Input.txt') as file:
    for line in file:
        # Add to passport entry until we hit an empty line
        if line == "\n":
            # Check validity of passport_entry
            if valid_passport(passport_entry):
                valid_count += 1
            passport_entry = ""
        else:
            # Add to passport entry
            passport_entry += line

# Check last passport entry because the file does not end if an empty line
if valid_passport(passport_entry):
    valid_count += 1

print(valid_count)
