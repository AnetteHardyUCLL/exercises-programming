# Examenvraag 1: Huisvesting

* Plaats alle code voor deze oefening in `housing.py`.
* In deze instructies zullen we altijd `self` weglaten.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een `basic_test_housing.py` bestand ontvangen dat basistesten bevat, zoals of bepaalde klassen bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_test_housing.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich op die klasse richten worden overgeslagen.
    Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit.
    Het niet slagen/overslaan van tests betekent dat je code zeker incompleet of incorrect is.
    Maar het slagen van de tests betekent niet dat je code volledig correct is!
* Je moet ook een aantal van je eigen tests maken in het `test-housing.py` bestand.
  * Alle tests die je zelf moet schrijven, staan aangegeven in dit opdrachtbestand.
  * Je mag hier extra tests toevoegen als je je code grondiger wilt controleren. Alleen de tests die in de opdracht worden gevraagd, worden beoordeeld.
  * Dit testbestand moet correct uitgevoerd kunnen worden om punten te verdienen.

## Person (Persoon)

* Definieer een klasse `Person`.
* Definieer een static method `is_valid_name(name)` die `True` teruggeeft als `name` geldig is en anders `False`.
  * Een naam moet uit minstens twee delen bestaan, gescheiden door een spatie.
  * Voorbeelden: "Harry Styles" en "Machine Gun Kelly" zijn geldige namen, maar "Rihanna" niet.
* Definieer de constructor van `Person`.
  * De constructor aanvaardt drie parameters: `id` (een string), `name` (een string) en `is_a_student` (een boolean).
  * De constructor moet een `ValueError` opwerpen als de naam ongeldig is.
* Sla `id` en `is_a_student` op in publieke velden en `name` in een privaat veld.
* Maak `naam` beschikbaar via een property.
  * Definieer een getter en een setter.
  * Als de naam ongeldig is, moet de setter een `ValueError` opwerpen.

## Residence (Verblijfplaats)

Een `Residence` vertegenwoordigt een plaats waar een persoon of personen kunnen wonen. Er zijn meerdere soorten residenties maar alle residenties hebben een aantal gemeenschappelijke methodes en velden. Daarom maken we een abstracte klasse `Residence` om gemeenschappelijke kenmerken van verschillende typen residenties op te slaan.

* Definieer een abstracte klasse `Residence`.
* Definieer een constructor voor `Residence`.
  * Deze heeft drie parameters: `address` (een string), `area` (een float, gemeten in vierkante meter), en `number_of_rooms` (een geheel getal).
  * Sla deze op in *publieke* velden.
  * Voeg nog een *privaat* veld `occupants` toe om een dictionary op te slaan van alle `Person`s die geregistreerd staan in deze `Residence`. <br>
  Deze dictionary bevat `id`s als sleutels en `Person` objecten als waardes.
  * Bij creatie heeft een `Residence` geen geregistreerde personen.
* Definieer een alleen-lezen property `number_of_occupants` die het aantal `Person`s geregistreerd in deze `Residence` teruggeeft.
* Definieer een read-only property `maximum_occupants`.
  * Het maximum aantal bewoners in een `Residence` is wettelijk bepaald. Om de berekening op dit examen niet te ingewikkeld te maken, hebben we de regels vereenvoudigd, zoals hier te zien is:
    * Elke `persoon` heeft minstens 20 vierkante meter ruimte nodig.
    * Elke kamer is geschikt voor maximaal 2 personen.
* Definieer een methode `register_resident(person)` die een `Person` toevoegt aan de dictionary van geregistreerde personen in deze `Residence`.
  * Als de `Person` al geregistreerd is bij deze `Residence`, moet er niets gebeuren.
  * Als er niet genoeg ruimte is voor een andere `Person` om zich legaal te registreren bij deze `Residence`, werp dan een `RuntimeError` op.
  * Als er genoeg ruimte is voor een extra `Person`, voeg deze `Person` dan toe aan de dictionary van personen die geregistreerd staan bij deze `Residence`. Gebruik de `id` van de `Person` als sleutel en het `Person` object als waarde.
* Definieer een methode `unregister_resident(id)` die een `Person` verwijdert uit het dictionary van geregistreerde personen in deze `Residence`.
* Definieer een property `resident_names` die een lijst met namen (strings) van alle geregistreerde personen in deze `Residence` teruggeeft.
  * Gebruik wat je geleerd hebt over functioneel programmeren om deze lijst te genereren.
* Definieer een abstracte methode `calculate_value()`.
  * Deze methode ontvangt geen parameters.

## Types of Residences (Soorten woningen)

Zoals eerder vermeld, zijn er verschillende soorten woningen: villa's, rijhuizen, appartementen en studentenkoten.
Gemeenschappelijke functionaliteit werd al geïmplementeerd in `Residence`. Hieronder zullen we twee subklassen definiëren om onderscheid te maken tussen verschillende soorten woningen. Om dit examen niet te lang te maken, zullen we alleen `Villa` en `StudentKot` implementeren.

### Villa

Een `Villa` erft over van `Residence`.
Behalve `address`, `area` en `number_of_rooms` (overgeërfd van `Residence`), kan een `Villa` ook een garage hebben.

* Definieer een constructor voor `Villa`.
  * Deze heeft vier parameters: drie van de `Residence`-constructor, plus `garage_capacity` (een geheel getal).
  * Sla `garage_capaciteit` op in een publiek veld.
* Implementeer `calculate_value`. De waarde van een `Villa` wordt op de volgende manier berekend:
  * villa_waarde = (25000 * number_of_rooms) + (2100 * area) + (10000 * garage_capacity)

### StudentKot (Studentenkot)

Een `StudentKot` erft over van `Residence`.
Een student heeft een adres en een oppervlakte, maar `number_of_rooms` is altijd 1.

* Definieer een constructor voor `StudentKot`.
  * Deze heeft twee parameters: `address` en `area` van `Residence`. De `number_of_rooms` is altijd 1.
* Voeg een extra beperking toe aan de overgeërfde methode `register_resident(person)`.
  * Een `Person` moet een student zijn om zich te kunnen registreren in een `StudentKot`. Als een `Person` die geen student is zich probeert in te schrijven in een `StudentKot`, werp dan een `RuntimeError` op.
* De waarde van een `StudentKot` wordt op de volgende manier berekend:
  * kot_value = 150000 + (750 * area)


## Voorbeeldgebruik:

```python
# maak een aantal personen
>>> aimee = Person("12.34.56-789.01","Aimee Backiel",False)
>>> bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# maak enkele woningen
>>> my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
>>> my_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)

# controleer de waarden van de eigenschappen
>>> my_villa.calculate_value()
427100

>>> myKot.calculate_value()
165000

# Verhuis de mensen naar een woning
>>> my_villa.register_resident(aimee)
>>> my_villa.register_resident(bastian)

# controleer de bewoners van de villa
>>> my_villa.resident_names
["Aimee Backiel","Bastian Li Backiel"]

# Op een dag, helaas, zal Bastian opgroeien en verhuizen naar zijn studentenkot
>>> my_villa.unregister_resident(bastian.id)
>>> my_kot.register_resident(bastian)

# controleer de bewoners opnieuw
>>> my_villa.resident_names
["Aimee Backiel"]

>>> my_kot.resident_names
["Bastian Li Backiel"]

# Met al haar vrije tijd kan Aimee de garage uitbreiden om ruimte te maken voor al haar hobby's.
>>> my_villa.garage_capacity = 3
>>> my_villa.calculate_value()
447100
```

# Testing (Testen)

Je moet tests schrijven die de property `maximum_occupants` voldoende testen. Neem deze tests op in het `test-housing.py` bestand.

Deze informatie is gekopieerd van de `Residence` klasse maar we geven tevens wat extra verduidelijking:
* Definieer een readonly property `maximum_occupants`.
  * Het maximum aantal bewoners in een `Residence` is wettelijk bepaald. Om de berekening op dit examen niet te ingewikkeld te maken, hebben we de regels vereenvoudigd, zoals hier getoond:
    * Elke `Person` heeft minstens 20 vierkante meter ruimte nodig.
    * Elke kamer is geschikt voor maximaal 2 personen.
* Deze regels moeten gecombineerd worden. Dus in een `Residence` met 72 vierkante meter en 3 kamers passen slechts 3 mensen (het kleinste resultaat van de twee berekeningen hierboven).
  * Andere voorbeelden:
    * In een kleine studio van 30 vierkante meter met slechts 1 kamer kan 1 persoon wonen.
    * In een iets grotere studio van 40 vierkante meter met 1 kamer kunnen 2 mensen wonen.
    * In een appartement van 200 vierkante meter met 3 kamers kunnen 6 mensen wonen.
* Gebruik de conventies die je in het hoofdstuk Testing hebt geleerd om deze functionaliteit te kunnen testen.
