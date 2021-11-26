import csv

from pybadges import badge

from utils import fileproc

with open('res/iverbs.csv', 'r') as iverb_csvfile:
    with open('res/inouns.csv', 'r') as inouns_csvfile:
        word_dict = {}
        word_dict = fileproc.gen_irregular_dict_from_csv(
            iverb_csvfile, inouns_csvfile)
        print(f"Irregular单词条目：{len(word_dict)}个")
        fileproc.save_word_dict("word_dict.json", word_dict)
        s = badge(left_text="Irregular Words", right_text=f"{len(word_dict)}")
        with open('irregular.svg', 'w') as f:
            f.write(s)

with open('res/picwords.csv', 'r') as csvfile:
    word_dict = {}
    chapter_dict = {}
    word_dict, chapter_dict = fileproc.gen_pic_dict_from_csv(csvfile)
    print(f"看图识词单词条目：{len(word_dict)}个")
    fileproc.save_word_dict("pic_dict.json", word_dict)
    fileproc.save_word_dict("chapter_dict.json", chapter_dict)

with open('res/grammar.csv', 'r') as csvfile:
    grammar_dict = {}
    grammar_dict = fileproc.gen_grammar_dict_from_csv(csvfile)
    print(f"语法条目：{len(grammar_dict)}个")
    fileproc.save_word_dict("grammar_dict.json", grammar_dict)
