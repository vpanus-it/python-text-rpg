# python-text-rpg
Jednoduchá textová RPG hra v Pythonu pro demonstraci pochopení objektově orientovaného programování (třídy, interakce objektů, inventář).

# Python Text RPG

Tento repozitář obsahuje ukázku jednoduché textové RPG hry vytvořené v jazyce Python. Projekt slouží k demonstraci práce s objektově orientovaným programováním (OOP).

## Co projekt obsahuje
Projekt je rozdělen do několika vývojových fází (skriptů), které postupně rozšiřují logiku hry:
* Tvorba základní třídy `Hrac`.
* Implementace atributů jako `jmeno`, `health` (zdraví) a `inventar`.
* Tvorba metod pro přidávání předmětů (zbraní) do inventáře.
* Logika útoku, kdy instance hráče volá metodu na objektu zbraně, která následně interaguje s dalším cílem (jiným hráčem/nepřítelem).

## Použité technologie
* Python 3
* Objektově orientované programování (OOP)
* Práce s moduly (např. `random`)

## Cíl projektu
Hlavním cílem tohoto projektu bylo prohloubit si znalosti v návrhu tříd, jejich vzájemné komunikaci a správě vnitřního stavu objektů v Pythonu.
