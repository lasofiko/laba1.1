from src.sources.file_source import FileSource
from src.sources.generate_source import Generate
from src.processors.task_processor import TaskProcessor
from src.sources.api_source import ApiSource


def main():
    p= TaskProcessor()

    file_source = FileSource("data/tasks.txt")
    p.process(file_source)

    gen_source = Generate(5)
    p.process(gen_source)

    api_sources=ApiSource("источник")
    p.process(api_sources)

if __name__ == "__main__":
    main()