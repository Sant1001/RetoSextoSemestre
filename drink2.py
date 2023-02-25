def funaux(word):
    aux=""
    for i in range(len(word)):
        if word[i]  == ' ':
            continue
        else:
            aux=aux+str(word[i])
    return aux

def isasce(word):
    for i in range(len(word)-1):
        if word[i]>word[i+1]:
            return False
    return True

def AddNewDrink(word):
    arrword=[]
    contaux=0
    cont=0
    tpe=""
    aux=""
    for i in range(len(word)):
        if(word[i]=='.' or word[i]==' ' or (word[i]==',' or word[i].isalnum())):
            if(word[i]==' '):
                continue
            elif(word[i]!=',' and cont==0):
                tpe = tpe+str(word[i])
            elif(word[i]==',' and cont==0):
                arrword.append(tpe)
                cont+=1
            elif(word[i]!=',' and cont>0):
                aux=aux+str(word[i])
                cont+=1
            elif(word[i]==',' and cont>0):
                cont+=1
                arrword.append(aux)
                aux=""
                contaux = i
        else:
            return False

    arrword.append(funaux(word[contaux+1:]))
    return arrword

def main(drink):
    err=[]
    if(drink!=False):
        if((len(drink))<2):
            err.append("No size value entered: Invalid")
        elif((len(drink))>6):
            err.append("More than five size values entered: Invalid")
        for i in range(len(drink)):
            if(i == 0):
                for j in range(len(drink[0])):
                    if(drink[0][j].isnumeric() == True):
                        err.append("Item name is not alphabetic: Invalid")
                if(len(drink[0])<2):
                    err.append("Item name is less than 2 characters in lenght: Invalid")
                elif(len(drink[0])>15):
                    err.append("Item name is greater than 15 characters in length: Invalid")
            elif(i>0):
                if(len(drink[i]) > 1):
                    try:
                        int(drink[i])
                    except:
                        if('.' in drink[i]):
                            if("Size value is a decimal: Invalid" not in err):
                                err.append("Size value is a decimal: Invalid")
                        else:
                            if("Size value includes nonnumeric characters: Invalid" not in err):
                                err.append("Size value includes nonnumeric characters: Invalid")
                        
        try:
            isasce(drink[1:])
        except:
            err.append("Missing size values: Invalid")
            return err
        if(isasce(drink[1:])==False):
            err.append("Size values entered in nonascending order: Invalid")
    else:
        err.append("Invalid character entered: Invalid")
        return err
    return err
    

k = input()
if(main(AddNewDrink(k))==[]):
    print("Valid")
else:
    print(main(AddNewDrink(k)))    

