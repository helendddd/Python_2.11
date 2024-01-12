#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def create_template_closure(template):
    """
    Внешняя функция создает замыкание для работы с заданным шаблоном.
    """
    def format_name(surname, name):
        """
        Внутренняя функция форматирует строку
        с использованием переданных фамилии и имени.
        """
        string = template.replace('%F%', surname).replace('%N%', name)
        return string

    return format_name


if __name__ == "__main__":
    template = "Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций."
    name_formatter = create_template_closure(template)

    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")

    result = name_formatter(first_name, last_name)
    print(result)
