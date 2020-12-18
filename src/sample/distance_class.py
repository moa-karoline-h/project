# distance, dot- and crossproduct of vectors through class
import math
import numpy as np

class Vector():
    """numpydoc:
    A new class Vector with functions
    to calculate the distance, the dot
    and cross products of vectors.

    Attributes
    ----------
    x, y, z : 'float'
        The vectors coordinates.

    Returns
    -------
    ret1 : float
        Distance/Magnitude between two vectors
    ret2 : float
        Dot product between two vectors
    ret3 : floats
        cross product between two vectors
        three floats representing the resulting vector

    Note:
    ----
    .. _NumPy Documentation HOWTO:
        https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
    pro: Better for complex descriptions and documentation
    con: Uses more vertical space
    """


    def __init__(self, x, y, z):
        """Construction of the necessary attributes for the vector.

        Parameters
        ----------
        x, y, z : 'float'
            The vectors coordinates.
        """

        self.x = x
        self.y = y
        self.z = z

    # function for magnitude between two vectors (betrag)
    def distance(self, other):
        """Prints the distance between two vectors
        if the coordinates for the other vector is passed.

        Parameters
        ----------
        other : floats
            actually a list of floats representing vector.

        Returns
        -------
        ret1 : float
            Distance/Magnitude between two vectors
        """
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)

    def dot(self, other):
        """Prints the dot product between two vectors
        if the coordinates for the other vector is passed.

        Parameters
        ----------
        other : floats
            actually a list of floats representing vector.

        Returns
        -------
        ret1 : float
            Dot product between two vectors
        """
        return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))

    def cross(self, other):
        """Prints the cross product between two vectors
        if the coordinates for the other vector is passed.

        Parameters
        ----------
        other : floats
            actually a list of floats representing vector.

        Returns
        -------
        ret2 : floats
            cross product between two vectors
        """
        return Vector((self.y * other.z) - (self.z * other.y),
        (self.x * other.z) - (self.z * other.x),
        (self.x * other.y) - (self.y * other.x))

    # formatting output of vector
    def __repr__(self):
        """Returns the object representation. In this case string.

        Parameters
        ----------
        self : floats
            actually a list of floats representing vector.

        Returns
        -------
        ret3 : sring
            cross product between two vectors formatted.
        """
        out = "x = " + str(self.x)

        if self.y >= 0:
            out = out + "+ "
        out = out + "\n y = " + str(self.y)

        if self.z >= 0:
            out = out + "+ "
        out = out + "\n z = " + str(self.z)

        return out


if __name__ == "__main__":
    """The global variable, __name__, in the module that is the entry
    point to your program, is '__main__'.
    Otherwise, it's the name you import the module by.
    So, code under the if block will only run if the module is the
    entry point to your program.
    It allows the code in the module to be importable by other modules,
    without executing the code block beneath on import.

    Notes
    -----
    Calling the class and seperate functions and printing their values.
    """

    v1 = Vector(2.8, -4.7, 0.4)
    v2 = Vector(-8.1, 3.0, -10.6)
    value1 = v1.distance(v2)
    value2 = v1.dot(v2)
    v3 = v1.cross(v2)

    print("Value1 = ", value1, "\nValue2 = ", value2, "\nv3: \n", v3)
    print("checking vector instance of v3: ", isinstance(v3, Vector))
