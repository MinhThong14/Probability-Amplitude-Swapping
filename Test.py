import unittest

from Amplitude_Swapping_Implementation import swappingAmplitude
from Amplitude_Swapping_Implementation import maxNumBits
from Amplitude_Swapping_Implementation import numBits
from Amplitude_Swapping_Implementation import extendBitString 

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import Statevector

class TestGenerators(unittest.TestCase):
    def test_01(self):
        """
        Input: x = 126 (sv_x = |0111111⟩), y = 93 (sv_y = |1011101⟩z = 7)
        Expected output: sv_x = |1011101⟩ , sv_y = |0111111⟩
        """
        x = 126
        y = 93
        z = 7


        # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)

    def test_02(self):
        """
        Input: x = 0 (sv_x = |0⟩), y = 0 (sv_y = |0⟩)
        Expected output: sv_x = |0⟩ , sv_y = |0⟩
        """
        x = 0
        y = 0
        z = 5

        # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)

    def test_03(self):
        """
        Input: x = 5 (sv_x = |1010⟩), y = 15 (sv_y = |1111⟩)
        Expected output: sv_x = |1111⟩ , sv_y = |1010⟩
        """
        x = 5
        y = 15
        z = 0

        # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)

    def test_04(self):
        """
        Input: x = 0 (sv_x = |0000000⟩), y = 100 (sv_y = |0010011⟩)
        Expected output: sv_x = |0010011⟩ , sv_y = |0000000⟩
        """
        x = 0
        y = 100
        z = 11

         # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)
    
    def test_05(self):
        """
        Input: x = 20 (sv_x = |00101⟩), y = 2 (sv_y = |01000⟩)
        Expected output: sv_x = |01000⟩ , sv_y = |00101⟩
        """
        x = 20
        y = 2
        z = 5

        # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)

    def test_06(self):
        """
        Input: x = 1000 (sv_x = |0001011111⟩), y = 87 (sv_y = |1110101000⟩)
        Expected output: sv_x = |1110101000⟩ , sv_y = |0001011111⟩
        """
        x = 1000
        y = 87
        z = 110

        # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)
    
    def test_07(self):
        """
        Input: x = 10000 (sv_x = |0011111010101⟩), y = 11000 (sv_y = |0101100010111⟩)
        Expected output: sv_x = |0101100010111⟩ , sv_y = |0011111010101⟩
        """
        x = 5500
        y = 7450
        z = 3560

        # The number of qubit is the length of the longest bitstring among 2 numbers
        n = maxNumBits(x, y)

        bitStringX = "{0:b}".format(x)
        bitStringY = "{0:b}".format(y)
        bitStringZ = "{0:b}".format(z)


        
        # Matching the bit string length
        if numBits(x) > numBits(y):
            bitStringY = extendBitString(bitStringY, n)
        elif numBits(x) < numBits(y):
            bitStringX = extendBitString(bitStringX, n)
        
        if numBits(z) < n:
            bitStringZ = extendBitString(bitStringZ, n)

        sv_x_original = Statevector.from_label(bitStringX[::-1])
        sv_y_original = Statevector.from_label(bitStringY[::-1])
        sv_z_original = Statevector.from_label(bitStringZ[::-1])

        circ, sv_x, sv_y = swappingAmplitude(x, y)
        sv_z = sv_z_original.evolve(circ)

        self.assertEqual(sv_y_original, sv_x)
        self.assertEqual(sv_x_original, sv_y)
        self.assertEqual(sv_z_original, sv_z)

    # def test_08(self):
    #     """
    #     Input: x = 1256 (sv_x = |1010001010100111⟩), y = 58693 (sv_y = |0001011100100000⟩)
    #     Expected output: sv_x = |0001011100100000⟩, sv_y = |1010001010100111⟩
    #     """
    #     x = 1256
    #     y = 58693

    #     # The number of qubit is the length of the longest bitstring among 2 numbers
    #     n = maxNumBits(x, y)

    #     bitStringX = "{0:b}".format(x)
    #     bitStringY = "{0:b}".format(y)
    #     # Matching the bit string length
    #     if numBits(x) > numBits(y):
    #         bitStringY = extendBitString(bitStringY, n)
    #     elif numBits(x) < numBits(y):
    #         bitStringX = extendBitString(bitStringX, n)

    #     sv_x_original = Statevector.from_label(bitStringX[::-1])
    #     sv_y_original = Statevector.from_label(bitStringY[::-1])

    #     circ, sv_x, sv_y = swappingAmplitude(x, y)

    #     self.assertEqual(sv_y_original, sv_x)
    #     self.assertEqual(sv_x_original, sv_y)

    # def test_09(self):
    #     """
    #     Input: x = 0 (sv_x = ), y = 78935 (sv_y = )
    #     Expected output: sv_x =  , sv_y = 
    #     """
    #     x = 0
    #     y = 78935

    #     # The number of qubit is the length of the longest bitstring among 2 numbers
    #     n = maxNumBits(x, y)

    #     bitStringX = "{0:b}".format(x)
    #     bitStringY = "{0:b}".format(y)
    #     # Matching the bit string length
    #     if numBits(x) > numBits(y):
    #         bitStringY = extendBitString(bitStringY, n)
    #     elif numBits(x) < numBits(y):
    #         bitStringX = extendBitString(bitStringX, n)

    #     sv_x_original = Statevector.from_label(bitStringX[::-1])
    #     sv_y_original = Statevector.from_label(bitStringY[::-1])

    #     circ, sv_x, sv_y = swappingAmplitude(x, y)

    #     self.assertEqual(sv_y_original, sv_x)
    #     self.assertEqual(sv_x_original, sv_y)

    # def test_10(self):
    #     """
    #     Input: x = 125635 (sv_x = |11000011010101111⟩), y = 45638 (sv_y = |01100010010011010⟩)
    #     Expected output: sv_x = |01100010010011010⟩, sv_y = |11000011010101111⟩
    #     """
    #     x = 125635
    #     y = 45638

    #     # The number of qubit is the length of the longest bitstring among 2 numbers
    #     n = maxNumBits(x, y)

    #     bitStringX = "{0:b}".format(x)
    #     bitStringY = "{0:b}".format(y)
    #     # Matching the bit string length
    #     if numBits(x) > numBits(y):
    #         bitStringY = extendBitString(bitStringY, n)
    #     elif numBits(x) < numBits(y):
    #         bitStringX = extendBitString(bitStringX, n)

    #     sv_x_original = Statevector.from_label(bitStringX[::-1])
    #     sv_y_original = Statevector.from_label(bitStringY[::-1])

    #     circ, sv_x, sv_y = swappingAmplitude(x, y)

    #     self.assertEqual(sv_y_original, sv_x)
    #     self.assertEqual(sv_x_original, sv_y)
    
if __name__ == "__main__":
    unittest.main()