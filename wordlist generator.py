def generate_wordlist(name, birth_year, pet_name):
    base_words = [name, pet_name, name + pet_name, name + birth_year, pet_name + birth_year]
    variants = []

    for word in base_words:
        variants.extend([
            word,
            word + "123",
            word.capitalize(),
            word.upper(),
            word[::-1],
            word + "@" + birth_year,
            word.replace('a', '@').replace('s', '$').replace('i', '1').replace('o', '0')
        ])

    return list(set(variants))  # remove duplicates
