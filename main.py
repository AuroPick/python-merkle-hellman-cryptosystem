from random import randint

def createSuperincreasingSequence():
  sequence = [1]

  for _ in range(7):
    sequence.append(sum(sequence) + randint(1, 100))

  return sequence

def convertToBinary(string):
  binary = []

  for word in string:
    temp = []

    for char in word:
      temp.append("".join(format(ord(b), '08b') for b in char))

    binary.append(temp)

  return binary

def convertToString(binaryString):
  string = []

  for word in binaryString:
    temp = ""

    for char in word:
      temp += (chr(int(char, 2)))

    string.append(temp)

  return string

def formatMessage(message, type):
  string = ""

  if type == "binary":
    for word in message:
      wordTemp = ""

      for char in word:
        wordTemp += str(char)
    
      string = "{} {}".format(string, wordTemp).strip()

  elif type == "string":
    for word in message:
      string = "{} {}".format(string, word).strip()

  return string

def modInverse(a, m):

  for x in range(1, m):
    if (((a % m) * (x % m)) % m == 1):
      return x

def createKey():
  sequence = createSuperincreasingSequence()
  publicKey = []

  randInt1 = sum(sequence) + randint(1, 100)
  randInt2 = randInt1 - 1

  for i in range(8):
    publicKey.append((sequence[i] * randInt2) % randInt1)

  return sequence, publicKey, randInt1, randInt2

def encrypt(message, publicKey):
  encrypted = []

  for word in message:
    wordTemp = []

    for char in word:
      result = 0

      for i, bit in enumerate(char):
        result += int(bit) * publicKey[i]

      wordTemp.append(result)

    encrypted.append(wordTemp)
  
  return encrypted

def decrypt(message, sequence, randInt1, randInt2):
  inverse = modInverse(randInt2, randInt1)

  decrypted = []

  for word in message:
    wordTemp = []

    for char in word:
      moduled = (char * inverse) % randInt1
      charTemp = ""

      for i in range(7, -1, -1):
        if moduled >= sequence[i]:
          moduled -= sequence[i]
          charTemp += '1'
        else:
          charTemp += '0'

      wordTemp.append(charTemp[::-1])
    
    decrypted.append(wordTemp)
  
  return decrypted

if __name__ == "__main__":
  message = input().split()

  sequence, publicKey, randInt1, randInt2 = createKey()

  binaryMessage = convertToBinary(message)

  encrypted = encrypt(binaryMessage, publicKey)

  print("\nEncrypted message \"{}\"\n".format(formatMessage(encrypted, "binary")))

  decrypted = decrypt(encrypted, sequence, randInt1, randInt2)

  stringMessage = convertToString(decrypted)

  print("Decrypted message \"{}\"".format(formatMessage(stringMessage, "string")))
