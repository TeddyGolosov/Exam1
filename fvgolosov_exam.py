import re
def reading():
    f = open('article.txt', 'r', encoding = 'utf-8')
    string = f.read()
    f.close()
    return string
def task1(x):
    regex = '[А-ЯЁ]\. ?(?:[А-ЯЁ][а-яё-]+)+'
    a = re.findall(regex, x)
    for word in a:
        print(word)
def task2(y):
    regex1 = '(?:(?:[А-ЯЁ]\.-? ?)+|(?:[А-ЯЁ][а-яё-]+)+ )(?:[А-ЯЁ][а-яё-]+)+'

    b = re.findall(regex1, y)
    for word1 in b:
        print(word1)
def main():
    n = task1(reading())
    m = task2(reading())
if __name__ == '__main__':
    main()


    
