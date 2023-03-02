class Store:
    data = {}

    def dset(self, block, key, value):
        if not (block in self.data):
            self.data[block] = {}

        self.data[block][key] = value

    def dget(self, block, key):
        try:
            return self.data[block][key]
        except:
            return None
