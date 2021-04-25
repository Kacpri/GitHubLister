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
## Opis rozwiązania
W rozwiązaniu rozdzieliłem wyświetlanie repozytoriów organizacji 
i repozytoriów użytkowników. Zrobiłem to z dwóch powodów:
po pierwsze linki do listy repozytoriów organizacji są prostsze,
np. dla Allegro, github.com/allegro,
zaś użytkowników nieco dłuższe,
np. github.com/Kacpri?tab=repositories
po drugie chciałem wylistować wszystkie repozytoria, 
a nie jedynie te na pierwszej stronie.
Dla organizacji było to bardzo proste,
wystarczy dopisać na końcu ?page=nr_strony,
np. github.com/allegro?page=2
Dla użytkowników nie da się w łatwy sposób utworzyć linku
do kolejnych stron z repozytoriami,
dlatego skorzystałem z przycisku, z którego pobieram link.

Rozwiązanie wydaje się działać dobrze zarówno dla organizacji
jak i użytkowników, jednak działa dość wolno, 
np. dla organizacji jak google, 
które posiada 67 stron z repozytoriami,
strona wydaje się nie reagować, 
jednak po dłuższej chwili wyświetla poprawnie informacje.

Rozważałem zastosowanie plug-inu datatables do biblioteki jquery,
który dodałby ciekawe funkcje do tablicy, 
np. sortowanie po nazwie, wyszukiwanie, czy rozmieszczenie na stronach,
jednak nie było tego w wymaganiach, dlategp zrezygnowałem.

Jeśli chodzi o uproszczenia, dla repozytoriów, 
które mają liczbę gwiazdek w postaci np. 3.4k, 
zamieniam to na 3400, mimo iż nie jest to ich dokładna liczba.
  
