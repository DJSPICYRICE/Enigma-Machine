# Simple Enigma Machine - Python translation of the App Lab (JavaScript) version

# variables are declared
straight_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
r1_straight = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
r2_straight = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
r3_straight = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
roter1 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
roter2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
roter3 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
reflector = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")

r1_offset = 0
r2_offset = 0
r3_offset = 0
roter2_notch = 5
roter3_notch = 22


# this function "rotates" the roters
def rotate(roter, straight, offset):
    roter.append(roter.pop(0))
    straight.append(straight.pop(0))
    offset = straight_letters.index(straight[0])
    return offset


# this function changes the letters based on historical enigma roters
def encode(r1, r2, r3, letter):
    global r1_offset, r2_offset, r3_offset
    if letter == " ":
        return " "

    r3_offset = rotate(roter3, r3_straight, r3_offset)
    if r3_offset == roter3_notch:
        r2_offset = rotate(roter2, r2_straight, r2_offset)
    if r2_offset == roter2_notch:
        r1_offset = rotate(roter1, r1_straight, r1_offset)

    letter = r3[straight_letters.index(letter)]
    letter = r2[r3_straight.index(letter)]
    letter = r1[r2_straight.index(letter)]

    letter = reflector[r1_straight.index(letter)]
    letter = reflector[straight_letters.index(letter)]

    letter = r1_straight[reflector.index(letter)]
    letter = r2_straight[r1.index(letter)]
    letter = r3_straight[r2.index(letter)]
    letter = straight_letters[r3.index(letter)]
    return letter


if __name__ == "__main__":
    text = input("Enter text: ").upper()
    output = ""
    for ch in text:
        output += encode(roter1, roter2, roter3, ch)
    print(output)
