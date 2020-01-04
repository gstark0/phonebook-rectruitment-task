# Django-Phonebook
Aplikacja książki telefonicznej w Django. Można ją przetestować pod adresem [phonebook.gstark.me](http://phonebook.gstark.me/ "phonebook.gstark.me")

### Funkcjonalności
- Przeglądanie listy kontaktów
- Dodawanie i edycja danych osobowych
- Wyszukiwanie po osobie, numerze telefonu lub adresie email
- Usuwanie osób do których nie ma przypisanych żadnych numerów telefonu ani adresów email.

### Jak uruchomić?
`python manage.py migrate`

Plik fixtures.json zawiera 20 przykładowych kontaktów, możesz je wczytać przy pomocy polecenia:<br>
`python manage.py loaddata fixtures.json`

`python manage.py runserver`

Serwer testowy działa pod adresem `http://127.0.0.1:8000/`

### Zdjęcia z aplikacji
![Książka telefoniczna](https://raw.githubusercontent.com/gstark0/phonebook-rectruitment-task/master/screenshots/phonebook.png)

![Dodawanie osób](https://raw.githubusercontent.com/gstark0/phonebook-rectruitment-task/master/screenshots/adding_people.png)

![Edycja osób](https://raw.githubusercontent.com/gstark0/phonebook-rectruitment-task/master/screenshots/editing_people.png)

![Wyszukiwanie osób](https://raw.githubusercontent.com/gstark0/phonebook-rectruitment-task/master/screenshots/searching_contacts.png)

![Dodawanie numerów i adresów email](https://raw.githubusercontent.com/gstark0/phonebook-rectruitment-task/master/screenshots/adding_phone_numbers_and_emails.png)
