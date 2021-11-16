from json import load

def load_and_parse_data(file_name):
    data = load(open(file_name))
    
    people_dict = {}
    people_list = []
    
    for faculty in data:
        for department in data[faculty]:
            for url in data[faculty][department]['staff']:
                fio      = data[faculty][department]['staff'][url]['name']
                courses  = data[faculty][department]['staff'][url]['courses']
                age      = data[faculty][department]['staff'][url]['age']
                sex      = data[faculty][department]['staff'][url]['sex']
                position = data[faculty][department]['staff'][url]['position']
                science  = data[faculty][department]['staff'][url]['science']
    
                people_dict.update({fio:{
                        'courses' : courses,
                        'age'     : age,
                        'sex'     : sex,
                        'position': position,
                        'science' : science,
                    }
                })
        
                people_list += [(
                    fio,
                    courses,
                    age,
                    sex,
                    position,
                    science,
                )]
    return people_dict, people_list

def find_teacher_in_dict(a_dict):
    sorted_dict = {
        k: v for k, v in sorted(a_dict.items(), key=lambda x:x[1]['courses'].count(','))
    }
    last = list(sorted_dict.keys())[-1]
    return last, a_dict[last]

def find_teacher_in_list(a_list):
    rez = sorted(a_list, key=lambda x:x[1].count(','))[-1]
    return rez

if __name__ == '__main__':
    people_dict, people_list = load_and_parse_data('out.json')
    
    the_most_erudite_teacher = find_teacher_in_dict(people_dict)
    print(the_most_erudite_teacher)
    the_most_erudite_teacher = find_teacher_in_list(people_list)
    print(the_most_erudite_teacher)