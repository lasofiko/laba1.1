from src.protocols.source_protocol import TaskSource

class TaskProcessor:

    def process(self,source):

        if not isinstance(source, TaskSource):
            print(f"Error. {type(source).__name__} doesnt comply with the contract")
            return
        print(f"{type(source).__name__} passed verification")

        try:
            tasks= source.get_tasks()
        except Exception as e:
            print(f"Error when receiving tasks: {e}")
            return

        print(f"Get {len(tasks)} tasks")

        for t in tasks:
            print(f"Task {t.id}: {t.payload}")


