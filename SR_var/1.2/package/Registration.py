class Registration:
    """Создаем конструктор, где его свойство participants - пустой список"""
    def __init__(self):
        self.participants = list()

    """Создаем метод "Добавление участника", где его входные значения - имя, фамилия, возраст и почта"""
    def AddingMember(self, name, surname, age, email):
        for member in self.participants:
          if(member["participant_email"]==email):
            print("Такой пользовател уже есть.")
            return False
        self.participants.append({"participant_name": name,
                                 "participant_surname": surname,
                                 "participant_age": age,
                                 "participant_email": email})
        return True                             
    
    """Создаем метод "Удаление участника", где удаление участника идет по почте, 
    так как email - это уникаьное значение"""
    def DeleteMember(self, email):
        for participant in self.participants:
            if participant.get("participant_email") == email:
                self.participants.remove(participant) 
    
    """Создаем метод - Запись в файл"""
    def RecordFile(self,filename):
        import json # чтобы преобразовать в json из dict в котором list        
        with open("./"+filename+".json", 'w') as file:
            json_data = { "all_participant": self.participants } # это делает так { [{},{}] }, делает  валидный json 
            # dumps = сделай мне из dict json
            # indent = количество пробелов в отступах
            file.write(json.dumps(json_data, indent=4))

    """Создаем метод "Чтение из файла"""
    def ReadFile(self, filename):
        import json
        self.participants=list()
        with open("./"+filename+".json") as json_file:          
          for obj in json.load(json_file)['all_participant']:
            self.participants.append(obj)

    """Создаем метод "Изменить участника", где изменение участника идет по почте, 
    так как email - это уникаьное значение"""
    def UpdateMember(self, email,propertyMember,valueMember):
        propeties=("participant_name","participant_surname","participant_age","participant_email")
        get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y] #функция для поиска в списке
        if (len(get_indexes(propertyMember,propeties))==0):
          print("Такого свойства нет.")
          return False       
        for member in self.participants:
          if(member["participant_email"]==email):
            member[propertyMember]=valueMember              
            return True

    """Создаем метод - Вывести список пользователей из книги"""
    def GetMembers(self):
      return self.participants

    """Создаем метод - Вывести список пользователей из книги"""
    def GetMember(self,email):
      for member in self.participants:
          if(member["participant_email"]==email):            
            print(member)    
            return True
      return False
