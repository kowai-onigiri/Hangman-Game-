import random
import dictionary
import hangmanart

word_list = dictionary.word_bank

#choose a mystery word
bank_length = len(word_list)
rand_select = random.randint(0, (bank_length - 1))

chosen_word = word_list[rand_select].lower()
length = len(chosen_word)


def play():

  def play_again():
    choice = input("Do you want to play again? ").lower()
    if choice == "yes":
      play()

  #display word with blanks
  display = []
  for char in chosen_word:
    display += "_"

  letter_bank = ""
    

  #end of game conditions
  
  end_of_game = False
  lives = 6
  stage = 6
  
  #game
  print("=================================================")
  print("-------------------------------------------------")
  print("=================================================")
  print(hangmanart.logo)
  print("=================================================")
  print("-------------------------------------------------")
  print("=================================================")
  
  print(" ")
  print(" ")
  
  while not end_of_game:
  
    #guess
    letter = input("Guess a letter: ").lower()
    print(" ")
    print("-------------------")
    print(" ")
  
    for position in range(length):
      guess = chosen_word[position]
      if guess == letter:
        print("Good choice!!")
        display[position] = guess
        print(" ")
        print(f"LETTER BANK: {letter_bank}")
  
    if letter not in chosen_word:
      print("Bad choice!!")
      letter_bank += letter + " "
      print(" ")
      print(f"LETTER BANK: {letter_bank}")
      lives -= 1
      stage -= 1
      
    print(" ")
    print(hangmanart.stages[stage])
    print("-------------------")
    print(" ")
    print("What is the word?")
    print(" ")
    print(f"{' '.join(display)}")
    print(" ")
    print(f"Lives left: {lives}")
    print(" ")
    print("-------------------")
    print("===================")
    print("-------------------")
    print(" ")
  
    if lives == 0:
      end_of_game = True
      print("You Lose!")
      print(" ")
      print(f"The correct word was'{chosen_word}'!")
      print(hangmanart.sad)
      play_again()
      
  
    
    #game win condition
    
    print(" ")
    if "_" not in display:
      end_of_game = True
      print("You Win!")
      print(" ")
      print(hangmanart.happy)
      print(" ")
      print(f"The correct word was '{chosen_word}'!")
      print(" ")
      play_again()
      print(" ")


  
play()