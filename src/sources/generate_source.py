from src.models.task import Task
import random

class Generate:
    tasks = [
        "обработать данные",
        "отправить отчет",
        "проверить статус",
        "обновить компьютер",
        "установить программу",
        "загрузить файл",
        "отправить письмо"
    ]

    def __init__(self, cnt=None):
        if cnt is None:
            self.cnt = random.randint(1, 7)
        else:
            self.cnt = cnt

    def _get_task_text(self):
        return random.choice(self.tasks)

    def get_tasks(self):
        print(f"Generating {self.cnt} tasks")
        tk = []
        for i in range(1, self.cnt + 1):
            task_text = self._get_task_text()
            task = Task(
                id=f"{i}",
                payload=f"{task_text}"
            )
            tk.append(task)
        return tk