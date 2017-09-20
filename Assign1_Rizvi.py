__author__ = 'Syed Haider Abbas Rizvi'
__author__ = 'MS Student Software Engineering!'
__author__ = '39129'

import re; # importing module!
from datetime import datetime; # importing Datetime module

# ******************************* Question # 1's Solution **************************************************************

class Calculator (object):

    
    def __init__(self, array):

        self.array = array;


    def calculateAverage(self):

        outputDictionary = {}; # Dictionary Declaration

        #  Calcutlation of Average

        addedSum = sum(self.array);
        lengthOfList = len(self.array);
        answer = addedSum / lengthOfList;

        if(answer <= 6):
            outputDictionary = {'a' : 'The Sum of the List is: ' + str(answer) + ' Low Average!!!'};


        elif(answer > 6 and answer <= 12):
             outputDictionary ={'b' : 'The Sum of the List is: ' + str(answer) + ' Medium Average!!!'};

        elif (answer >= 16):
              outputDictionary = {'c' : 'The Sum of the List is: ' + str(answer) + ' High Average!!!'};

        # condition to dynamically print the value according to the existance of Key inside a Dictionary
        print('Answer # 1 : ');
        if('a' in outputDictionary):
          print(outputDictionary['a']);

        elif('b' in outputDictionary):
          print(outputDictionary['b']);

        else:
              print(outputDictionary['c']);



makePrinter = Calculator([33,4,0,1,3]);

makePrinter.calculateAverage();

#******************* End of Answer # 1 ******************************************************************************


# ************************* Question # 2 's Solution ****************************************************************

class Calculators (object):


    def __init__(self, arrays):
        self.array = arrays;

    @classmethod
    def redefineList(cls,list):
        patternList =  re.findall(r'\d+', list);
        patternList = map(int, patternList);
        return cls(patternList)



    def calculateAverages(self):

        outputDictionary = {}; # Dictionary Declaration

        #Calcutlation of Average

        addedSum = sum(self.array);
        lengthOfList = len(self.array);
        answer = addedSum / lengthOfList;

        if(answer <= 6):
            outputDictionary = {'a' : 'The Sum of the List is: ' + str(answer) + ' Low Average!!!'};


        elif(answer > 6 and answer <= 12):
             outputDictionary ={'b' : 'The Sum of the List is: ' + str(answer) + ' Medium Average!!!'};

        elif (answer >= 16):
              outputDictionary = {'c' : 'The Sum of the List is: ' + str(answer) + ' High Average!!!'};


        print('Answer # 2 : ');
        if('a' in outputDictionary):

          print(outputDictionary['a']);

        elif('b' in outputDictionary):
              print(outputDictionary['b']);

        else:
              print(outputDictionary['c']);


objString = "l33t h4x0r 1s pwn3d"; # input value which is a String!
makePrinters = Calculators.redefineList(objString);
makePrinters.calculateAverages();



#************************************* End of Answer # 2 ****************************************************************


# ********************* Question # 3 **************************************************************************************


def dateMaker(inputObj):
    dateFormat = '%Y-%m-%d'; # date format American Style.!
    madeDate = datetime.strptime(inputObj, dateFormat);
    currentDate = datetime.now();
    date2 = str(currentDate);
    days = currentDate - madeDate
    return days;

def findDaysArticle(obj):
    arrayList = [];
    array = (obj.split('/'));
    stringDate = array[1] + '-'+ array[2] + '-'+array[3]
    days = dateMaker(stringDate);

    for a in array:
        if(a == 'my_summer'):
            arrayList.append(a);
            array.remove(a);
            arrayList.append(stringDate); #inserting value inside a list
            arrayList.append(days.days); #inserting value inside a list
            arrayTuple = tuple(arrayList); # converting List into Tuple

    print('Answer # 3');
    print(arrayTuple);


findDaysArticle("articles/2010/10/21/my_summer")

#************************ End of Answer # 3 ***************************************************************************