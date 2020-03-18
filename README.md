# coding_challenge
## Chapter_I
Do uruchomienia nie są potrzebne żadne dodatkowe pakiety. Kod główny znajduje się w pliku internship_car.py
## Chapter_II
Do tego zadania została użyta nierelacyjna baza danych "MongoDB" postawiona na darmowym klastrze.
W celu uruchomienia projektu należy zainstalować dodatkowe biblioteki:
- pymongo
- argparse
- hashlib

```python
pip install pymongo
pip install argparse
pip install hashlib
```
Przykładowe użycia aplikacji konsolowej:

```script
python tasks_mongodb.py add --name Cleaning [--deadline 2020-10-10] [--description vacuuming]
python tasks_mongodb.py update [--name Cleaning] [--deadline 2020-10-10] [--description DESCRIPTION] --task_hash hash
python tasks_mongodb.py remove --task_hash hash
python tasks_mongodb.py list --all | --today
```
Parametry podane w nawiasach kwadratowych są opcjonalne.
W przypadku komendy 'list' należy podać jeden z przełączników --all lub --today
hashe poszególnych zadań można odczytać po wykonaniu komendy list --all


## Chapter_III
W zadaniu 3 nie użyłem żadnych dodatkowych pakietów. W celu otrzymania wyniku należy po prostu wystartować skrypt.
Prawidłowa odpowiedź to 935.
