def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=10):

        if choice==1:
            print_result(read_txt('phonebook.txt'))
            read_txt('phonebook.txt')
        elif choice==2:
            last_name=input('Введите фамилию: ')
            print_result(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('Введите номер телефона: ')
            print_result(find_by_number(phone_book,number))
	    	
        elif choice==4:
            last_name=input('Фамилия: ')
            first_name=input('Имя: ')
            new_number=input('Новый номер: ')
            change_number(phone_book,last_name,first_name,new_number)
            
        elif choice==5:
            last_name=input('Фамилия: ')
            first_name=input('Имя: ')
            delete_user(phone_book,last_name, first_name)
        elif choice==6:
            last_name=input('Фамилия: ')
            first_name=input('Имя: ')
            number=input('номер: ')
            data=input('описание: ')
            add_user(phone_book,last_name,first_name, number,data)
            
        elif choice==7:
            last_name=input('Фамилия: ')
            first_name=input('Имя: ')
            new_data=input('новое описание: ')
            mod_data(phone_book,last_name,first_name,new_data)
        elif choice==8:
            write_csv(phone_book) 
        elif choice==9:
            print_result(read_csv('phonebook_exp.csv')) 

        choice=show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер абонента\n"
          "5. Удалить абонента\n"
          "6. Добавить абонента\n"
          "7. Изменить описание абонента\n"
          "8. Сохранить справочник в формате CSV\n"
          "9. Открыть справочник в формате CSV\n"
          "10. Завершить работу со справочником\n")
         
    choice = int(input())
    return choice



'''Иванов,       Иван ,   111,  описание Иванова

Петров,      Петр ,    222,  описание Петрова

Васичкина , Василиса , 333 , описание Васичкиной

Питонов,    Антон,     777,    умеет в Питон'''

def print_result(data):
    
    #print(data)
   
    print('\n')
    print('Фамилия', 'Имя', 'Телефон', 'Описание')
    print('_____________________________________')
    for i in data:
        
        for j in i.values():
           print (j, end=' ')
        print()
    print('\n')
    

    
    
    
          
        
        

def find_by_lastname(phone_book,last_name):
    found=[]
    found1=0
    for i in range(len(phone_book)):
        if last_name in phone_book[i].values():
            found.append(phone_book[i])
            found1+=1
    if found1==0: print("абонент не найден!")
    return found


def change_number(phone_book_,last_name,first_name,new_number):
    
    changes=0
    changed_book=[]
    
    for i in range(len(phone_book_)):
       
        if (last_name in phone_book_[i].values()) & (first_name in phone_book_[i].values()):
            phone_book_[i]["Телефон"]=new_number
            changes+=1
            
        changed_book.append(phone_book_[i])
     
    if changes==0:
        print("абонент не найден, проверьте данные!")
        return
    else:
        write_txt('phonebook.txt',changed_book)
        print("Номер успешно изменен, данные сохранены!")
    


def delete_user(phone_book,lastname, firstname):
    changes=0
    changed_book=phone_book
    
    for i in range(len(changed_book)):
       
        if (lastname in changed_book[i].values()) & (firstname in changed_book[i].values()):
            changed_book.pop(i)
            changes+=1
            

    if changes==0:
        print("абонент не найден, проверьте данные!")
        return
    else:
        write_txt('phonebook.txt',changed_book)
        print("Пользователь успешно удален, данные сохранены!")


def find_by_number(phone_book,number):
    found=[]
    found1=0
    for i in range(len(phone_book)):
        if number in phone_book[i].values():
            found.append(phone_book[i])
            found1+=1
    if found1==0: print("абонент с таким номером не найден!")
    return found


def add_user(phone_book,last,first,num,desc):
    new_book=phone_book
    
    new_record=dict()
    new_record["Фамилия"]=last
    new_record["Имя"]=first
    new_record["Телефон"]=num
    new_record["Описание"]=desc

    new_book.append(new_record)

    write_txt('phonebook.txt',new_book)
    print("Пользователь успешно добавлен, данные сохранены!")


def mod_data(phone_book,last,first,new_desc):
    changes=0
    changed_book=[]
    
    for i in range(len(phone_book)):
       
        if (last in phone_book[i].values()) & (first in phone_book[i].values()):
            phone_book[i]["Описание"]=new_desc
            changes+=1
            
        changed_book.append(phone_book[i])
     
    if changes==0:
        print("абонент не найден, проверьте данные!")
        return
    else:
        write_txt('phonebook.txt',changed_book)
        print("Описание успешно изменено, данные сохранены!")




def read_txt(filename): 
 phone_book=[]
 fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
 
 with open(filename,'r',encoding='utf-8') as phb:
    for line in phb:
        record=dict()
        if len(line)!=1:
          record = dict(zip(fields, line.replace(' ','').replace('\t','').replace('\n','').split(',')))
          phone_book.append(record)
		   #dict(( (фамилия,Иванов),(имя, Точка),(номер,8928), (Описание, питонист) ))
          #print(record)
        #phone_book.append(record)
 return phone_book




def write_txt(filename , phone_book):
    with open('phonebook.txt','w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')



def write_csv(phone_book):
    import csv
    filednames=["Фамилия", "Имя", "Телефон", "Описание"]

    with open('phonebook_exp.csv','w', encoding='utf-8') as phcsv:
        writer=csv.DictWriter(phcsv, lineterminator="\r", fieldnames=filednames)
        writer.writeheader()
        for i in phone_book:
          writer.writerow(i)
       
    print('данные успешно сохранены в файл "phonebook_exp.csv"')


def read_csv(filename):
    phone_book=[]
    import csv
    #filednames=["Фамилия", "Имя", "Телефон", "Описание"]

    with open(filename,'r', encoding='utf-8') as r_phcsv:
        
        reader=csv.DictReader(r_phcsv)
        for row in reader:
                        
          phone_book.append(row)
          
    print('данные успешно загружены из файла "phonebook_exp.csv"')
    return phone_book


work_with_phonebook()
