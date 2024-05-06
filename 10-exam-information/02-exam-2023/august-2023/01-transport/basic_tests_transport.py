import inspect
import pytest
import transport as module_under_test


def is_class_defined(class_name):
    return class_name in dir(module_under_test)


def if_class_exists(class_name):
    return pytest.mark.skipif(not is_class_defined(class_name), reason=f'Skipped because {class_name} has not been defined')


def is_class_abstract(c):
    return inspect.isabstract(c)


def is_subclass_of(*, super_name, sub_name):
    superclass = getattr(module_under_test, super_name)
    subclass = getattr(module_under_test, sub_name)
    return subclass in superclass.__subclasses__()


def is_abstract_method(cls, method_name):
    return method_name in cls.__abstractmethods__


def has_property(cls, *, property_name, abstract=False):
    if not hasattr(cls, property_name):
        return False
    prop = getattr(cls, property_name)
    if type(prop) is not property:
        return False
    if prop.__isabstractmethod__ != abstract:
        return False
    return True


def has_method(cls, *, method_name, parameter_names=None, abstract=False, static=False):
    if parameter_names is None:
        parameter_names = []

    if not hasattr(cls, method_name):
        return False
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    if abstract:
        if not is_abstract_method(cls, method_name):
            return False
    is_static = isinstance(inspect.getattr_static(cls, method_name), staticmethod)
    if is_static != static:
        return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True



@pytest.mark.parametrize('class_name', [
    'Passenger',
    'Vehicle',
    'Taxi',
    'Bus'
])
def test_classes_are_defined(class_name):
    assert is_class_defined(class_name), f'class {class_name} has not been defined'


@if_class_exists('Passenger')
@pytest.mark.parametrize('property_name', [
    'name',
])
def test_passenger_properties(property_name):
    assert has_property(
        module_under_test.Passenger,
        property_name=property_name
        ), f"Passenger must have property {property_name}"


@if_class_exists('Passenger')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'id', 'name', "money"],
    },
    {
        'method_name': 'is_valid_name',
        'parameter_names': ['name'],
        'static': True,
    },
])

def test_passenger_methods(kwargs):
    assert has_method(
        module_under_test.Passenger,
        **kwargs), f"Passenger's method {kwargs['method_name']} is missing or incorrect"


@if_class_exists('Vehicle')
def test_vehicle_class_is_abstract():
    assert is_class_abstract(module_under_test.Vehicle), 'Vehicle class is not abstract'


@if_class_exists('Vehicle')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'occupant_names',
    },
    {
        "property_name": 'number_of_occupants',
    },
    {
        "property_name": 'maximum_occupants',
        "abstract": True,
    },
])
def test_vehicle_properties(kwargs):
    assert has_property(module_under_test.Vehicle, **kwargs), f"Vehicle's {kwargs['property_name']} property is missing or incorrect"


@if_class_exists('Vehicle')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'license_plate', 'amount_of_seats'],
    },
    {
        'method_name': 'add_passenger',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'remove_passenger',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'remove_all_passengers',
        'parameter_names': ['self'],
    },
])
def test_vehicle_methods(kwargs):
    assert has_method(
        module_under_test.Vehicle,
        **kwargs), f"Vehicle's method {kwargs['method_name']} is missing or incorrect"


@if_class_exists('Taxi')
def test_taxi_class_is_not_abstract():
    assert not is_class_abstract(module_under_test.Taxi), 'Taxi should not be an abstract class'


@if_class_exists('Taxi')
def test_taxi_is_subclass_of_vehicle():
    assert is_subclass_of(super_name='Vehicle', sub_name='Taxi'), 'Taxi should inherit from Vehicle'


@if_class_exists('Taxi')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'occupant_names',
    },
    {
        "property_name": 'number_of_occupants',
    },
    {
        "property_name": 'maximum_occupants',
    },
])
def test_taxi_properties(kwargs):
    assert has_property(module_under_test.Taxi, **kwargs), f"Taxi's {kwargs['property_name']} property is missing or incorrect"


@if_class_exists('Taxi')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'license_plate', 'amount_of_seats'],
    },
    {
        'method_name': 'add_passenger',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'remove_passenger',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'remove_all_passengers',
        'parameter_names': ['self'],
    },
    {
        'method_name': 'pickup',
        'parameter_names': ['self', 'passengers', 'distance'],
    },
    {
        'method_name': 'dropoff',
        'parameter_names': ['self'],
    },
])
def test_taxi_methods(kwargs):
    assert has_method(module_under_test.Taxi, **kwargs), f"Taxi's method {kwargs['method_name']} is missing or incorrect"


@if_class_exists('Bus')
def test_bus_class_is_not_abstract():
    assert not is_class_abstract(module_under_test.Bus), 'Bus should not be an abstract class'


@if_class_exists('Bus')
def test_bus_is_subclass_of_vehicle():
    assert is_subclass_of(super_name='Vehicle', sub_name='Bus'), 'Bus should inherit from Vehicle'


@if_class_exists('Bus')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'occupant_names',
    },
    {
        "property_name": 'number_of_occupants',
    },
    {
        "property_name": 'maximum_occupants',
    },
])
def test_bus_properties(kwargs):
    assert has_property(module_under_test.Taxi, **kwargs), f"Bus's {kwargs['property_name']} property is missing or incorrect"


@if_class_exists('Bus')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'license_plate', 'amount_of_seats'],
    },
    {
        'method_name': 'add_passenger',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'remove_passenger',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'remove_all_passengers',
        'parameter_names': ['self'],
    },
    {
        'method_name': 'board',
        'parameter_names': ['self', 'passenger'],
    },
    {
        'method_name': 'disembark',
        'parameter_names': ['self', 'passenger'],
    },
])
def test_bus_methods(kwargs):
    assert has_method(module_under_test.Bus, **kwargs), f"Bus's method {kwargs['method_name']} is missing or incorrect"
