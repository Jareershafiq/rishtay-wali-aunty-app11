import requests
from time import sleep

# === WHATSAPP API CONFIG ===
INSTANCE_ID = "instance135036"  # ✅ Your Instance ID
TOKEN = "n1tfmohkvp7zoylf"      # ✅ Your Token

def send_whatsapp_ultramsg(to_number, message):
    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"  # ✅ Fixed URL
    payload = {
        "token": TOKEN,
        "to": +923112712971,               # ✅ Keep number as string
        "body": "sara khan , age=22, profession= desinger, city=multan"
        
        "Alisha khan , age = 19 ,profession= doctor, city= karachi"
        
        "Mehwish Javed" , "age": 26, "gender": "female", "city": "Peshawar", "profession": "Nutritionist"
        
        "Aleena Shah", "age": 22, "gender": "female", "city": "Quetta", "profession": "Artist"
        
        "Zara Ahmed", "age": 25, "gender": "female", "city": "Multan", "profession": "Designer"
        
        "Ayesha Khan", "age": 24, "gender": "female", "city": "Lahore", "profession": "Doctor"
     }
    
    
    try:
        response = requests.post(url, data=payload)
        print(f"✅ Sent to {to_number}: ", response.json())  # Print server response
    except Exception as e:
        print(f"❌ Error sending to {to_number}: ", e)

def rishtay_wali_aunty(gender):
    profiles = [
        {"name": "Ayesha Khan", "age": 25, "gender": "female", "city": "Lahore", "profession": "Doctor", "whatsapp": ""},
        {"name": "Sara Ali", "age": 27, "gender": "female", "city": "Islamabad", "profession": "Teacher", "whatsapp": ""},
        {"name": "Jareer", "age": 18, "gender": "male", "city": "Karachi", "profession": "Engineer", "whatsapp": "+923112712971"},
        {"name": "Hamza Tariq", "age": 30, "gender": "male", "city": "Faisalabad", "profession": "Software Developer", "whatsapp": ""},
        {"name": "Zara Ahmed", "age": 24, "gender": "female", "city": "Multan", "profession": "Designer", "whatsapp": ""}
    ]

    print("\n👵 Rishtay Wali Aunty bol rahi hain...\n")

    matched = [p for p in profiles if p["gender"].lower() == gender.lower()]

    if not matched:
        print("Beta, aise koi rishtay nahi hain abhi.")
        return

    for p in matched:
        profile_line = f"{p['name']}, {p['age']} saal ka/ki, {p['profession']} from {p['city']}"
        print("👤", profile_line)

        # Send WhatsApp message
        send_whatsapp_ultramsg(
            to_number=p["whatsapp"],
            message=f"Aunty ka paighaam:\n{profile_line}"
        )

        sleep(1)  # slight delay to avoid API spam

    print("\n🧕 Aunty ne sabko message bhej diya beta. Duaon mein yaad rakhna.\n")

# ==== Program Start ====
print("🟢 Rishtay Wali Aunty Activated!")
gender_input = input("Beta, kis gender ke rishtay chahiye? (male/female): ")
rishtay_wali_aunty(gender_input)
