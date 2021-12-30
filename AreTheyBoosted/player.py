class Player:
    def __init__(self, name=None, uuid=None):
        self.name = name
        self.uuid = uuid

    def get_rank(self):
        if isinstance(self.name, None):
            return None
