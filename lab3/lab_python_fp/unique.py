class Unique:
    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = list(data)
        self.index = 0
        self.ignore_case = False
        for key, value in kwargs.items():
            if key == 'ignore_case' and isinstance(value, bool):
                self.ignore_case = value

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                flag = False
                if self.ignore_case and isinstance(current, str):
                    for elem in self.used_elements:
                        if current.upper() == elem.upper():
                            flag = True
                            break
                    if not flag:
                        self.used_elements.add(current)
                        return current

                else:
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current