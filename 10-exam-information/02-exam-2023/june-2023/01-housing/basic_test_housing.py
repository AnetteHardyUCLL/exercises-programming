import inspect
import pytest
import housing


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(housing), reason=f'Skipped because {class_name} has not been defined')


def is_class_abstract(c):
    return inspect.isabstract(c)


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



def test_person_class_is_defined():
    assert 'Person' in dir(housing), 'Person class has not been defined'


@if_class_exists('Person')
@pytest.mark.parametrize('property_name', [
    'name',
])

def test_person_properties(property_name):
    assert has_property(
        housing.Person,
        property_name=property_name
        ), f"Person must have property {property_name}"


@if_class_exists('Person')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'id', 'name','is_a_student'],
        'abstract': False,
    },
    {
        'method_name': 'is_valid_name',
        'parameter_names': ['name'],
        'abstract': False,
        'static': True,
    },
])
def test_person_methods(kwargs):
    assert has_method(
        housing.Person,
        **kwargs), f"Person's method {kwargs['method_name']} is missing or incorrect"


def test_residence_class_is_defined():
    assert 'Residence' in dir(housing), 'Residence class has not been defined'


@if_class_exists('Residence')
def test_residence_class_is_abstract():
    assert is_class_abstract(housing.Residence)

@if_class_exists('Residence')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'number_of_occupants',
        'abstract': False,
    },
    {
        "property_name": 'maximum_occupants',
        'abstract': False,
    },
    {
        "property_name": 'resident_names',
        'abstract': False,
    },
])
def test_residence_properties(kwargs):
    assert has_property(housing.Residence, **kwargs), f"Residence's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Residence')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'address', 'area','number_of_rooms'],
        'abstract': False,
    },
    {
        'method_name': 'register_resident',
        'parameter_names': ['self','person'],
        'abstract': False,
    },
    {
        'method_name': 'unregister_resident',
        'parameter_names': ['self','id'],
        'abstract': False,
    },
    {
        'method_name': 'calculate_value',
        'parameter_names': ['self'],
        'abstract': True,
    },
])
def test_residence_methods(kwargs):
    assert has_method(
        housing.Residence,
        **kwargs), f"Residence's method {kwargs['method_name']} is missing or incorrect"


def test_villa_class_is_defined():
    assert 'Villa' in dir(housing), 'Villa class has not been defined'


@if_class_exists('Villa')
def test_file_class_is_not_abstract():
    assert not is_class_abstract(housing.Villa)


@if_class_exists('Villa')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'address', 'area','number_of_rooms','garage_capacity'],
        'abstract': False,
    },
    {
        'method_name': 'calculate_value',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_file_methods(kwargs):
    assert has_method(
        housing.Villa,
        **kwargs), f"Villa's method {kwargs['method_name']} is missing or incorrect"


def test_directory_class_is_defined():
    assert 'StudentKot' in dir(housing), 'StudentKot class has not been defined'


@if_class_exists('StudentKot')
def test_directory_class_is_not_abstract():
    assert not is_class_abstract(housing.StudentKot)


@if_class_exists('StudentKot')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'address', 'area'],
        'abstract': False,
    },
    {
        'method_name': 'register_resident',
        'parameter_names': ['self', 'person'],
        'abstract': False,
    },
    {
        'method_name': 'calculate_value',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_directory_methods(kwargs):
    assert has_method(
        housing.StudentKot,
        **kwargs), f"StudentKot's method {kwargs['method_name']} is missing or incorrect"
