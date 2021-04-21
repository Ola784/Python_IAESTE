def mirror(text):
    L=text.split(' ')
    list_len=len(L)
    a=[]
    max=0
    for i in range(list_len):#znajduje najdluzsze slowo z listy
         if len(L[i])>max :
            max=len(L[i])
    max+=4
    word = list('*' * max)
    word2=''.join(word)
    a.append(word2)
    max-=4
    for i in range(list_len):
        roznica=max-len(L[i])
        reversedstr=''.join(reversed(L[i]))
        a.append('* '+reversedstr+' '*roznica+' *')
    a.append(word2)
    for i in range(len(a)):
        a[i]=a[i].rjust(5)
    #nie mam pojecia czemu nie przechodza mi testy, w konsoli wyglada ok
    return a

#dl najdluzszego + 4
print('noice')
#mirror('ETSEAI ROF EHT NIW')
"""
Your task is to write a mirror function, that will reverse given string and print it like in the example:

ETSEAI ROF EHT NIW

**********
* IAESTE *
* FOR    *
* THE    *
* WIN    *
**********

Align text to the right.
"""

assert mirror('ETSEAI ROF EHT NIW') == '''**********
* IAESTE *
* FOR    *
* THE    *
* WIN    *
**********'''
assert mirror('eW deen uoy') == '''********
* We   *
* need *
* you  *
********'''
assert mirror('Mary plays the piano') == '''*********
* yraM  *
* syalp *
* eht   *
* onaip *
*********'''
assert mirror('yraM syalp eht onaip') == '''*********
* Mary  *
* plays *
* the   *
* piano *
*********'''
assert mirror('ehT weiv morf eht esuohthgil deticxe neve eht tsom denosaes relevart') == '''**************
* The        *
* view       *
* from       *
* the        *
* lighthouse *
* excited    *
* even       *
* the        *
* most       *
* seasoned   *
* traveler   *
**************'''
