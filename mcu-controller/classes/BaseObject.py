class BaseObject:
    createdObjects = [] # Intentional assignment

    def __init__(self):
        self.createdObjects.append(self)

    def update(deltaTime):
        pass