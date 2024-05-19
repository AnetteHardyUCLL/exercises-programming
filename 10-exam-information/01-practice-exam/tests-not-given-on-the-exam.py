import pytest
import filesystem
import string


VALID_ENTITY_NAMES = (*string.ascii_letters, *string.digits, '.', '0123456789abcdef', 'test.txt')
INVALID_ENTITY_NAMES = ('', '0123456789abcdefg', 'abc def', 'x_y', 'a-b')


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(filesystem), reason=f'Skipped because {class_name} has not been defined')


def create_storage_device(*, block_count=100, block_size=20):
    return filesystem.StorageDevice(block_count=block_count, block_size=block_size)


def create_file(*, storage=None, name=None, size_in_blocks=0):
    storage = storage or create_storage_device()
    name = name or VALID_ENTITY_NAMES[0]
    file = filesystem.File(storage, name)
    if size_in_blocks:
        file.grow(size_in_blocks)
    return file


def create_directory(*, storage=None, name=None):
    storage = storage or create_storage_device()
    name = name or VALID_ENTITY_NAMES[0]
    return filesystem.Directory(storage, name)


@if_class_exists('StorageDevice')
@pytest.mark.parametrize('block_count', range(1, 11))
@pytest.mark.parametrize('block_size', range(1, 11))
def test_storage_creation(block_count, block_size):
    # Act
    storage = filesystem.StorageDevice(block_count=block_count, block_size=block_size)

    # Assert
    assert storage.total_block_count == block_count
    assert storage.available_block_count == block_count
    assert storage.used_block_count == 0
    assert storage.block_size == block_size


@if_class_exists('StorageDevice')
@pytest.mark.parametrize('block_count', range(1, 101))
def test_storage_allocation(block_count):
    # Arrange
    storage_size = 100
    block_size = 5
    storage = filesystem.StorageDevice(block_count=storage_size, block_size=block_size)

    # Act
    allocated_blocks = storage.allocate(block_count=block_count)

    # Assert
    assert len(allocated_blocks) == block_count
    assert storage.total_block_count == storage_size
    assert storage.available_block_count == storage_size - block_count
    assert storage.used_block_count == block_count


@if_class_exists('StorageDevice')
@pytest.mark.parametrize('storage_size, allocation_sizes', [
    (
        10,
        [11]
    ),
    (
        10,
        [2, 4, 5]
    ),
])
def test_storage_allocation_failing_due_to_out_of_storage(storage_size, allocation_sizes):
    # Arrange
    storage = filesystem.StorageDevice(block_count=storage_size, block_size=5)
    for size in allocation_sizes[:-1]:
        storage.allocate(size)

    # Act/Assert
    with pytest.raises(RuntimeError):
        storage.allocate(allocation_sizes[-1])


@if_class_exists('StorageDevice')
@pytest.mark.parametrize('freed_block_count', range(1, 21))
def test_storage_free(freed_block_count):
    # Arrange
    storage_size = 100
    block_size = 5
    allocated_block_count = 20
    storage = filesystem.StorageDevice(block_count=storage_size, block_size=block_size)
    allocated_blocks = storage.allocate(allocated_block_count)
    to_be_freed = allocated_blocks[:freed_block_count]

    # Act
    storage.free(blocks=to_be_freed)

    # Assert
    assert storage.available_block_count == storage_size - allocated_block_count + freed_block_count
    assert storage.used_block_count == allocated_block_count - freed_block_count


@if_class_exists('StorageDevice')
def test_storage_free_fails_when_freeing_unallocated_block():
    # Arrange
    storage_size = 100
    block_size = 5
    storage = filesystem.StorageDevice(block_count=storage_size, block_size=block_size)

    # Act/Assert
    with pytest.raises(RuntimeError):
        storage.free(blocks=[0])


@if_class_exists('StorageDevice')
def test_storage_free_fails_when_freeing_same_blocks_twice():
    # Arrange
    storage_size = 100
    block_size = 5
    allocation_size = 10
    storage = filesystem.StorageDevice(block_count=storage_size, block_size=block_size)
    allocated_blocks = storage.allocate(allocation_size)
    storage.free(blocks=allocated_blocks)

    # Act/Assert
    with pytest.raises(RuntimeError):
        storage.free(blocks=allocated_blocks)


@if_class_exists('Entity')
@pytest.mark.parametrize('name, expected', [
    *(
        (name, True)
        for name in VALID_ENTITY_NAMES
    ),
    *(
        (name, False)
        for name in INVALID_ENTITY_NAMES
    ),
])
def test_entity_is_valid_name(name, expected):
    # Act
    actual = filesystem.Entity.is_valid_name(name)

    # Assert
    assert expected == actual


@if_class_exists('File')
@pytest.mark.parametrize('valid_file_name', VALID_ENTITY_NAMES)
def test_file_creation(valid_file_name):
    # Arrange
    storage = create_storage_device()

    # Act
    file = filesystem.File(storage=storage, name=valid_file_name)

    # Assert
    assert file.name == valid_file_name
    assert file.storage is storage
    assert file.size_in_blocks == 0
    assert file.size_in_bytes == 0


@if_class_exists('File')
@pytest.mark.parametrize('invalid_file_name', INVALID_ENTITY_NAMES)
def test_file_creation_failure_due_to_invalid_name(invalid_file_name):
    # Arrange
    storage = create_storage_device()

    # Act/Assert
    with pytest.raises(RuntimeError):
        filesystem.File(storage=storage, name=invalid_file_name)


@if_class_exists('File')
@pytest.mark.parametrize('valid_name', VALID_ENTITY_NAMES)
def test_file_rename_to_valid_name(valid_name):
    # Arrange
    file = create_file()

    # Act
    file.name = valid_name

    # Assert
    assert file.name == valid_name


@if_class_exists('File')
@pytest.mark.parametrize('invalid_name', INVALID_ENTITY_NAMES)
def test_file_rename_to_invalid_name(invalid_name):
    # Arrange
    file = create_file()

    # Act/Assert
    with pytest.raises(RuntimeError):
        file.name = invalid_name


@if_class_exists('File')
@pytest.mark.parametrize('grow_block_count', range(1, 11))
@pytest.mark.parametrize('storage_block_count', [10, 100, 213])
@pytest.mark.parametrize('storage_block_size', [5, 10, 100, 213])
def test_file_grow(grow_block_count, storage_block_count, storage_block_size):
    # Arrange
    storage = create_storage_device(block_count=storage_block_count, block_size=storage_block_size)
    file = create_file(storage=storage)

    # Act
    file.grow(grow_block_count)

    # Assert
    assert file.size_in_blocks == grow_block_count
    assert file.size_in_bytes == grow_block_count * storage_block_size
    assert storage.available_block_count == storage_block_count - grow_block_count
    assert storage.used_block_count == grow_block_count


@if_class_exists('File')
@pytest.mark.parametrize('grow_block_counts', [
    [1],
    [5],
    [1, 1, 1, 1, 1],
    [2, 2, 4],
])
@pytest.mark.parametrize('storage_block_count', [10, 100, 213])
@pytest.mark.parametrize('storage_block_size', [5, 10, 100, 213])
def test_file_clear(grow_block_counts, storage_block_count, storage_block_size):
    # Arrange
    storage = create_storage_device(block_count=storage_block_count, block_size=storage_block_size)
    file = create_file(storage=storage)
    for grow_block_count in grow_block_counts:
        file.grow(grow_block_count)

    # Act
    file.clear()

    # Assert
    assert file.size_in_blocks == 0
    assert file.size_in_bytes == 0
    assert storage.available_block_count == storage_block_count
    assert storage.used_block_count == 0


@if_class_exists('Directory')
@pytest.mark.parametrize('valid_directory_name', VALID_ENTITY_NAMES)
def test_directory_creation(valid_directory_name):
    # Arrange
    storage = create_storage_device()

    # Act
    directory = filesystem.Directory(storage=storage, name=valid_directory_name)

    # Assert
    assert directory.name == valid_directory_name
    assert directory.storage is storage
    assert directory.size_in_blocks == 0
    assert directory.size_in_bytes == 0


@if_class_exists('Directory')
@pytest.mark.parametrize('invalid_directory_name', INVALID_ENTITY_NAMES)
def test_directory_creation_failure_due_to_invalid_name(invalid_directory_name):
    # Arrange
    storage = create_storage_device()

    # Act/Assert
    with pytest.raises(RuntimeError):
        filesystem.Directory(storage=storage, name=invalid_directory_name)


@if_class_exists('Directory')
@pytest.mark.parametrize('valid_name', VALID_ENTITY_NAMES)
def test_file_rename_to_valid_name(valid_name):
    # Arrange
    directory = create_directory()

    # Act
    directory.name = valid_name

    # Assert
    assert directory.name == valid_name


@if_class_exists('Directory')
@pytest.mark.parametrize('invalid_name', INVALID_ENTITY_NAMES)
def test_file_rename_to_invalid_name(invalid_name):
    # Arrange
    directory = create_directory()

    # Act/Assert
    with pytest.raises(RuntimeError):
        directory.name = invalid_name


@if_class_exists('Directory')
@pytest.mark.parametrize("storage_size_in_blocks", [10, 50, 123])
@pytest.mark.parametrize("storage_block_size", [1, 5, 452])
@pytest.mark.parametrize("file_size_in_blocks", range(1, 11))
def test_directory_add_file(storage_size_in_blocks, storage_block_size, file_size_in_blocks):
    # Arrange
    storage = create_storage_device(block_count=storage_size_in_blocks, block_size=storage_block_size)
    directory = create_directory(storage=storage)
    file = create_file(storage=storage, size_in_blocks=file_size_in_blocks)

    # Act
    directory.add(file)

    # Assert
    assert directory.size_in_blocks == file_size_in_blocks
    assert directory.size_in_bytes == file_size_in_blocks * storage_block_size
    assert storage.available_block_count == storage.total_block_count - file_size_in_blocks
    assert storage.used_block_count == file_size_in_blocks


@if_class_exists('Directory')
@pytest.mark.parametrize("storage_block_size", [1, 5, 452])
@pytest.mark.parametrize('file_size_in_blocks', [1, 2, 3, 4, 5])
def test_directory_subdirectories(storage_block_size, file_size_in_blocks):
    # Arrange
    storage = create_storage_device(block_size=storage_block_size, block_count=1000)
    directory = create_directory(storage=storage)
    subdirectory1 = create_directory(storage=storage)
    subdirectory2 = create_directory(storage=storage)
    files = [create_file(storage=storage, size_in_blocks=file_size_in_blocks) for _ in range(5)]

    # Act
    directory.add(subdirectory1)
    directory.add(subdirectory2)
    subdirectory1.add(files[0])
    subdirectory1.add(files[1])
    subdirectory2.add(files[2])
    subdirectory2.add(files[3])
    subdirectory2.add(files[4])

    # Assert
    assert directory.size_in_blocks == file_size_in_blocks * len(files)
    assert directory.size_in_bytes == file_size_in_blocks * len(files) * storage_block_size


@if_class_exists('Directory')
@pytest.mark.parametrize("storage_size_in_blocks", [10, 50, 123])
@pytest.mark.parametrize("storage_block_size", [1, 5, 452])
@pytest.mark.parametrize("file_size_in_blocks", range(1, 11))
def test_directory_clear(storage_size_in_blocks, storage_block_size, file_size_in_blocks):
    # Arrange
    storage = create_storage_device(block_count=storage_size_in_blocks, block_size=storage_block_size)
    directory = create_directory(storage=storage)
    file = create_file(storage=storage, size_in_blocks=file_size_in_blocks)
    directory.add(file)

    # Act
    directory.clear()

    # Assert
    assert directory.size_in_blocks == 0
    assert directory.size_in_bytes == 0
    assert file.size_in_blocks == 0
    assert file.size_in_bytes == 0
    assert storage.available_block_count == storage.total_block_count
    assert storage.used_block_count == 0


@if_class_exists('Directory')
@pytest.mark.parametrize("storage_block_size", [1, 5, 452])
@pytest.mark.parametrize('file_size_in_blocks', [1, 2, 3, 4, 5])
def test_directory_clear_hierarchy(storage_block_size, file_size_in_blocks):
    # Arrange
    storage = create_storage_device(block_size=storage_block_size, block_count=1000)
    directory = create_directory(storage=storage)
    subdirectory1 = create_directory(storage=storage)
    subdirectory2 = create_directory(storage=storage)
    files = [create_file(storage=storage, size_in_blocks=file_size_in_blocks) for _ in range(5)]
    directory.add(subdirectory1)
    directory.add(subdirectory2)
    subdirectory1.add(files[0])
    subdirectory1.add(files[1])
    subdirectory2.add(files[2])
    subdirectory2.add(files[3])
    subdirectory2.add(files[4])
    entities = [directory, subdirectory1, subdirectory2, *files]

    # Act
    directory.clear()

    # Assert
    assert all(entity.size_in_blocks == 0 for entity in entities)
    assert all(entity.size_in_bytes == 0 for entity in entities)
