# Create a blosum_matrix object

class blosum_matrix:
    def __init__(self):
        self.blosum_string = ' \
   C  S  T  P  A  G  N  D  E  Q   H  R  K  M  I  L  V  F  Y  W \
C  9 -1 -1 -3  0 -3 -3 -3 -4 -3  -3 -3 -3 -1 -1 -1 -1 -2 -2 -2 \
S -1  4  1 -1  1  0  1  0  0  0  -1 -1  0 -1 -2 -2 -2 -2 -2 -3 \
T -1  1  5 -1  0 -2  0 -1 -1 -1  -2 -1 -1 -1 -1 -1  0 -2 -2 -2 \
P -3 -1 -1  7 -1 -2 -2 -1 -1 -1  -2 -2 -1 -2 -3 -3 -2 -4 -3 -4 \
A  0  1  0 -1  4  0 -2 -2 -1 -1  -2 -1 -1 -1 -1 -1  0 -2 -2 -3 \
G -3  0 -2 -2  0  6  0 -1 -2 -2  -2 -2 -2 -3 -4 -4 -3 -3 -3 -2 \
N -3  1  0 -2 -2  0  6  1  0  0   1  0  0 -2 -3 -3 -3 -3 -2 -4 \
D -3  0 -1 -1 -2 -1  1  6  2  0  -1 -2 -1 -3 -3 -4 -3 -3 -3 -4 \
E -4  0 -1 -1 -1 -2  0  2  5  2   0  0  1 -2 -3 -3 -2 -3 -2 -3 \
Q -3  0 -1 -1 -1 -2  0  0  2  5   0  1  1  0 -3 -2 -2 -3 -1 -2 \
H -3 -1 -2 -2 -2 -2  1 -1  0  0   8  0 -1 -2 -3 -3 -3 -1  2 -2 \
R -3 -1 -1 -2 -1 -2  0 -2  0  1   0  5  2 -1 -3 -2 -3 -3 -2 -3 \
K -3  0 -1 -1 -1 -2  0 -1  1  1  -1  2  5 -1 -3 -2 -2 -3 -2 -3 \
M -1 -1 -1 -2 -1 -3 -2 -3 -2  0  -2 -1 -1  5  1  2  1  0 -1 -1 \
I -1 -2 -1 -3 -1 -4 -3 -3 -3 -3  -3 -3 -3  1  4  2  3  0 -1 -3 \
L -1 -2 -1 -3 -1 -4 -3 -4 -3 -2  -3 -2 -2  2  2  4  1  0 -1 -2 \
V -1 -2  0 -2  0 -3 -3 -3 -2 -2  -3 -3 -2  1  3  1  4 -1 -1 -3 \
F -2 -2 -2 -4 -2 -3 -3 -3 -3 -3  -1 -3 -3  0  0  0 -1  6  3  1 \
Y -2 -2 -2 -3 -2 -3 -2 -3 -2 -1   2 -2 -2 -1 -1 -1 -1  3  7  2 \
W -2 -3 -2 -4 -3 -2 -4 -4 -3 -2  -2 -3 -3 -1 -3 -2 -3  1  2 11'
        self.matrix = [ [None] * 21 for _ in range(21) ]
        self.create_matrix()

    def create_matrix(self):
        row = 0
        col = 1  # start at second index since (0,0) entry is empty
        str_index = 0

        while str_index < len(self.blosum_string):
            if self.blosum_string[str_index] == ' ':
                str_index += 1

            elif self.blosum_string[str_index + 1] == ' ':
                self.matrix[row][col] = self.blosum_string[str_index]
                str_index += 1
                col += 1
            
            elif self.blosum_string[str_index + 1] != ' ':
                # This is the case of a negative number
                # No 2 digit nevative numbers
                self.matrix[row][col] = self.blosum_string[str_index] + self.blosum_string[str_index + 1]
                str_index += 2
                col += 1
            
            if col == 21:
                row += 1
                col = 0
                str_index += 1  # for space before \


