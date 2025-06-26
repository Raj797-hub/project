from password_strength import analyze_password_strength
from wordlist_generator import generate_wordlist

def main():
    print("🔐 Password Strength Analyzer & Wordlist Generator\n")
    password = input("Enter a password to analyze: ")

    analysis = analyze_password_strength(password)
    print(f"\nPassword Score (0-4): {analysis['score']}")
    print(f"Estimated Crack Time: {analysis['crack_time']}")
    print("Feedback:")
    for fb in analysis['feedback']['suggestions']:
        print("  -", fb)

    print("\n📝 Let's generate a custom wordlist.")
    name = input("Enter your name: ")
    birth_year = input("Enter your birth year: ")
    pet_name = input("Enter your pet's name: ")

    wordlist = generate_wordlist(name, birth_year, pet_name)
    with open("sample_output/wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print("\n✅ Wordlist saved to 'sample_output/wordlist.txt'")

if _name_ == "_main_":
    main()
