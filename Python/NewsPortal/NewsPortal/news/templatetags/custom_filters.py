from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Censor применяется только к переменным строкового типа")

    forbidden_words = ['badword1', 'badword2', 'редиска']

    forbidden_variants = [word.lower() for word in forbidden_words] + \
                         [word[0].upper() + word[1:].lower() for word in forbidden_words]

    words = value.split()
    for i, word in enumerate(words):
        if word in forbidden_variants:
            words[i] = word[0] + '*' * (len(word) - 1)

    return ' '.join(words)
