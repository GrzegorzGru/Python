# Word jumble. Napisz program, który losuje słowo z listy i miesza jego litery. Użytkownik ma odgadnąć, jakie to słowo.
# Program powinien sprawdzić, czy odpowiedź użytkownika jest prawidłowa i wyświetlić odpowiedni komunikat.
# Pozwól użytkownikowi zgadywać 3 razy, w myśl zasady do trzech razy sztuka

from random import shuffle, randint
words = ['drzwi', 'kartka', 'stół', 'kino', 'sklep', 'sufit', 'trawa', 'cukier', 'wiatr', 'klawiatura', 'długopis', 'basen', 'praca', 'dom', 'szkoła', 'klucz', 'klasa', 'burza', 'kwiat', 'chmura', 'brama', 'droga', 'las', 'lampa', 'zamek', 'miasto', 'kuchenka', 'słownik', 'rower', 'piekarnik', 'kometa', 'papier', 'krzesło', 'słowo', 'szafa', 'książka', 'ciasto', 'serce', 'słońce', 'okno', 'kwiat', 'komputer', 'butelka', 'kamień', 'woda', 'twarz', 'morze', 'drożdże', 'projektor', 'kubek', 'talerz', 'obiad', 'deszcz', 'dach', 'telewizor', 'samolot', 'pies', 'niebo', 'farba', 'skarpetka', 'ziemia', 'rzeka', 'ogród', 'światło', 'pociąg', 'podróż', 'telefon', 'jezioro', 'truskawka', 'czas', 'list', 'zeszyt', 'drzewo', 'samochód', 'pianino', 'miska', 'pokój', 'zegar', 'kawa', 'kapelusz', 'zupa', 'świeca', 'dzień', 'jabłko', 'motyl', 'ogród', 'kolor', 'herbata', 'kran', 'drzwi', 'ryba', 'płaszcz', 'miłość', 'księżyc', 'rower', 'bilet', 'kot', 'muzyka', 'słoik', 'jajko']
number = randint(0,99)
word = words[number]
shuffled_word = []
word_to_guess = ''
tries = 3

for letter in word:
    shuffled_word.append(letter)
shuffle(shuffled_word)
for letter in shuffled_word:
    word_to_guess += word_to_guess.join(letter)
print(f'Jak myślisz, jakie to słowo?\n'
      f'{word_to_guess}\n' )
for _ in range(tries):
    player_word = input(f'Pozostała ilość prób: {tries}\n')
    tries -= 1
    if player_word.lower() == word:
        if tries == 2:
            print('Udało Ci się za pierwszym razem! Gratulacje!')
        elif tries == 1:
            print('Udało Ci się za drugim razem! Dobra robota!')
        else:
            print('Było blisko - ale się udało. Następnym razem na pewno będzie lepiej.')
        quit()
    print('To nie jest właściwe słowo.')
print('Porażka. Może następna runda?')