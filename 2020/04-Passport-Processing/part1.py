import re

def validate(text):
    pass

if __name__ == "__main__":
    pattern_byr = "byr:"
    pattern_iyr = "iyr:"
    pattern_eyr = "eyr:"
    pattern_hgt = "hgt:"
    pattern_hcl = "hcl:"
    pattern_ecl = "ecl:"
    pattern_pid = "pid:"
    pattern_cid = "cid:"

    __patterns__ = [pattern_byr, pattern_iyr, pattern_eyr, pattern_hgt,
                    pattern_hcl, pattern_ecl, pattern_pid]

    patterns = [re.compile(pattern) for pattern in __patterns__]
    
    with open("input.txt", "r") as fp:
        f = fp.read()

    passports = f.split("\n\n")
    valid_passports = 0

    for passport in passports:
        flag = True
        for pattern in patterns:
            if pattern.search(passport) is None:
                flag = False
                break
        if flag:
            valid_passports += 1
    print(valid_passports)
