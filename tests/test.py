import pytest
import tempfile
import os
from src.models.task import Task
from src.protocols.source_protocol import TaskSource
from src.sources.file_source import FileSource
from src.sources.generate_source import Generate
from src.sources.api_source import ApiSource
from src.processors.task_processor import TaskProcessor


@pytest.fixture
def temp_file():
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        f.write("задача 1\n")
        f.write("задача 2\n")
        f.write("задача 3\n")
        path = f.name
    yield path
    os.unlink(path)


@pytest.fixture
def processor():
    return TaskProcessor()


def test_task_creation():
    task = Task("1", "тест")
    assert task.id == "1"
    assert task.payload == "тест"


def test_protocol_compliance():
    assert isinstance(FileSource("dummy.txt"), TaskSource)
    assert isinstance(Generate(), TaskSource)
    assert isinstance(ApiSource(), TaskSource)
    assert not isinstance("строка", TaskSource)


def test_file_source_reads_file(temp_file):
    source = FileSource(temp_file)
    tasks = source.get_tasks()
    assert len(tasks) == 3
    assert tasks[0].payload == "задача 1"
    assert tasks[1].payload == "задача 2"
    assert tasks[2].payload == "задача 3"


def test_file_source_not_found():
    source = FileSource("nonexistent.txt")
    tasks = source.get_tasks()
    assert len(tasks) == 3
    assert tasks[0].payload == "test 1"


def test_generator_source_default():

    source = Generate()
    tasks = source.get_tasks()
    assert 1 <= len(tasks) <= 10
    assert isinstance(tasks[0].id, str)
    assert tasks[0].payload != ""


def test_generator_source_with_count():
    source = Generate(3)
    tasks = source.get_tasks()
    assert len(tasks) == 3
    assert tasks[0].id == "1"
    assert tasks[1].id == "2"
    assert tasks[2].id == "3"


def test_api_source():
    source = ApiSource()
    tasks = source.get_tasks()
    assert len(tasks) == 3
    assert tasks[0].id == "1001"
    assert tasks[0].payload == "Задача 1"


def test_api_source_with_name():
    source = ApiSource("weather")
    assert source.name == "weather"
    tasks = source.get_tasks()
    assert len(tasks) == 3


def test_processor_with_valid_source(processor):
    source = Generate(2)
    processor.process(source)


def test_processor_with_invalid_source(processor):
    processor.process("строка")


def test_processor_output(capsys):
    processor = TaskProcessor()
    source = Generate(2)
    processor.process(source)
    captured = capsys.readouterr()
    assert "passed verification" in captured.out
    assert "Get 2 tasks" in captured.out