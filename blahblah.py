def leap():
    year = int(input('알고싶은 년도를 입력해주세요'))
    print('윤년' if year % 4 == 0 and year % 100 != 0
                  or year % 400 == 0 else '평년')


if __name__ == '__main__':
    leap()
