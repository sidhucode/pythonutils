def tictactoe_py():
  import os

  def clear():
    os.system('clear')

  def choose_py(var_name,list_options,question_text):
    questions = [
      inquirer.List(var_name,
                    message=question_text,
                    choices=list_options,
                ),
    ]
    global answers
    answers = inquirer.prompt(questions)
    return answers[var_name] 

  import inquirer

  def main():
    global x1
    global o1
    a1 = '#'
    b1 = '#'
    c1 = '#'
    a2 = '#'
    b2 = '#'
    c2 = '#'
    a3 = '#'
    b3 = '#'
    c3 = '#'
    x1 = ''
    o1 = ''
    while True:
      print('''
    _______________________
    | [Guide]   | [#Grid] |  
    _______________________
    | a1,a2,a3  | ''',a1,a2,a3,''' |
    | b1,b2,b3  | ''',b1,b2,b3,''' |
    | c1,c2,c3  | ''',c1,c2,c3,''' |
    _______________________
    '''
    )
      print()
      choose_py('x',['a1','b1','c1','a2','b2','c2','a3','b3','c3',],'Choose the following - Player 1 - X')
      print('Player 1 chose',answers['x'],'\n')
      x1 = answers['x']
      if x1=='a1' and a1 != 'o':
        a1 = 'x'
      elif x1=='b1' and b1 != 'o':
        b1 = 'x'
      elif x1=='c1' and c1 != 'o':
        c1 = 'x'
      elif x1 == 'a2' and a2 != 'o':
        a2 = 'x'
      elif x1 == 'b2' and b2 != 'o':
        b2 = 'x'
      elif x1 == 'c2' and c2 != 'o':
        c2 = 'x'
      elif x1 == 'a3' and a3 != 'o':
        a3 = 'x'
      elif x1 == 'b3' and b3 != 'o':
        b3 = 'x'
      elif x1 == 'c3' and c3 != 'o':
        c3 = 'x'
      print(a1,a2,a3)
      print(b1,b2,b3)
      print(c1,c2,c3)
      print()
      if (a1 == 'x' and a2 == 'x' and a3 == 'x') or (b1 == 'x' and b2 == 'x' and b3 == 'x') or (c1 == 'x' and c2 == 'x' and c3 == 'x') or (a1 == 'x' and b2 == 'x' and c3 == 'x') or (c1 == 'x' and b2 == 'x' and a3 == 'x'):
        print('Player 1 Wins!')
        exit() 
      elif (a1 == 'o' and a2 == 'o' and a3 == 'o') or (b1 == 'o' and b2 == 'o' and b3 == 'o') or (c1 == 'o' and c2 == 'o' and c3 == 'o') or (a1 == 'o' and b2 == 'o' and c3 == 'o') or (c1 == 'o' and b2 == 'o' and a3 == 'o'):
        print('Player 2 Wins!') 
        exit()
      elif (a1!='#' and b1!='#' and c1!='#' and a2!='#' and b2!='#' and c2!='#' and a3!='#' and b3!='#' and c3!='#'):
        print('Player 1 - X and Player 2 - O are tied!')
        exit()
      else:
        pass
      input('Press ENTER to continue')
      clear()

      print('''
    _______________________
    | [Guide]   | [#Grid] |  
    _______________________
    | a1,a2,a3  | ''',a1,a2,a3,''' |
    | b1,b2,b3  | ''',b1,b2,b3,''' |
    | c1,c2,c3  | ''',c1,c2,c3,''' |
    _______________________
    '''
    )
      print()
      choose_py('o',['a1','b1','c1','a2','b2','c2','a3','b3','c3',],'Choose the following - Player 2 - O')
      print('Player 2 chose',answers['o'],'\n')
      o1 = answers['o']
      if o1 == 'a1' and a1 != 'x':
        a1 = 'o'
      elif o1 == 'b1' and b1 != 'x':
        b1 = 'o'
      elif o1 == 'c1' and c1 != 'x':
        c1 = 'o' 
      elif o1 == 'a2' and a2 != 'x':
        a2 = 'o' 
      elif o1 == 'b2' and b2 != 'x':
        b2 = 'o'
      elif o1 == 'c2' and c2 != 'x':
        c2 = 'o'
      elif o1 == 'a3' and a3 != 'x':
        a3 = 'o'
      elif o1 == 'b3' and b3 != 'x':
        b3 = 'o'
      elif o1 == 'c3' and c3 != 'x':
        c3 = 'o'
      print(a1,a2,a3)
      print(b1,b2,b3)
      print(c1,c2,c3)
      print()
      if (a1 == 'x' and a2 == 'x' and a3 == 'x') or (b1 == 'x' and b2 == 'x' and b3 == 'x') or (c1 == 'x' and c2 == 'x' and c3 == 'x') or (a1 == 'x' and b2 == 'x' and c3 == 'x') or (c1 == 'x' and b2 == 'x' and a3 == 'x'):
        print('Player 1 Wins!')
        exit() 
      elif (a1 == 'o' and a2 == 'o' and a3 == 'o') or (b1 == 'o' and b2 == 'o' and b3 == 'o') or (c1 == 'o' and c2 == 'o' and c3 == 'o') or (a1 == 'o' and b2 == 'o' and c3 == 'o') or (c1 == 'o' and b2 == 'o' and a3 == 'o'):
        print('Player 2 Wins!') 
        exit()
      elif (a1!='#' and b1!='#' and c1!='#' and a2!='#' and b2!='#' and c2!='#' and a3!='#' and b3!='#' and c3!='#'):
        print('Player 1 - X and Player 2 - O are tied!')
        exit()
      else:
        pass
      input('Press ENTER to continue')
      clear()

  main()
tictactoe_py()