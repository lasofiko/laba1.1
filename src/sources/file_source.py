from src.models.task import Task
class FileSource:
    def __init__(self,f):
        self.f=f
    def get_tasks(self):
        try:
            with open(self.f,'r',encoding='utf-8') as file:
                tasks=[]
                for n,l in enumerate(file,1):
                    l=l.strip()
                    if l:
                        tasks.append(Task(str(n),l))
                return tasks
        except FileNotFoundError:
            print(f"file {self.f} not found. Return tests")
            return [
                Task("1","test 1"),
                Task("2","test 2"),
                Task("3","test 3")
            ]
