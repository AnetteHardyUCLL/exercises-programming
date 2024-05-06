# Examen Vraag 1: Transportvoertuigen

* Plaats alle code voor deze oefening in `transport.py`.
* In deze instructies laten we altijd het vermelden van `self` achterwege.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een bestand `basic_test_transport.py` ontvangen dat basis testen bevat, zoals of bepaalde klassen bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_test_transport.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich richten op die klasse worden overgeslagen.
    Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit.
    Falende/overgeslagen tests betekenen dat je code zeker onvolledig of incorrect is.
    Maar geslaagde tests betekenen niet dat je code volledig correct is!
* Je moet ook zelf enkele tests maken in het bestand `test-transport.py`.
  * Alle tests die je zelf moet schrijven, zijn aangegeven in dit opdrachtbestand.
  * Je kunt hier extra tests aan toevoegen als je je code grondiger wilt controleren. Alleen de tests die in de opdracht worden gevraagd, worden beoordeeld.
  * Dit testbestand moet correct kunnen worden uitgevoerd om punten te verdienen.

## Passagier

* Definieer een klasse `Passenger`.
* Definieer een statische methode `is_valid_name(name)` die `True` retourneert als `name` geldig is en anders `False`.
  * Een naam moet bestaan uit ten minste twee delen gescheiden door een spatie.
  * Voorbeelden: "Harry Styles" en "Machine Gun Kelly" zijn geldige namen, maar "Rihanna" niet.
* Definieer de constructor van `Passenger`.
  * De constructor neemt drie parameters: `id` (een string), `name` (een string) en `money` (een int).
  * De constructor moet een `ValueError` genereren als de naam ongeldig is.
* Sla `id` en `money` op in openbare velden.
* Sla `name` op in een privéveld en maak het toegankelijk via een eigenschap.
  * Definieer een getter en een setter voor `name`.

## Voertuig

Een `Vehicle` vertegenwoordigt een voertuig waarmee mensen naar een bestemming kunnen reizen, waarvan sommige een tarief moeten betalen. Er zijn verschillende soorten voertuigen, maar alle voertuigen delen enkele gemeenschappelijke kenmerken. Daarom zullen we een abstracte klasse `Vehicle` definiëren om gemeenschappelijke kenmerken van verschillende soorten voertuigen op te slaan.

* Definieer een abstracte klasse `Vehicle`.
* Definieer een constructor voor `Vehicle`.
  * Het heeft twee parameters: `license_plate` (een string) en `amount_of_seats` (een int).
  * Sla deze op in *openbare* velden.
  * Voeg nog een *privaat* veld `occupants` toe om een ​​dictionary van alle mensen die in dit `Vehicle
` rijden, op te slaan.
  * Bij aanmaak heeft een `Vehicle` geen geregistreerde inwoners.
* Definieer een alleen-lezen eigenschap `number_of_occupants` die het aantal geregistreerde `Passenger`s voor dit `Vehicle` retourneert.
* Definieer een abstracte alleen-lezen eigenschap `maximum_occupants`.
* Definieer een methode `add_passenger(passenger)` om een ​​`Passenger` aan de `occupants` dictionary toe te voegen.
* Definieer een methode `remove_passenger(passenger)` om een `Passenger` uit de `occupants` dictionary te verwijderen.
* Definieer een methode `remove_all_passengers()` om alle `Passenger`s uit de `occupants` dictionary te verwijderen.
* Definieer een eigenschap `occupant_names` die een lijst met namen (strings) van alle mensen die in dit `Vehicle` rijden, retourneert.

## Soorten Voertuigen

Zoals eerder vermeld, zijn er verschillende soorten voertuigen: taxi's, bussen, auto's, vliegtuigen, enzovoort.
Gemeenschappelijke functionaliteit is al geïmplementeerd in `Vehicle`. Hieronder zullen we twee dergelijke subklassen definiëren om onderscheid te maken tussen soorten voertuigen. Om te voorkomen dat dit examen te lang wordt, zullen we alleen `Bus` en `Taxi` implementeren.

### `Taxi`

Een `Taxi` erft van `Vehicle`. Elke zitplaats in een `Taxi` kan precies één passagier bevatten.

* Definieer een constructor voor `Taxi`.
  * Het heeft twee parameters: beide overgenomen van de constructor van `Vehicle`.
  * Voeg een ander openbaar veld `is_available` toe. Deze boolean geeft aan of de `Taxi` beschikbaar is om nieuwe passagiers te accepteren.
* Implementeer `maximum_occupants`: één passagier per stoel.
* Maak een methode `pickup(passengers, distance)`.
  * Een `ValueError` moet worden gegenereerd als de `Taxi` momenteel niet beschikbaar is of als het aantal passagiers het maximum overschrijdt.
  * Als de `Taxi` beschikbaar is en de passagiers kunnen worden ondergebracht:
    * Bereken het tarief: tarief = 1 + afstand, er is een minimumtarief van 5 euro.
    * De eerste `Passenger` in de lijst `passengers` is verantwoordelijk voor het betalen van de rit. Als deze `Passenger` niet genoeg geld heeft om het tarief te betalen, moet een `RuntimeError` worden gegenereerd.
    * Dit verantwoordelijke `Passenger`-object wordt geld afgetrokken ter waarde van het tarief.
    * Alle `Passenger`s in de lijst `passengers` moeten worden geregistreerd als rijdend in deze `Taxi`.
* Maak een methode `dropoff()` om de passagiers uit de taxi op hun bestemming te laten uitstappen.
  * Er mogen geen passagiers meer in de `Taxi` zijn.
  * De `Taxi` moet beschikbaar worden voor de volgende groep passagiers.
  * Als er geen huidige passagiers zijn, is er geen actie vereist.

### `Bus`

Een `Bus` erft van `Vehicle`.

* Definieer een constructor voor `Bus`.
  * Het heeft twee parameters: `license_plate` en `amount_of_seats`, beide overgenomen van de constructor van `Vehicle
`.
* Implementeer `maximum_occupants`: voor een bus geldt `maximum_occupants = 2 * amount_of_seats`.
* Maak een methode `board(passenger)` om een passagier toe te laten in de bus:
  * Als het toevoegen van één passagier het maximale aantal rijders zou overschrijden, moet een `RuntimeError` worden gegenereerd.
  * Het tarief is 2 euro voor alle passagiers.
  * Als de `Passenger` niet genoeg geld heeft om het tarief te betalen, moet een `RuntimeError` worden gegenereerd.
  * Anders moet het tarief worden afgetrokken van het geld van de `Passenger`.
  * De `Passenger` moet worden geregistreerd in de `occupants` dictionary.
* Maak een methode `disembark(passenger)` om een passagier de bus te laten verlaten:
  * De `Passenger` moet uit de `occupants` dictionary worden verwijderd als deze in de bus rijdt.

## Voorbeeldgebruik

```python
# enkele passagiers aanmaken
>>> aimee = Passagier("12.34.56-789.01", "Aimee Backiel", 40)
>>> bastian = Passagier("01.02.03-040.05", "Bastian Li Backiel", 5)

# enkele voertuigen aanmaken
>>> mijn_taxi = Taxi("1-NGL-760", 4)
>>> mijn_bus = Bus("1-HUE-344", 30)


# samen een busrit maken; Bastian betaalt graag zelf
>>> mijn_bus.board(aimee)
>>> mijn_bus.board(bastian)

# de inwoners van de bus controleren
>>> mijn_bus.occupant_names
["Aimee Backiel", "Bastian Li Backiel"]

# ze stappen uit bij de dierentuin
>>> mijn_bus.disembark(aimee)
>>> mijn_bus.disembark(bastian)

# opnieuw de inwoners controleren
>>> mijn_bus.occupant_names
[]

# Bastian wil voor het eerst alleen met de bus gaan en Aimee volgt hem in een taxi
# ze rijden slechts 5 km om zeker te zijn dat hij niet verdwaalt
>>> mijn_bus.board(bastian)
>>> mijn_taxi.pickup([aimee], 5)

# de inwoners in elk voertuig controleren
>>> mijn_bus.occupant_names
["Bastian Li Backiel"]
>>> mijn_taxi.occupant_names
["Aimee Backiel"]

# controleren hoeveel geld er nog over is in hun portemonnees
>>> aimee.money
32
>>> bastian.money
1
```

# Testing
Je moet tests schrijven die voldoende de eigenschap `maximum_occupants` testen. Neem deze tests op in het bestand `test-transport.py`.

* Raadpleeg de beschrijving van zowel `Taxi` als `Bus` voor informatie over hoe je `maximum_occupants` kunt implementeren.
* Gebruik de conventies die je hebt geleerd in het hoofdstuk over Testen om deze functionaliteit te kunnen testen.