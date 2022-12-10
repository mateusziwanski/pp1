film_titles = ['Fight Club', 'Avatar', 'Seven', 'Sixth Sense', 'Titanic']

with open ("films.txt", 'w') as f:
    for x in film_titles:
        f.write(x+ "\n")