import numpy as np

numTilings = 8


def tilecode(in1, in2, tileIndices):
    # write your tilecoder here (5 lines or so)
    offset = ((1/numTilings) * 0.6) * np.arange(numTilings)
    x = np.floor((in1 + offset)/0.6).astype(int)
    y = (np.floor((in2 + offset)/0.6)*11).astype(int)
    tileIndices[:] = np.floor(121 * np.arange(numTilings) + x + y).astype(int)


def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2,') are : ', tileIndices)


def testTileCoder():
    printTileCoderIndices(0.1, 0.1)
    printTileCoderIndices(4.0, 2.0)
    printTileCoderIndices(5.99, 5.99)
    printTileCoderIndices(4.0, 2.1)


if __name__ == '__main__':
    testTileCoder()