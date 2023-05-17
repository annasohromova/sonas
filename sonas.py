import random

import os

def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

rus:list=loe_failist("rus.txt")

def load_dictionary(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        words = f.read().splitlines()
    return words

def save_dictionary(file_path, words):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(words))

def translate_word(word, source_lang, target_lang):
    source_dict = load_dictionary(f"{source_lang}.txt")
    target_dict = load_dictionary(f"{target_lang}.txt")

    if source_lang == "rus":
        source_words, target_words = source_dict, target_dict
    else:
        source_words, target_words = target_dict, source_dict

    if word in source_words:
        index = source_words.index(word)
        return target_words[index]
    else:
        return None

def add_word(word_rus, word_est):
    rus_dict = load_dictionary("rus.txt")
    est_dict = load_dictionary("est.txt")

    if word_rus in rus_dict or word_est in est_dict:
        return False

    rus_dict.append(word_rus)
    est_dict.append(word_est)

    save_dictionary("rus.txt", rus_dict)
    save_dictionary("est.txt", est_dict)

    return True

def edit_word(old_word_rus, old_word_est, new_word_rus, new_word_est):
    rus_dict = load_dictionary("rus.txt")
    est_dict = load_dictionary("est.txt")

    if old_word_rus in rus_dict and old_word_est in est_dict:
        index_rus = rus_dict.index(old_word_rus)
        index_est = est_dict.index(old_word_est)
        rus_dict[index_rus] = new_word_rus
        est_dict[index_est] = new_word_est

        save_dictionary("rus.txt", rus_dict)
        save_dictionary("est.txt", est_dict)

        return True
    else:
        return False

def check_word_knowledge():
    rus_dict = load_dictionary("rus.txt")
    est_dict = load_dictionary("est.txt")

    total_words = len(rus_dict)
    correct_answers = 0

    for i in range(total_words):
        index = random.randint(0, total_words - 1)
        russian_word = rus_dict[index]
        estonian_word = est_dict[index]

        print(f"Как переводится слово '{russian_word}' на эстонский?")
        user_translation = input()

        if user_translation == estonian_word:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный перевод: {estonian_word}")

    percentage_correct = (correct_answers / total_words) * 100
    print(f"\nВы правильно перевели {correct_answers} слов(а) из {total_words}.")
    print(f"Процент правильных ответов: {percentage_correct}%")



