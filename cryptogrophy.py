#Kade Donohoue
#5/22/23
#Hello World Script

def main():
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   key = 3
   newMessage = ''
   message = input("What message would you like to encrypt? : ")
   for character in message:
      position = alphabet.find(character)
      newPosition = (position + key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
   print("Your encrypted message is: ", newMessage)
main()