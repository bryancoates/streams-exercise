""" Class to handle processing a stream of numbers """

class StreamProcessor(object):
    """ Processes a stream of numbers """

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """ Count and sum two digit numbers from a stream """

        count = 0
        total = 0

        while total < 200 and count < 10:
            digits = self._stream.read(2)
            if len(digits) < 2:
                break
            
            number = int(digits)
                
            total += number
            
            count += 1

        return count
