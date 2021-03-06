Minecraft Pi
#############

`Minecraft Pi Edition <http://pi.minecraft.net/>`_ to specjalna wersja gry
`Minecraft <https://pl.wikipedia.org/wiki/Minecraft>`_ uruchamianej jako serwer
na minikomputerze `Raspberry Pi <https://pl.wikipedia.org/wiki/Raspberry_Pi>`_
z systemem `Raspbian <https://www.raspbian.org/>`_.
Wyjątkową cechą tej wersji jest możliwość kontrolowanie niektórych elementów gry za pomocą
`Minecraft API <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
zawartych w bibliotekach **mcpi** napisanych w języku `Python <https://www.python.org/>`_
i preinstalowanych w Raspbianie (w wersji dla Pythona 2 i 3).
Całość bardzo dobrze nadaje się do nauki programowania z wykorzystaniem języka Python.

**Wymagania wstępne**

1. Serwer Minecrafta Pi, czyli minikomputer Raspberry Pi w wersji B+, 2 lub 3
   z najnowszą wersją systemu Raspbian.
2. Klient, czyli dowolny komputer z systemem Linux lub Windows,
   zawierający:

   - interpreter Pythona 2.7.x,
   - biblioteki PyGame i numpy,
   - bibliotekę `mcpi <https://github.com/martinohanlon/mcpi>`_,
   - symulator `mcpi-sim <https://github.com/pddring/mcpi-sim>`_.

3. Adresy IP serwera i klienta muszą należeć do tej samej sieci lokalnej.

**Instalacja bibliotek**

Pobierz archwium :download:`mcpi-sim.zip <mcpi-sim.zip>` i rozpakuj je w wybranym
katalogu (np. katalogu domowym) za pomocą menedżera archwiwów lub poleceniem w terminalu:

.. code-block:: bash

    ~$ unzip mcpi-sim.zip

Archiwum zawiera katalog :file:`mcpi-sim` z biblioteką *mcpi* oraz zmodyfikowanymi
na potrzeby naszych scenariuszy bibliotekami symulatora.

W razie potrzeby zobacz, jak zainstalować biblioteki *PyGame* i *numpy* w systemie
:ref:`Linux <linux-pakiety>` lub :ref:`Windows <pygame-win>`.

.. note::

  * Dystrybucja XenialPup KzkBox przygotowana na potrzeby naszego projektu zawiera już symulator.
  * Opisane poniżej scenariusze można realizować bezpośrednio w Raspbianie na Raspberry Pi.


.. toctree::
    :maxdepth: 2

    podstawy/index
    figury/index
    turtle/index
    funkcje/index
    algorytmy/index
    glife/index
    rgame/index
    gloss_mcpi

**Materiały**

1. Minecraft `Pi Edition <http://minecraft.gamepedia.com/Pi_Edition>`_
2. Dokumentacja `Minecraft API <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
3. `Getting started with Minecraft Pi <https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/>`_
