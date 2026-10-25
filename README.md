# Enigma Machine (Python)

A Python simulator of the WWII **Enigma I** cipher machine, translated from my original Code.org App Lab (JavaScript) version. Type a message and it's scrambled letter by letter through three rotors and a reflector, using the historical rotor wirings. Because Enigma is symmetric, running the scrambled text back through gives you the original message.

Made by Mouli Grandhi.

> The JavaScript (App Lab) version and its demo video are on the [`main`](https://github.com/DJSPICYRICE/Enigma-Machine/tree/main) branch.

## Running it

```bash
python enigma.py
```

Type a message and press Enter. To decode, run it again and enter the scrambled text.

## Example

```
Input:   Meet at 55 Main St., 9pm!
Prepped: MEETXATXFIVEXFIVEXMAINXSTXNINEPM
Encoded: DLCFTWHABURTMDZOTBLBGVPPKAZVDOKV
Decoded: MEETXATXFIVEXFIVEXMAINXSTXNINEPM
```

## How it works

1. **Preparing the text**: like real Enigma operators did, spaces become `X`, digits are spelled out (`55` becomes `FIVEXFIVE`), and punctuation is dropped.
2. **Rotors**: each letter passes through three historical Enigma I rotors:
   - Rotor I: `EKMFLGDQVZNTOWYHXUSPAIBRCJ`
   - Rotor II: `AJDKSIRUXBLHWTMCQGZNPYFVOE`
   - Rotor III: `BDFHJLCPRTXVZNYEIWGAKMUSQO`
3. **Reflector**: the signal bounces off Reflector B (`YRUHQSLDPXNGOKMIEBFZCWVJAT`) and goes back through the rotors in reverse.
4. **Stepping**: the right rotor turns before every letter, and turnover notches advance the next rotor. This is why the same letter typed twice comes out different.
