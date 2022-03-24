## Spis treści
* [Informacje ogólne](#informacje-ogólne)
* [Technologie](#technologie)
* [Instalacja](#instalacja)
* [Opis rozwiązania](#opis-rozwiązania)
## Informacje ogólne
Aplikacja webowa do wyszukiwania repozytoriów organizacji 
i użytkowników i sortowania ich po liczbie gwiazdek.
Projekt przygotowany na trzeci etap rekrutacji
na letni staż allegro.
## Technologie
Projekt stworzony przy użyciu
* Python 3.8.8
* Flask 1.1.2
* BeautifulSoup 4.9.2
* WTForms 2.3.3
* Bootstrap 5.0
## Instalacja
Wymagania: 

[git](https://git-scm.com/downloads)

[Python 3.8](https://www.python.org/downloads/release/python-388/)

1. Sklonuj gałąź master repozytorium i wejdź do folderu 
```
$ git clone https://github.com/Kacpri/GitHubLister.git
$ cd GitHubLister
```
2. Utwórz i aktywuj wirtualne środowisko (Python Virtual Environment)
```
$ python3 -m venv venv
$ venv\Scripts\activate.bat
```
3. Zainstaluj pakiety z pliku requirements.txt
```
$ pip install -r requirements.txt
```
4. Uruchom app.py
```
$ python app.py
```
5. Wejdź w przeglądarce na adres http://127.0.0.1:5000/ 
