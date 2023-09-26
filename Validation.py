import re
def validate_age(age):
    try:
        age = int(age)
        if age >= 18:
            return age
        else:
            return None
    except ValueError:
        return None

def validate_gender(gender):
    if gender.lower() in ['male', 'female', 'other']:
        return gender
    else:
        return None
    
def validate_dob(dob):
    dob_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$')
    if dob_pattern.match(dob):
        return dob
    else:
        return None

  
def validate_pan_card(pan_card):
    pan_pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')
    if pan_pattern.match(pan_card):
        return pan_card
    else:
        return None

  
def validate_aadhar_number(aadhar_number):
        
        aadhar_pattern = re.compile(r'^\d{12}$')
        if aadhar_pattern.match(aadhar_number):
            return aadhar_number
        else:
            return None