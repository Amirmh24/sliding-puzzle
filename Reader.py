from PIL import Image
class Reader:
    def __init__(self, path, n):
        self.puzzleSize = 500
        self.image = Image.open(path)
        self.n = n
        size = self.image.size
        minDim = min(size[0], size[1])
        self.image = self.image.crop((0, 0, minDim, minDim))
        self.image = self.image.resize((self.puzzleSize, self.puzzleSize))
        self.savePieces()

    def savePieces(self):
        h = self.puzzleSize // self.n
        for i in range(self.n):
            for j in range(self.n):
                self.image.crop((i * h, j * h, (i + 1) * h, (j + 1) * h)).save(
                    'crops/' + str(j) + '-' + str(i) + '.jpg')
        Image.open('Images/null.jpg').resize((h, h)).save('crops/null.jpg')
