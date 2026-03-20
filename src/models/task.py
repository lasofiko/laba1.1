class Task:
    def __init__(self, id, payload):
        self.id=id
        self.payload=payload
    def __repr__(self):
        return f"Task(id={self.id}. payload='{self.payload}')"
