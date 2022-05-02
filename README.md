# PRproj
## Instalacja python - Windows

Ściągamy i instalujemy najnowszego pythona3:
https://www.python.org/downloads/

Ważne, zeby przy isntalacji zaznaczyć opcję o dodaniu do PATH, oraz instalacje PIP


Instalacja/kompilacja bibliotek:
Większość da się zrobić z poziomu konsoli windows:

>pip install dlib -v
- powyższa linijka prawdopodobnie skończy się błędem. Pakiet ten trzeba będzie skompilować ze źródeł. W tym celu:

instalacja cmake:
>pip install cmake

upewnić się, że jest zainstalowany Visual Studio (wystarczy darmowa wersja Community - spora szasna, ze już kiedyś używaliście i macie)
https://visualstudio.microsoft.com/pl/downloads/

Jak to mamy to ponownie:
>pip install dlib -v
(Może to potrwać kilkadziesiąt minut)

Reszta juz prościej:
>pip install opencv-python

>pip install face-recognition

>pip install pyttsx3

Możliwe, ze trzeba będzie coś jeszcze doinstalować jak zaczną wyskakiwać błędy z różnymi kodami.

Jeżeli chcemy sprawdzić czy pakiety się dobrze zainstalowały:
odpalamy pythona:
>py

Po kolei importujemy biblioteki:
>>>import cv2

>>>import face_recognition

>>>import pyttsx3

Jeżeli pojawił się jakikolwiek błąd to znaczy, że coś wcześniej nie poszło dobrze.

## Importowanie źródeł z GItHuba

Kod możemy porbać takim jakim jest. Na stronie repozytorium klikamy Code->download zip i wypakowujemy gdzie chcemy.

To rozwiązanie zadziała, ale ma wady. Po każdym updacie trzeba by ściągać nową wersję i podmieniać pliki. Dlatego można skorzystać z dobrodziejstw gita. Zakładając, że nie chcecie używać za dużo konsoli- klikając Open with GitHub desktop pozwoli wam zainstalować przyjemne w użyciu narzędzie GitHubba do pracy z repozytorium. Mając to narzędzie będziecie mieli łatwą możliwość ściągania najnowszych wersji kodu, commitowania swoich zmian, pushowania na swój fork i (po dodaniu jako contributiorzy) robienia pull requestów żebym mógł zmergować Wasze zmiany w głównym branchu. W intrernecie jest sporo materiałów jak sie pracuje z gitem (większośc używa konsoli, ale na początek może Wam być łatiwej z desktopową wersją). Ogólnie to jest narzędzie które może Wam się przydać i jego znajomośc może Wam uprościć życie w przysżłości.


## Odpalenia i praca z kodem

Skrypty pythona nie wymagają kompilacji. Skrypt można odpalic bezpośrednio z exploratora, lub poziomu konsoli. Bedąc w folderze w którym ściągneliśmy pliki z gita odpalamy:
>py proj.py

Powinno zadziałać. Jak zwraca jakieś błey to trzeba wyjaśnić. 
Źródła można modyfikować nawet i w notatniku, jednak polecam jakieś sensowniejsze narzędzie do edycji i debugowania. Np. Visual Studio Code:
https://visualstudio.microsoft.com/pl/downloads/
W Extyensions wyszukujemy i instalujemy w nim narzędzia do Pythona Microsoftu. Od tego momentu możemy odpalać i debugować skrypty bezpośrednio z VSC co jest wygodne.

## działanie programu (stan na 02.05.2022)

W folderze zdjęcia znajduje się plik data.txt. W pliku tym znajdują się nazwy zdjęć oraz powiązane z nimi teksty. 
Enkoduje zdjęcia z listy w dace_recognition.
Odpala kamere o id=0 (zwykle kamera w laptopie, lub kamera podpięta przez USB). Na każdej kolejnej klatce wyszukuje widoczne twarze. Każą z tych twarzy porównuje z wcześniej encodowanymi twarzami. Jak znajdzie dopasowanie to uruchamia syntezator z tekstem z pliku.
