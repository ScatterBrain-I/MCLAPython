import NEMO

foods = ['Vanilla', 'Chocalate', 'Strawbery','Bacon']
ratings = []
for flavor in foods:
    rating = NEMO.userInt("Rate %s from 1 to 5:" % flavor)
    ratings.append ("%s rated as a %s" % (flavor, rating))
   
print 
print ratings    
    
    

    

    
    
    