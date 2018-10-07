import re
import codecs

def remove_character_punctuation(lst):
    punctuation = ',.?!:;\"\'#$%^&*()-+=_`~'
    lst_removed = []
    for l in lst:
        character_tail = l[len(l)-1]
        character_head = l[0]
        if character_tail in punctuation:
            l = l.rstrip(character_tail)
        if character_head in punctuation:
            l = l.lstrip(character_head)
        lst_removed.append(l)
    return lst_removed

def check_string(st):
    cdau = u"àảãáạăằẳẵắặâầẩẫấậèẻẽéẹêềểễếệìỉĩíịòỏõóọôồ\
            ổỗốộơờởỡớợùủũúụưừửữứựỳỷỹýỵđÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬÈẺẼ\
            ÉẸÊỀỂỄẾỆÌỈĨÍỊÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢÙỦŨÚỤƯỪỬỮỨỰỲỶỸÝỴĐ"
    
    ret = True
    for char in st:
        if char not in cdau and \
            bool(re.match('^[a-zA-Z0-9]+$', char)) == False:
            ret = False
    return ret


def processing_raw_text(st):
    #raw_text = codecs.open(pathFile, encoding='utf-8', mode='r').read()
    #lst_raw_text = raw_text.split()  # list string utf-8 
    lst_raw_text = st.split()
    lst_process = remove_character_punctuation(lst_raw_text)
    index_remove = []
    for i in range(len(lst_process)):
        if check_string(lst_process[i]) == False:
            index_remove.append(i)
    lst = []
    for i in range(len(lst_raw_text)):
        if i not in index_remove:
            lst.append(lst_raw_text[i])

    return (' '.join(lst))



def main():

    st = codecs.open('2.txt', encoding='utf-8', mode='r').read()
    print(processing_raw_text(st))


if __name__ == '__main__':
    main()
