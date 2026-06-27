from pprint import pprint
import csv
import re


def normalize_name(contact):
    full_name = " ".join(contact[:3]).split()
    contact[0] = full_name[0] if len(full_name) > 0 else ""
    contact[1] = full_name[1] if len(full_name) > 1 else ""
    contact[2] = full_name[2] if len(full_name) > 2 else ""
    return contact


def normalize_phone(contact):
    phone_pattern = re.compile(
        r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
        r"(\s*\(?доб\.?\s*(\d+)\)?)?"
    )

    phone = contact[5]

    def phone_replacer(match):
        result = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
        if match.group(7):
            result += f" доб.{match.group(7)}"
        return result

    contact[5] = phone_pattern.sub(phone_replacer, phone)
    return contact


def merge_duplicates(contacts):
    result = {}

    for contact in contacts:
        key = (contact[0], contact[1])

        if key not in result:
            result[key] = contact
        else:
            existing_contact = result[key]

            for index, value in enumerate(contact):
                if existing_contact[index] == "" and value != "":
                    existing_contact[index] = value

    return list(result.values())


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

headers = contacts_list[0]
contacts = contacts_list[1:]

normalized_contacts = []

for contact in contacts:
    contact = normalize_name(contact)
    contact = normalize_phone(contact)
    normalized_contacts.append(contact)

merged_contacts = merge_duplicates(normalized_contacts)

contacts_list = [headers] + merged_contacts

pprint(contacts_list)

with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(contacts_list)