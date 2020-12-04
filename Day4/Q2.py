# Valid passport if:
    # Has all eight fields
    # Has all fields besides CID 

    # This means that CID is irrelevant -> Just need to check the seven fields
import re

validations = { "byr": lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,

                "iyr": lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,

                "eyr": lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,

                "hgt": lambda x: (x[-2:] == "cm" and int(x[:-2]) >= 150  and int(x[:-2]) <= 193 ) 
                              or (x[-2:] == "in" and int(x[:-2]) >= 59  and int(x[:-2]) <= 76),
                              
                "hcl": lambda x: x[0] == "#" and len(x) == 7 and re.search("^[0-9a-f]+", x[1:]),

                "ecl": lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],

                "pid": lambda x: len(x) == 9 and x.isdigit()
}

def valid_passport(passport):
    # Ensure all keys from the validation set exist in the passport
    valid = all(x in passport for x in validations.keys())

    # If all fields exist, validate them
    if valid:
        for field in passport.strip().replace('\n',' ').split(" "):
            k, v = field.split(":")

            # Check validity of k,v pair
            if k != "cid":
                if not validations[k](v):
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
