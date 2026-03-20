from src.models.task import Task

class ApiSource:

    def __init__(self, name="default"):
        self.name=name
        self.data=[
            {"id": 1001, "text": "Задача 1"},
            {"id": 1002, "text": "Задача 2"},
            {"id": 1003, "text": "Задача 3"},
        ]
    def get_tasks(self):
        tasks=[]
        for i in self.data:
            task=Task(
                id=str(i["id"]),
                payload=i["text"]
            )
            tasks.append(task)
        return tasks
