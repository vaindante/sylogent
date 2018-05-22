from itertools import zip_longest
from random import choice

import allure
from logger import logger
from exceptions import MismatchError, ObjectDataException, ObjectDataFormattedException


class CompareJson:
    start_index = 0
    accuracy = 3
    setter_for_tuning = {
        'dict_list_json': {
            'atr': 'v_in',
            'func': lambda v_in, x: {key: v_in[key] for key in x} if isinstance(v_in, dict) else v_in
        },
        'excludes_keys': {
            'atr': 'v_in',
            'func': lambda v_in, x: {key: v for key, v in v_in.items() if key not in x}
            if isinstance(v_in, dict) else v_in
        },
        'replaced_keys': {
            'atr': 'v_in',
            'func': lambda v_in, x: {x.get(key, key): v for key, v in v_in.items()} if isinstance(v_in, dict) else v_in
        },
        'start_index': {
            'atr': 'start_index',
            'func': lambda v_in, x: x
        },
        'accuracy': {
            'atr': 'accuracy',
            'func': lambda v_in, x: x
        }
    }

    @staticmethod
    def is_instance(v_iter, v_type):
        return all(map(lambda t: isinstance(t, v_type), v_iter))

    def tuning(self, **kwargs):
        for key, value in kwargs.items():
            if value:
                setattr(
                    self,
                    self.setter_for_tuning[key]['atr'],
                    self.setter_for_tuning[key]['func'](self.v_in, value)
                )

    def __call__(self, v_in, v_out, **kwargs):
        self.v_in = v_in if not isinstance(v_in, str) else v_in.strip()
        self.tuning(**kwargs)

        if isinstance(v_out, str):
            v_out = v_out.strip()

        mismatch_items = dict()
        if v_in == '!not_empty' and (v_out and 'нет в ответе' not in v_out if isinstance(v_out, str) else True):
            pass
        elif v_in == '!empty' and not v_out:
            pass
        elif self.v_in != v_out:
            # Сначала проверяем что пришел не список или другой попхожий итератор
            if self.is_instance((self.v_in, v_out), (list, tuple, map)):
                for key, value in enumerate(zip_longest(self.v_in, v_out), start=self.start_index):
                    result = CompareJson()(*value, **kwargs)
                    if result:
                        mismatch_items[key] = result

            elif isinstance(self.v_in, set):
                if self.v_in.symmetric_difference(v_out):
                    return self.formation_error(list(self.v_in), v_out)
                return

            elif self.is_instance((self.v_in, v_out), (int, float)):
                if round(self.v_in, self.accuracy) != round(v_out, self.accuracy):
                    return self.formation_error(self.v_in, v_out)
                return

            elif self.is_instance((self.v_in, v_out), dict):
                for key, value_in in self.v_in.items():
                    result = CompareJson()(
                        value_in,
                        v_out.get(key, 'Поля %r нет в ответе' % key),
                        **kwargs
                    )
                    if result:
                        mismatch_items[key] = result
            else:
                return self.formation_error(self.v_in, v_out)

            return mismatch_items

    @staticmethod
    def formation_error(v_in, v_out):
        return {
            'Хотели': v_in,
            'Получили': v_out
        }


#####################
def correspond_selected_object(
        objects,
        table,
        select_option=None,
        dict_list_json=None,
        excludes_keys=None,
        replaced_keys=None,
        start_index=None,
        accuracy=None,
        return_failed=False
):
    """
    Функция для проверки сравневания двух джисоно валидных объектов

    :param objects: объет который проверяем, может быть типа list или dict
    :param table: объект по которому проверяем objects, может иметь меньше значений чем objects, если проверям list,
                  предпочительнее скидывать tuple (шаблон, таблица; то, как должно быть)
    :param select_option: если задан, то по нему произойдет выборка 1 объекта
    :param dict_list_json: Для провреки будет использованы ключи из списка  
    :param excludes_keys: Исключить ключи из проверки (list)
    :param replaced_keys: replaced JSON keys names after update: {'before_1': 'after_1', 'before_2': 'after_2', ...}
    :param start_index: начальная позиция для нумерации списков
    :param accuracy: знак до которого округлять цивры при проверке
    :param return_failed: return 'Failed'
    :return: item или error
    """
    if select_option:
        item = get_item_from(objects, 'single', 'table', select_option)
    else:
        item = objects

    with allure.step('Сравниваем данные с ожидаемыми значениями'):
        error = CompareJson()(
            table,
            item,
            dict_list_json=dict_list_json,
            excludes_keys=excludes_keys,
            replaced_keys=replaced_keys,
            start_index=start_index,
            accuracy=accuracy
        )
        if error:
            logger.attach_subdebug('Данные которые проверяем', item)
            logger.attach_subdebug('Данные для проверки', table)
            if not return_failed:
                raise MismatchError('Данные не сошлись', error)
            else:
                logger.attach_error('Данные не сошлись', error)
                return 'Failed'


def check_count(objects_list, count, objects_name='-'):
    if isinstance(objects_list, (list, tuple, dict)):
        with allure.step('Проверяем кол-во элементов в %s' % objects_name
                         if objects_name != '-' else 'запрошенных данных'):
            if len(objects_list) != count:
                logger.attach_debug('Objects list:', objects_list)
                raise ObjectDataException(
                    'Количество элементов в "%s" не совпадает с ожидаемым. Хотели: %s, получили: %s' % (
                        objects_name, count,
                        len(objects_list)
                    ))
    else:
        raise TypeError("Переданный объект не является (list, tuple, dict)")


@allure.step('Выбираем объект(ы) из массива данных')
def get_item_from(select_data, amount='single', condition='table', table=None):
    """
    Выбор объекта или объектов из списка объектов
    :param select_data:
    :param amount: "single" or "multiple".  If "single" - return object, if "multiple" - return list of objects
    :param condition: by "table" or "random" (only single data_amount for random condition)
    :param table:
    :return: found_list
    """

    # Choose random object
    def search(item_search, filter_search):
        flag = False
        if isinstance(filter_search, dict):
            # При проверке словаря, идем в глубь по ключам
            for key_filter in filter_search:
                flag = search(item_search[key_filter], filter_search[key_filter])
                if not flag:
                    break

        elif isinstance(filter_search, list):
            # для листа проходим по всем вложеным листам
            for row_filter in filter_search:
                for row_search in item_search:
                    try:
                        flag = search(row_search, row_filter)
                        if flag:
                            break
                    except KeyError:
                        flag = False

        # Для сравнивания строк, будем отрезать лишнии пробелы в начале и конце, как фронт.
        elif isinstance(filter_search, str) and isinstance(item_search, str) \
                and item_search.strip() == filter_search.strip():
            return True

        # Простые значения, в итоге все равно сюда попадаем
        elif item_search == filter_search:
            return True

        return flag

    if condition == "random":
            return choice(select_data)

    # Choose specified object
    elif condition == "table":
        found_list = list()

        if table is None:
            raise Exception('table is None')

        for item in select_data:

            found = True
            for key in table:
                # Оборачиваем станадратные ошибки, для более полного понимания картины
                if not search(item.get(key), table[key]):
                    found = False
                    break

            if found:
                if amount == 'single':
                    return item

                elif amount == 'multiple':
                    found_list.append(item)

                else:
                    raise Exception('Unknown amount property')

        if found_list:
            return found_list

        else:
            logger.attach_info('SELECT_DATA', select_data)
            raise ObjectDataFormattedException("Не найден объект с заданными параметрами: ", table)
