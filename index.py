import csv


class bookmenager:
    booklist = []
    player = []

    @staticmethod
    def add_book(dat):
        with open('book.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(dat) 



bookm = bookmenager()

def get_book():
    bookm.booklist = []
    with open('book.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            bookm.booklist.append(row)
    return bookm.booklist

def selected(afd):
    if afd == 1:
        for row in bookm.booklist:
            print("{:<5} {:<10}".format(row[0], row[1]))
        
        print("Выберите книгу")
        idbook = input()
        print("Вы арендавали книгу необходимо ее вернуть через 14 дней")
        main()
    if afd == 2:
        print("Введите имя:")
        name = input()
        if checkuser(name) == True:
            print("Чтобы добавить книгу введите название")
            namebook = input()
            print("Введите цену аренды книги")
            pricebook = int(input())
            bookm.add_book([f"{namebook}", f"{pricebook}"])
        if checkuser(name) == False:
            print("Ты не пройдешь в систему!")
            main()
    if afd == 3:
        return

def get_user():
    bookm.player = []
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            bookm.player.append(row)
    return bookm.player

def checkuser(name):
    for row in bookm.player:
        if name in row:
            return True
    return False


def main():
    get_user()
    get_book()
    print("1. Арендавать книгу \n2. Авторизация \n Выйти")
    ab = int(input())
    selected(ab)


main()