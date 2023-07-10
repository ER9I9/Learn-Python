def spin_words(sentence):
    words=sentence.split()
    result=''
    for n in range(len(words)):
        if n==0 :     
            if len(words[n])<5:
                result= result+words[n]
            else :
                 result= result+words[n][::-1]
        else :
            if len(words[n])<5:
                result= result+' '+words[n]
            else :
                 result= result+' '+words[n][::-1]
    return result
