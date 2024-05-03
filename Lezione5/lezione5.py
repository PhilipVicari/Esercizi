def convert_temperature(gradi_c, gradi_f= False):
    Diff=32
    formulaF= (gradi_f-Diff)*5
    formulaF=formulaF/9
    formulaC=(gradi_c*9)/5
    formulaC=formulaC+Diff
    return formulaC
convert_temperature(32, False)
print(convert_temperature(32, False))
def is_magic_number(num: int) -> bool:
    list=[]
    for i in str(num):
        list.append(i)
    print(list)
    if '7' in list:
        return True
    else:
        return False
is_magic_number(12345)
print(is_magic_number(12370))