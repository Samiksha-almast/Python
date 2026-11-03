def clean_customer(raw):
    parts = raw.split(';')
    if len(parts) != 4:
        return None
    # Step 2: Extract and clean the fields
    name = parts[0].strip()
    email = parts[1].strip().lower()
    phone = parts[2].strip()

    city = parts[3].strip()
    # Step 3: Clean the name and city
    name = ' '.join(name.split()).title()
    city = city.title()
    # Validate the name
    if not name:
        return None
    for word in name.split():
        if not word.isalpha():
            return None
    # Validate the city
    if not city:
        return None
    # Step 4: Validate the email
    if email.count('@') != 1:
        return None
    email_parts = email.split('@')
    local = email_parts[0]
    domain = email_parts[1]
    if not local:
        return None
    if '.' not in domain:
        return None
    if domain.startswith('.') or domain.endswith('.'):
        return None
    # Step 5: Clean the phone number
    phone = phone.replace(' ', '')
    phone = phone.replace('-', '')
    # Remove +91 if present
    if phone.startswith('+91'):
        phone = phone[3:]
    # Remove 91 from a 12-digit number
    elif len(phone) == 12 and phone.startswith('91'):
        phone = phone[2:]
    # Step 6: Validate the phone number
    if len(phone) != 10:
        return None
    if not phone.isdigit():
        return None
    if phone[0] not in '6789':
        return None
    # Step 7: Return the cleaned record
    return {

        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }
        
        
lines = [
 ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
 'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
 'meera;meera@mail;9123456780;Delhi',
 'john doe; john@x.org ;12345; Goa',
 'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
 'amit;amit@site.com;9876543210'
]
rejected = 0
for raw in lines:
    result = clean_customer(raw)
    if result is not None:
        print(result)
    else:
        rejected += 1
print('Rejected:', rejected)