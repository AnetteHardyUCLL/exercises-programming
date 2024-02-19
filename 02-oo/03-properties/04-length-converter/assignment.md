# Assignment

A more challenging exercise: write a class `LengthConverter` that helps you convert between different units of measurement.
Usage is as follows:

```python
>>> converter = LengthConverter()

# Set the distance to 100 meter
>>> converter.meter = 100

# Convert the 100 meter into feet
>>> converter.feet
328.084

# Convert the 100 meter into inch
>>> converter.inch
3937.01

# Convert the 100 meter into meter
>>> converter.meter
100

# Set the distance to 5 feet
>>> converter.feet = 5

# Convert 5 feet into inches
>>> converter.inch
60
```

We support three units: meter, feet and inches.
In order to use the converter, you must first set it to a certain distance:

```python
# Set distance to 10 inch
converter.inch = 10
```

In other words, *writing* to a property sets the distance in the corresponding unit (here inches).
To convert it to another unit, simply read the corresponding property:

```python
# Converting to meter
print(converter.meter)

# Converting to feet
print(converter.feet)
```

## Hints

* Internally, rely on a single private attribute that stores the distance in meter, e.g. `__distance_in_meter`.
* Each getter method should read `__distance_in_meter` and convert it to the corresponding unit.
* Each setter should convert the new value to the meters and store it in `__distance_in_meter`.
