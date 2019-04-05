def weight_on_planets():
   # write your code here
   weight = float(input("What do you weigh on earth? "))
   mars_weight = weight*.38
   jupiter_weight = weight*2.34
   print("\n" + "On Mars you would weigh" , mars_weight , "pounds.\n" + "On Jupiter you would weigh" , jupiter_weight , "pounds.")
if __name__ == '__main__':
   weight_on_planets()