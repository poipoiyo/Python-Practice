# Game start

# Read quesiton (1000 words)
  # Choose 1 of them, and get it's length
  # EX. cat -> _ _ _
def ReadQuesion() -> str:
    # read xxx file
    # pick one
    # record index ...

# Initialize 
  # You can guess 6 times
  # Enter player's name

# Start guessing
  # Enter 1 letter, and check if it matches question
    # Yes -> display that, EX. c _ _
    # No -> minus 1 life, and list the letter
    # Special words, ex. `exit!`, goto Game over
    #### Special words, ex. `show!`, show your name and highest record
  
  # After every guess, check if game over
    # Life > 0, keep guessing
    # Life <= 0, goto Died

  # Finish the word
    #### disaply its meaning, ...
    # score += 1, life set to 6 again
    # if score == 1000, goto Game over
    # goto Start guessing, exclude all previous questions

  # Died 
    # goto Game over

# Game over (record score)
  # Display your score
  # Record the highest score for each player
  # Rank all players
  # Result will be save at ??