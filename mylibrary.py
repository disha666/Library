def my_library(): 
    print('                                       WELCOME TO MY SKILL CIRCLE LIBRARY MANAGEMENT SYSTEM      ')
    print('======TITLE OF BOOKS======')
    print('\n',"1.Mahabharta",'\n', "2.Henna Artist" '\n', "3.When Dimple Met Rishi" '\n', "4.The God of Small Things" '\n', "5.The Oath of the Vayuputras")

    number = int(input('Enter a number'))
    if (number==1):
        print('\n',"1.[BOOK NAME : Mahabharta","\n","2.[Published] : Published in the year 1951.","\n","3 [Author] :Vasya ","\n",
          '''4.[Discription] : The huge popularity of the book has resulted in the book being re-printed several times. Centuries ago, 
          it was proclaimed of the Mahabharata: "What is not in it, is nowhere." But even now, we can use the same words about it. 
          He who knows it not, knows not the heights and depths of the soul; he misses the trials and tragedy and the beauty and grandeur of life.
          The Mahabharata is not a mere epic; it is a romance telling the tale of heroic men and women, and of some who were divine.
          It is a whole literature in itself, containing a code of life, a philosophy of social and ethical relations, and speculative thought on human
          problems that is hard to rival.''')
    elif(number==2):
        print('\n',"1.[BOOK NAME] :The Henna Artist","\n","2.[Published] : Published in the year 2020.","\n","3 [Author] :Alka Joshi ","\n",
          '''4.[Discription] :Vivid and compelling in its portrait of one woman’s struggle for fulfillment in a society pivoting between 
          the traditional and the modern, The Henna Artist opens a door into a world that is at once lush and fascinating, stark and cruel.''')
    elif(number==3):
        print('\n',"1.[BOOK NAME:When Dimple Met Rishi","\n","2.[Published] : Published in the year 2017.","\n","3 [Author] :Sandhya Menon ","\n",
          '''4.[Discription] : Dimple Shah has it all figured out. With graduation behind her, she’s more than ready for a break from her family—and from Mamma’s inexplicable obsession with her finding the “Ideal Indian Husband.” Ugh. Dimple knows they must respect her principles on some level, though. If they truly believed she needed a husband right now, they wouldn’t have paid for her to attend a summer program for aspiring web developers…right?

Rishi Patel is a hopeless romantic. So when his parents tell him that his future wife will be attending the same summer program—wherein he’ll have to woo her—he’s totally on board. Because as silly as it sounds to most people in his life, Rishi wants to be arranged, believes in the power of tradition, stability, and being a part of something much bigger than himself.

The Shahs and Patels didn’t mean to start turning the wheels on this “suggested arrangement” so early in their children’s lives, but when they noticed them both gravitating toward the same summer program, they figured, Why not?

Dimple and Rishi may think they have each other figured out. But when opposites clash, love works hard to prove itself in the most unexpected ways..''')
    elif(number==4):
        print('\n',"1.[BOOK NAME: The God of Small Things","\n","2.[Published] : Published in the year 1969.","\n","3 [Author] :Arundhati Roy ","\n",
          '''4.[Discription] :The year is 1969. In the state of Kerala, on the southernmost tip of India, a skyblue Plymouth with chrome tailfins is stranded on the highway amid a Marxist workers' demonstration. Inside the car sit two-egg twins Rahel and Esthappen''')
    elif(number==5):
        print('\n',"1.[BOOK NAME: The Oath of the Vayuputras","\n","2.[Published] : Published in the year 2013.","\n","3 [Author] :Amish Tripathi ","\n",
          '''4.[Discription] : Shiva is gathering his forces. He reaches the Naga capital, Panchavati, and Evil is finally revealed. The Neelkanth prepares for a holy war against his true enemy, a man whose name instils dread in the fiercest of warriors.

India convulses under the onslaught of a series of brutal battles. It's a war for the very soul of the nation. Many will die. But Shiva must not fail, no matter what the cost. In his desperation, he reaches out to the ones who have never offered any help to him: the Vayuputras.

Will he succeed? And what will be the real cost of battling Evil? To India? And to Shiva's soul?

Discover the answer to these mysteries in this concluding part of the bestselling Shiva Trilogy.''')
    else:
        print("Please select the given serial numbers only.")

    
    n1= str(input("\n""Do you want to continue? (yes/no):"))
    if (n1=='yes'):
            my_library()
    elif (n1=='YES'):
            my_library()
    elif (n1=="no"):
        print('\n',"======================================THANK YOU FOR VISITING======================================")
    elif (n1=="NO"):
        print("======================================THANK YOU FOR VISITING======================================")

    else:
        print('\n',"PLEASE PRESS YES OR NO")
        
my_library()
    