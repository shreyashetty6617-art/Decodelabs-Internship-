import random, string

def check_strength(pwd):
    if len(pwd) < 6: return "Weak 🔴"
    if len(pwd) < 10: return "Medium 🟡"
    return "Strong 🟢"

length = int(input("Password length: "))
chars = string.ascii_letters + string.digits + "!@#$%"
pwd = ''.join(random.choice(chars) for _ in range(length))

print(f"Password: {pwd}")
print(f"Strength: {check_strength(pwd)}")
