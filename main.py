import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def main(contacts_list):
    pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
    new_contacts_list = []
    for contact in contacts_list:
        full_name = " ".join(contact[:3]).split(" ")
        full_info = [full_name[0], full_name[1], full_name[2], contact[3], contact[4],
                     re.sub(pattern, r"+7(\2)-\3-\4-\5 \6\7", contact[5]), contact[6]]
        new_contacts_list.append(full_info)
    return new_contacts_list


def sort(new_contacts_list):
    for i in new_contacts_list:
        first_name = i[0]
        last_name = i[1]
        for b in new_contacts_list:
            new_first_name = b[0]
            new_last_name = b[1]
            if first_name == new_first_name and last_name == new_last_name:
                if i[2] == "": i[2] = b[2]
                if i[3] == "": i[3] = b[3]
                if i[4] == "": i[4] = b[4]
                if i[5] == "": i[5] = b[5]
                if i[6] == "": i[6] = b[6]
    result_list = list()
    for c in new_contacts_list:
        if c not in result_list:
            result_list.append(c)
    return result_list


m = main(contacts_list)
r = sort(m)


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(r)
