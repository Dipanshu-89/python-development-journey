class Fraction:
    def __init__(self,num,den):
        self.numerator=num
        self.denominator=den
    def __str__(self):
        return "{} / {}".format(self.numerator,self.denominator)
    def __add__(self,other):
        new_num=self.numerator*other.denominator+other.numerator*self.denominator
        new_den=self.denominator*other.denominator
        return '{}/{}'.format(new_num,new_den)
    def __sub__(self,other):
        new_num=self.numerator*other.denominator-other.numerator*self.denominator
        new_den=self.denominator*other.denominator
        return '{}/{}'.format(new_num,new_den)
    def __mul__(value1,value2):
        new_num=value1.numerator*value2.numerator
        new_denominator=value1.denominator*value2.denominator
        return "{}/{}".format(new_num,new_denominator)
    def __truediv__(value1,value2):
        new_numerator=value1.numerator*value2.denominator
        new_den=value1.denominator*value2.numerator
        return "{}/{}".format(new_numerator,new_den)

fr1=Fraction(7,4)
fr2=Fraction(1,4)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)
