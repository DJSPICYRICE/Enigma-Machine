rotar1 = [*"EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
rotar2 = [*"AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotar3 = [*"BDFHJLCPRTXVZNYEIWGAKMUSQO"]
rotar1stright = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotar2stright = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotar3stright = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
strightletters = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
reflector = [*"EJMZALYXVBWFCRQUONTSPIKHGD"]
rotar1notch = 16
rotar2notch = 5
rotar3notch = 21
rotar1position = 0
rotar2position = 0
rotar3position = 0
output = ""
plugboardto = []
plugboardfrom = []


def getplugboard():
    print('First you must enter your plugboard substutions.')
    print('You can do 10 different assignments to your plugboard.')
    print('You can also only use each letter once.')
    for i in range(1, 11):
        temp = input(f'Enter plugboard assignment number {i} (example:A->B): ').upper()
        if temp == 'NONE':
            break
        else:
            temp = [*temp]
            plugboardto.append(temp[0])
            plugboardfrom.append(temp[-1])


def plugboard(enter):
    global plugboardto, plugboardfrom
    if enter in plugboardto:
        enter = plugboardfrom[plugboardto.index(enter)]
    elif enter in plugboardfrom:
        enter = plugboardto[plugboardfrom.index(enter)]


def rotate(rotar, stright, position):
    rotar.append(rotar.pop(0))
    stright.append(stright.pop(0))
    position = stright.index("A")
    return position


def encode(r1, r2, r3, x):
    global rotar3position
    global rotar2position
    global rotar1position
    global strightletters
    if x not in strightletter:
        if x == ' ':
            x = 'X'
        rotar3position = rotate(rotar3, rotar3stright, rotar3position)
        if rotar3position == rotar2notch:
            rotar2position = rotate(rotar2,rotar2stright, rotar2position)
        if rotar2position == rotar1notch:
            rotar1position = rotate(rotar1,rotar1stright,rotar1position)
        x = r3[strightletters.index(x)]
        x = r2[rotar3stright.index(x)]
        x = r1[rotar2stright.index(x)]

        x = reflector[rotar1stright.index(x)]
        x = reflector[strightletters.index(x)]

        x = rotar1stright[reflector.index(x)]
        x = rotar2stright[r1.index(x)]
        x = rotar3stright[r2.index(x)]
        x = strightletters[r3.index(x)]
    return x

