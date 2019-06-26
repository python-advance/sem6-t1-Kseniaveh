import Registration

if __name__ == "__main__":
    #Создаем 1 книгу
    GuestBook = Registration.Registration()
    #Добавляем в 1 книгу 3 юзеров
    GuestBook.AddingMember("Ksenia", "Vehov", 20, "ksen@gmail.com")
    GuestBook.AddingMember("IaIaIa", "Foool", 200, "iafoool@gmail.com")
    GuestBook.AddingMember("111", "Fooo2222l", 200, "i2afoool@gmail.com")
    GuestBook.AddingMember("111", "Fooo2222l", 200, "i2afoool@gmail.com")
    #Удаляем из 1 книги 1 юзера
    GuestBook.DeleteMember("i2afoool@gmail.com")
    #Сохраняем 1 книгу в файл
    GuestBook.RecordFile("test1")
    
    #Создаем 2 книгу
    GuestBook2 = Registration.Registration()
    #Читаем информацию из файла во 2 книгу
    GuestBook2.ReadFile("test1")
    #Удаляем из 2 книги 1 юзера
    GuestBook2.DeleteMember("ksen@gmail.com")
    #Добавляем в 2 книгу 1 юзера
    GuestBook2.AddingMember("Ksenia", "Vehov", 20, "ksen@gmail.com")
    #Изменяем свойство во 2 книге у юзера ksen@gmail.com
    GuestBook2.UpdateMember("ksen@gmail.com","participant_surname","Vehova")
    #Сохраняем 2 книгу в новый файл
    GuestBook2.RecordFile("test2")
    #Выводим список пользователей
    print(GuestBook2.GetMembers())
    #Выводим 1 пользователя
    print(GuestBook2.GetMember("ksen@gmail.com"))
