import secrets, string

random = secrets.SystemRandom()
print(random.randrange(0, 50))
print(random.randint(0, 50))
print(random.uniform(0, 50))
print(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10)))