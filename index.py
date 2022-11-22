import random
import time
from tkinter import *

win = Tk()
win.title("Trillionaire Tycoon")
win.geometry("550x550")
win.resizable(True, True)
money = 300
products = 20
score = 0 
cost = 7
number1 = 100
number2 = 120







def destroy():
  CostL3.destroy()
  Quest3.destroy()
  Enter3.destroy()
  invest4.destroy()
  Quest4.destroy()
  invest5.destroy()
  invest6.destroy()
  Quest5.destroy()
  Quest6.destroy()
  Back3.destroy()
  Chs.destroy()
  next()






def element98():
  global money

  agent = random.randint(1,10)
  if agent < 1:
    money += 2000
    pound.config(text = "Company Balance: £"+str(money))
    time.sleep(0.3)

    invest6.config(state = DISABLED)
  else:
    invest6.config(state= DISABLED)
  if money <= 200:
    win.destroy()
    win4 = Tk()
    win4.title("Trillionaire tycoon")
    win4.geometry("550x550")
    ag = Label(win4, text = "Unfortunately, you fell bellow the amount needed to sustain your business...\n Are you willing to try again??")
    ag.place(relx = 0.02, rely = 0.1)
    win4.mainloop()




  






def element48():
  global money
  global currently3
  agent = random.randint(1,10)
  if agent < 4:
    money += 2000
    pound.config(text = "Company Balance: £"+str(money))
    time.sleep(0.3)
    invest5.config(state = DISABLED)
  else:
    money -= 1000
    pound.config(text = "Company Balance: £"+str(money))
    invest5.config(state= DISABLED)
  if money <= 200:
    win.destroy()
    win4 = Tk()
    win4.title("Trillionaire tycoon")
    win4.geometry("550x550")
    ag = Label(win4, text = "Unfortunately, you fell bellow the amount needed to sustain your business...\n Are you willing to try again??")
    ag.place(relx = 0.02, rely = 0.1)
    win4.mainloop()

 



def element23():
  global money
  global currently2
  agent = random.randint(1,10)
  
  if agent < 5:
    money += 2000
    pound.config(text = "Company Balance: £"+str(money))
    time.sleep(0.3)
    invest4.config(state = DISABLED)
  else:
    money -= 1000
    pound.config(text = "Company Balance: £"+str(money))
    invest4.config(state= DISABLED)
  if money <= 200:
    win.destroy()
    win4 = Tk()
    win4.title("Trillionaire tycoon")
    win4.geometry("550x550")
    ag = Label(win4, text = "Unfortunately, you fell bellow the amount needed to sustain your business...\n Are you willing to try again??")
    ag.place(relx = 0.02, rely = 0.1)
    win4.mainloop()


  
 





def element():
  global money
  global currently
  agent = random.randint(1,10)
  if agent < 6:
    money += 2000
    pound.config(text = "Company Balance: £"+str(money))
    time.sleep(0.3)
 
    Enter3.config(state = DISABLED)
  else:
    Enter3.config(state= DISABLED)

  if money <= 200:
    win.destroy()
    win4 = Tk()
    win4.title("Trillionaire tycoon")
    win4.geometry("550x550")
    ag = Label(win4, text = "Unfortunately, you fell bellow the amount needed to sustain your business...\n Are you willing to try again??")
    ag.place(relx = 0.02, rely = 0.1)
    win4.mainloop()
  

  





def invest():
  A.destroy()
  time.sleep(0.3)
  B.destroy()
  time.sleep(0.03)
  C.destroy()
  time.sleep(0.03)
  D.destroy()
  global CostL3
  global Quest3

  CostL3 = Label(win, text = "% => [Chance of return on investment] | [Investment: £1000 -> £2000 to -£1000")
  CostL3.place(relx = 0.04, rely = 0.21)

  Quest3 = Label(win, text = "1. Bitcoin Stocks:(65%) + Insurance")
  Quest3.place(relx = 0.04, rely = 0.285)



  global Enter3
  Enter3 = Button(win, text = "Invest", fg = "brown", command = element)
  Enter3.place(relx = 0.5, rely = 0.28, relheight = 0.05, relwidth = 0.17)
  global Quest4

  Quest4 = Label(win, text = "2. Gold Stocks:(90%), no Insurance")
  Quest4.place(relx = 0.04, rely = 0.355)



  global invest4
  invest4 = Button(win, text = "Invest", fg = "brown", command = element23)
  invest4.place(relx = 0.5, rely = 0.35, relheight = 0.05, relwidth = 0.17)


  global Quest5
  Quest5 = Label(win, text = "3. Apple Stocks:(80%), no Insurance")
  Quest5.place(relx = 0.04, rely = 0.425)



  global invest5
  invest5 = Button(win, text = "Invest", fg = "brown",command  = element48)
  invest5.place(relx = 0.5, rely = 0.42, relheight = 0.05, relwidth = 0.17)


  global Quest6
  Quest6 = Label(win, text = "4. Tesla Stocks:(70%) + Insurance")
  Quest6.place(relx = 0.04, rely = 0.495)



  global invest6
  invest6 = Button(win, text = "Invest", fg = "brown", command = element98)
  invest6.place(relx = 0.5, rely = 0.49, relheight = 0.05, relwidth = 0.17)








  
  global Back3
  global Chs


  Back3 = Button(win, text = "⇦", font = "Bold",fg = "brown", command = destroy)
  Back3.place(relx = 0.05, rely = 0.13, relheight = 0.05, relwidth = 0.1)

  Chs.config(text = "[press to go back]", fg = "brown")
  Chs.place(relx = 0.17)












def al():
  CostL2.destroy()
  Enter2.destroy()
  Back2.destroy()
  Chs.destroy()
  Quest2.destroy()
  tell.destroy()
  next()
  





def spontan():
  global number1
  global number2
  global money
  number1 += 10
  number2 += 10

  money -= 1000
  pound23 = Label(win, text = "Company Balance: £"+str(money), fg = "red")
  pound23.place(relx = 0.02,rely = 0.05)

  if money <= 200:
    win.destroy()
    win4 = Tk()
    win4.title("Trillionaire tycoon")
    win4.geometry("550x550")
    ag = Label(win4, text = "Unfortunately, you fell bellow the amount needed to sustain your business...\n Are you willing to try again??")
    ag.place(relx = 0.02, rely = 0.1)
    win4.mainloop()





def camp():
  A.destroy()
  time.sleep(0.3)
  B.destroy()
  time.sleep(0.03)
  C.destroy()
  time.sleep(0.03)
  D.destroy()

  global CostL2
  global Quest2

  CostL2 = Label(win, text = "The cost of marketing/campaigning is £1000")
  CostL2.place(relx = 0.05, rely = 0.21)

  Quest2 = Label(win, text = "Click Yes to proceed with payment: ")
  Quest2.place(relx = 0.05, rely = 0.425)

  global tell
  tell = Label(win, text = "Clicking Yes => increase in market value e.g.  [100-110] => [110-120]")
  tell.place(relx = 0.05, rely = 0.32)

 

  global Enter2
  Enter2 = Button(win, text = "Yes / ✓", fg = "green", command = spontan)
  Enter2.place(relx = 0.5, rely = 0.415, relheight = 0.05, relwidth = 0.17)
  global Back2
  global Chs


  Back2 = Button(win, text = "⇦", font = "Bold",fg = "green", command = al)
  Back2.place(relx = 0.05, rely = 0.13, relheight = 0.05, relwidth = 0.1)

  Chs.config(text = "[press to go back]", fg = "green")
  Chs.place(relx = 0.17)














def redot():
  CostL1.destroy()
  Enterz.destroy()
  e1.destroy()
  Backz.destroy()
  Chs.destroy()
  Quest1.destroy()
  next()



def acumulator():
  global money
  global products
  now = int(e1.get())
  cashier = now * score
  money = money + cashier
  pound.config(text = "Company Balance: £"+str(money))


  products = products - now
  Products.config(text = "Products: "+str(products))
  if products <= 10:
    win.destroy()
    win3 = Tk()
    win3.title("Become a Trillionaire")
    win3.geometry("550x550")
    ag3 = Label(win3, text = "Unfortunately, you fell bellow the assets needed to sustain your business...\n Are you willing to try again??")
    ag3.place(relx = 0.02, rely = 0.1)
    win3.mainloop()







def sell():
  A.destroy()
  time.sleep(0.3)
  B.destroy()
  time.sleep(0.03)
  C.destroy()
  time.sleep(0.03)
  D.destroy()

  global CostL1
  global Quest1

  CostL1 = Label(win, text = "The current market value is [approx]: £" + str(score))
  CostL1.place(relx = 0.05, rely = 0.21)

  Quest1 = Label(win, text = "How much do you want to sell: ")
  Quest1.place(relx = 0.05, rely = 0.3)

  global e1
  e1 = Entry(win)
  e1.place(relx = 0.05, rely = 0.37, relheight = 0.05, relwidth = 0.18)

  global Enterz
  Enterz = Button(win, text = "Enter", fg = "blue", command = acumulator)
  Enterz.place(relx = 0.24, rely = 0.37, relheight = 0.05, relwidth = 0.19)
  global Backz
  global Chs


  Backz = Button(win, text = "⇦", font = "Bold",fg = "blue", command = redot)
  Backz.place(relx = 0.05, rely = 0.13, relheight = 0.05, relwidth = 0.1)

  Chs.config(text = "[press to go back]", fg = "blue")
  Chs.place(relx = 0.17)













  
def acalculate():
  global money
  global products
  now = int(e.get())
  cashier = now * 7
  money = money - cashier
  pound.config(text = "Company Balance: £"+str(money))

  products = products + now
  Products.config(text = "Products[min=10]: "+str(products))

  if money <= 200:
    win.destroy()
    win2 = Tk()
    win2.title("Become a Trillionaire")
    win2.geometry("550x550")
    ag = Label(win2, text = "Unfortunately, you fell bellow the amount needed to sustain your business...\n Are you willing to try again??")
    ag.place(relx = 0.02, rely = 0.1)
    win2.mainloop()
    
 








def redo():
  CostL.destroy()
  Enter.destroy()
  e.destroy()
  Back.destroy()
  Chs.destroy()
  Quest.destroy()
  next()




def make():
  A.destroy()
  time.sleep(0.3)
  B.destroy()
  time.sleep(0.03)
  C.destroy()
  time.sleep(0.03)
  D.destroy()
  global CostL
  global Quest

  CostL = Label(win, text = "The cost of production is £" + str(cost))
  CostL.place(relx = 0.05, rely = 0.21)

  Quest = Label(win, text = "How much do you want to make: ")
  Quest.place(relx = 0.05, rely = 0.3)

  global e
  e = Entry(win)
  e.place(relx = 0.05, rely = 0.37, relheight = 0.05, relwidth = 0.18)

  global Enter
  Enter = Button(win, text = "Enter", fg = "purple", command = acalculate)
  Enter.place(relx = 0.24, rely = 0.37, relheight = 0.05, relwidth = 0.19)
  global Back
  global Chs


  Back = Button(win, text = "⇦", font = "Bold", command = redo, fg = "purple")
  Back.place(relx = 0.05, rely = 0.13, relheight = 0.05, relwidth = 0.1)

  Chs.config(text = "[press to go back]", fg = "purple")
  Chs.place(relx = 0.17)









def next():
  global A
  global B
  global C
  global D
  global Chs
  global pound
  global Products
  start.destroy()
  time.sleep(0.45)
  pound = Label(win, text = "Company Balance: £"+str(money), fg = "red")
  pound.place(relx = 0.02,rely = 0.05)
  Products = Label(win, text = "Products: "+str(products), fg = "blue")
  Products.place(relx = 0.425,rely = 0.05)

  Line = Label(win, text = "---------------------------------------------------------------------------------------------------------")
  Line.place(relx = 0.012, rely = 0.09)

  wrong = Label(win, text = "[Min = £200]", fg = "red")
  wrong.place(relx = 0.02, rely = 0.017)

  pd = Label(win, text = "[Min = 10]", fg = "blue")
  pd.place(relx = 0.425, rely = 0.017)

  Chs = Label(win, text = "Options/Choices:")
  Chs.place(relx = 0.014, rely = 0.14)


  A = Button(win, text = "1: Make more products", fg = "Purple", command = make)
  A.place(relx = 0.012, rely = 0.2, relwidth = 0.45, relheight = 0.07)

  B = Button(win, text = "2: Sell your products", fg = "blue", command = sell)
  B.place(relx = 0.51, rely = 0.2, relwidth = 0.45, relheight = 0.07)

  C = Button(win, text = "3: Promote your product", fg = "green", command = camp)
  C.place(relx = 0.012, rely = 0.35, relwidth = 0.45, relheight = 0.07)
  
  D = Button(win, text = "4: Invest in other products", fg = "brown", command = invest)
  D.place(relx = 0.51, rely = 0.35, relwidth = 0.45, relheight = 0.07)







  def nextt():
      lab = Label(win, text = "Market Value: £"+str(score), fg = "red")

      lab.place(relx = 0.7, rely = 0.05)


  def clock():    
      global score
      global num
      global number1
      global number2
      num = random.randint(number1,number2)
      score = num
      win.after(1100, clock)
      nextt()    
      win.update()
  clock()



 # answer = Entry(win)
 # answer.place(relx = 0.014, rely = 0.50)
  

global start
start = Button(win, text = "Start", command = next)
start.place(relx = 0.40, rely = 0.21, relwidth = 0.12, relheight = 0.1)


submit = Button(win, text="Enter")
submit.place()

nexton = Button(win, text = "next")
nexton.place()

win.mainloop()