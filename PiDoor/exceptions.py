

class ActionNotFoundException(Exception):
    def __str__(self):
        return 'Action not found: ' + Exception.__str__(self)

class LightIndexNotFoundException(Exception):
    def __str__(self):
        return 'No light found with index: ' + Exception.__str__(self)