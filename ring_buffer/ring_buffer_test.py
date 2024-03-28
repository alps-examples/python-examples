from ring_buffer import *

import unittest
import time

class RingBufferTest(unittest.TestCase):
    def test_push_pop(self):
        buffer = RingBuffer(number_entries=3, number_rows=4, zeros=True)

        buffer.push_front(np.array([1, 2]), np.array([5, 6]))
        self.assertEqual(buffer.get_number_of_entries().tolist(), [0, 1, 1, 0])

        buffer.push_front(np.array([0, 1, 2, 3]), np.array([8, 4, 8, 3]))
        self.assertEqual(buffer.get_number_of_entries().tolist(), [1, 2, 2, 1])

        extracted = buffer.pop_back(np.array([2, 0]))
        self.assertEqual(extracted.tolist(), [6, 8])
        self.assertEqual(buffer.get_number_of_entries().tolist(), [0, 2, 1, 1])

        buffer.push_front(np.array([1, 3, 2]), np.array([9, 0, 4]))
        self.assertEqual(buffer.get_number_of_entries().tolist(), [0, 3, 2, 2])
        self.assertEqual(buffer.get_entries(offset=0).tolist(), [-1, 9, 4, 0])
        self.assertEqual(buffer.get_entries(offset=1).tolist(), [-1, 4, 8, 3])
        self.assertEqual(buffer.get_entries(offset=10).tolist(), [-1, -1, -1, -1])

    def test_push_back(self):
        buffer = RingBuffer(number_rows=3, number_entries=3)
        buffer.push_back(np.array([0, 1]), np.array([2, 3]))
        self.assertEqual(buffer.pop_back(np.array([1, 0])).tolist(), [3, 2])

    def test_push_front_time_complexity(self):
        R = 5
        for N in [1000, 10_000, 100_000, 1_000_000]:
            start = time.time()
            buffer = RingBuffer(number_entries=N, number_rows=R)
            for i in range(N):
                buffer.push_front(np.arange(R), 42)
            end = time.time()
            elapsed = end - start
            self.assertEqual(buffer.get_number_of_entries().tolist(), [N, N, N, N, N])
            print('Filling with {:10,d} elements takes {:.6f} s.'.format(N, elapsed))

if __name__ == '__main__':
    unittest.main(exit=False)
