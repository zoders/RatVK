import random

buzz = ('жесть', 'лень',
        'грусть', 'печаль', 'глупость')
adjectives = ('Бесконечная', 'Постоянная', 'Инфернальная', 'Жестокая', 'Гадкая')
adverbs = ('постоянно', 'жестоко', 'критично', 'серьёзно',
           'стремительно')
verbs = ('вызывает', 'производит', 'нагнетает', 'усиливает', 'не убирает')


def sample(l, n=1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
                       sample(verbs), buzz_terms[1]])
    return phrase


if __name__ == "__main__":
    print(generate_buzz())
    print(type('str') == type('dadasd'))