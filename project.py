import ast

from flask import Flask, request, jsonify, app
# import sys
import urllib.parse
import re
from urllib.request import Request, urlopen

# path = '/dictionary_json/oussaElDictionary/Dictionary'
# if path not in sys.path:
#     sys.path.insert(0, path)

app = Flask(__name__)


@app.route("/apiou19990612Dictionary", methods=['GET'])
def dictionary_json():
    d = {}

    di = Dictionary()
    word = str(request.args['word'])
    data_uk = get_dictionary_data('https://www.lexico.com/definition/',
                                  word.replace('é', 'e').replace('è', 'e').replace('à', 'a').lower())
    data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                  word.replace('é', 'e').replace('è', 'e').replace('à', 'a').lower())
    if di.get_noun_or_verb(data_uk) != ['word not find'] and di.get_noun_or_verb(data_uk) != ['500']:
        get_word_json = di.get_word(data_uk, word)
        get_noun_or_verb_json = di.get_noun_or_verb(data_uk)
        get_definition_json = di.get_definition(data_uk)
        get_example_json = di.get_example(data_uk)
        get_more_example_json = di.get_more_example(data_uk)
        if di.get_more_definition(data_us) != ["word not find"]:
            get_more_definition_json = di.get_more_definition(data_us)
        else:
            get_more_definition_json = di.get_more_definition(data_uk)
        get_synonym_json = di.get_synonym(data_uk)
        get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
        if get_pronunciation_json == ["500", "500"]:
            if str(word)[len(str(word)) - 1] == 's':
                word = str(word)[:len(str(word)) - 1]
                data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                              word.replace('é', 'e').replace('è', 'e').replace('à', 'a').lower())
                if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != ['500']:
                    get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
                word = word + 's'
            if str(word)[len(str(word)) - 3:] == 'ies':
                word = str(word)[:len(str(word)) - 3] + 'y'
                data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                              word.replace('é', 'e').replace('è', 'e').replace('à', 'a').lower())
                if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != ['500']:
                    get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
    else:
        data_uk = get_dictionary_data('https://www.lexico.com/definition/',
                                      word.replace(" ", "_").replace('é', 'e').replace('è', 'e').replace('à',
                                                                                                         'a').lower())
        data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                      word.replace(" ", "_").replace('é', 'e').replace('è', 'e').replace('à',
                                                                                                         'a').lower())
        if di.get_noun_or_verb(data_uk) != ['word not find'] and di.get_noun_or_verb(data_uk) != ['500']:
            get_word_json = di.get_word(data_uk, word)
            get_noun_or_verb_json = di.get_noun_or_verb(data_uk)
            get_definition_json = di.get_definition(data_uk)
            get_example_json = di.get_example(data_uk)
            get_more_example_json = di.get_more_example(data_uk)
            if di.get_more_definition(data_us) != ["word not find"]:
                get_more_definition_json = di.get_more_definition(data_us)
            else:
                get_more_definition_json = di.get_more_definition(data_uk)
            get_synonym_json = di.get_synonym(data_uk)
            get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
            if get_pronunciation_json == ["500", "500"]:
                if str(word)[len(str(word)) - 1] == 's':
                    word = str(word)[:len(str(word)) - 1]
                    data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                                  word.replace(" ", "_").replace('é', 'e').replace('è', 'e').replace(
                                                      'à', 'a').lower())
                    if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != ['500']:
                        get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
                    word = word + 's'
                if str(word)[len(str(word)) - 3:] == 'ies':
                    word = str(word)[:len(str(word)) - 3] + 'y'
                    data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                                  word.replace(" ", "_").replace('é', 'e').replace('è', 'e').replace(
                                                      'à', 'a').lower())
                    if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != ['500']:
                        get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
        else:
            data_uk = get_dictionary_data('https://www.lexico.com/definition/',
                                          word.replace(" ", "-").replace('é', 'e').replace('è', 'e').replace('à',
                                                                                                             'a').lower())
            data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                          word.replace(" ", "-").replace('é', 'e').replace('è', 'e').replace('à',
                                                                                                             'a').lower())
            if di.get_noun_or_verb(data_uk) != ['word not find'] and di.get_noun_or_verb(data_uk) != ['500']:
                get_word_json = di.get_word(data_uk, word)
                get_noun_or_verb_json = di.get_noun_or_verb(data_uk)
                get_definition_json = di.get_definition(data_uk)
                get_example_json = di.get_example(data_uk)
                get_more_example_json = di.get_more_example(data_uk)
                if di.get_more_definition(data_us) != ["word not find"]:
                    get_more_definition_json = di.get_more_definition(data_us)
                else:
                    get_more_definition_json = di.get_more_definition(data_uk)
                get_synonym_json = di.get_synonym(data_uk)
                get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
                if get_pronunciation_json == ["500", "500"]:
                    if str(word)[len(str(word)) - 1] == 's':
                        word = str(word)[:len(str(word)) - 1]
                        data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                                      word.replace(" ", "-").replace('é', 'e').replace('è',
                                                                                                       'e').replace('à',
                                                                                                                    'a').lower())
                        if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != [
                            '500']:
                            get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
                        word = word + 's'
                    if str(word)[len(str(word)) - 3:] == 'ies':
                        word = str(word)[:len(str(word)) - 3] + 'y'
                        data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                                      word.replace(" ", "-").replace('é', 'e').replace('è',
                                                                                                       'e').replace('à',
                                                                                                                    'a').lower())
                        if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != [
                            '500']:
                            get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
            else:
                get_word_json = di.get_word(data_uk, word)
                get_noun_or_verb_json = di.get_noun_or_verb(data_uk)
                get_definition_json = di.get_definition(data_uk)
                get_example_json = di.get_example(data_uk)
                get_more_example_json = di.get_more_example(data_uk)
                if di.get_more_definition(data_us) != ["word not find"]:
                    get_more_definition_json = di.get_more_definition(data_us)
                else:
                    get_more_definition_json = di.get_more_definition(data_uk)
                get_synonym_json = di.get_synonym(data_uk)
                get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
                if get_pronunciation_json == ["500", "500"]:
                    if len(str(word)) != 0:
                        if str(word)[len(str(word)) - 1] == 's':
                            word = str(word)[:len(str(word)) - 1]
                            data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                                          word.replace('é', 'e').replace('è', 'e').replace('à',
                                                                                                           'a').lower())
                            if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != [
                                '500']:
                                get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
                            word = word + 's'
                    if str(word)[len(str(word)) - 3:] == 'ies':
                        word = str(word)[:len(str(word)) - 3] + 'y'
                        data_us = get_dictionary_data('https://www.lexico.com/en/definition/',
                                                      word.replace('é', 'e').replace('è', 'e').replace('à',
                                                                                                       'a').lower())
                        if di.get_noun_or_verb(data_us) != ['word not find'] and di.get_noun_or_verb(data_us) != [
                            '500']:
                            get_pronunciation_json = di.get_pronunciation(data_us, data_uk)
    d['word'] = get_word_json
    d['noun or verb'] = get_noun_or_verb_json
    d['pronunciation'] = get_pronunciation_json
    d['definition'] = get_definition_json
    d['example'] = get_example_json
    d['more example'] = get_more_example_json
    d['more definition'] = get_more_definition_json
    d['synonym'] = get_synonym_json

    return jsonify(d)



def get_dictionary_data(link, word):
    link = link + word

    headers = {}
    headers[
        'use-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

    try:
        req = Request(link, headers=headers)
        web_page = urlopen(req)
        data = web_page.read()
    except Exception:
        data = 'word not find'
    return data




class Dictionary:

    def get_word(self, data, mot):
        if data != 'word not find':
            try:
                word = ast.literal_eval(
                    "b'" + re.findall(r'<span class="hw" data-headword-id=".*?">(.*?)</span>', str(data))[
                        0] + "'").decode('utf-8')
            except IndexError:
                word = '500'
            if re.search('<sup>\d</sup>', str(word)):
                word = mot.title()
            elif '<sup></sup>' in str(word):
                word = str(word).replace('<sup></sup>', '')
        else:
            word = 'word not find'
        return word

    def get_noun_or_verb(self, data):
        if data != 'word not find':
            # cross_reference = re.findall(r'<div class="crossReference">(.*?)<a href="/definition/', str(data))
            # k = len(cross_reference)
            pos = re.findall(r'<span class="pos">(.*?)</span>', str(data))
            n = len(pos)
            noun_or_verb = []
            if n == 0:
                noun_or_verb = ['500']
            elif n == 1:
                if pos[0] != "":
                    # noun_or_verb.append(ast.literal_eval("b'<span class=\"pos\">"+pos[0]+"</span>'").decode('utf-8'))
                    noun_or_verb.append(pos[0])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        0] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")
            elif n == 2:
                if pos[0] != "":
                    noun_or_verb.append(pos[0])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        0] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>.*?<span class="pos">' +
                                               pos[1] + '</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")
                if pos[1] != "":
                    noun_or_verb.append(pos[1])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        1] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")

            elif n == 3:
                if pos[0] != "":
                    noun_or_verb.append(pos[0])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        0] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>.*?<span class="pos">' +
                                               pos[1] + '</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")
                if pos[1] != "":
                    noun_or_verb.append(pos[1])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        1] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>.*?<span class="pos">' +
                                               pos[2] + '</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")
                if pos[2] != "":
                    noun_or_verb.append(pos[2])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        2] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")

            else:
                if pos[0] != "":
                    noun_or_verb.append(pos[0])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        0] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>.*?<span class="pos">' +
                                               pos[1] + '</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")
                if pos[1] != "":
                    noun_or_verb.append(pos[1])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        1] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>.*?<span class="pos">' +
                                               pos[2] + '</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")
                if pos[2] != "":
                    noun_or_verb.append(pos[2])
                else:
                    sense_regions = re.findall(r'<span class="pos">' + pos[
                        2] + '</span>.*?<span class="sense-regions domain_labels">(.*?)</span>.*?<span class="pos">' +
                                               pos[3] + '</span>', str(data))
                    k = len(sense_regions)
                    if k != 0:
                        noun_or_verb.append(sense_regions[0])
                    else:
                        noun_or_verb.append("information")

        else:
            noun_or_verb = ['word not find']
        return noun_or_verb

    def get_pronunciation(self, data_us, data_uk):
        if data_uk != 'word not find' or data_us != 'word not find':
            pronunciation = {}
            try:
                audios_us = re.findall(r'audio src="(.*?)mp3"', str(data_us))
                audio_us = audios_us[0] + "mp3"
            except IndexError:
                audio_us = '500'
            try:
                phoneticspellings_us = re.findall(r'<span class="phoneticspelling">(.*?)</span>', str(data_us))
                phoneticspelling_us = ast.literal_eval("b'" + phoneticspellings_us[0] + "'").decode('utf-8')
            except IndexError:
                phoneticspelling_us = '500'
            try:
                audios_uk = re.findall(r'audio src="(.*?)mp3"', str(data_uk))
                audio_uk = audios_uk[0] + "mp3"
            except IndexError:
                audio_uk = '500'
            try:
                phoneticspellings_uk = re.findall(r'<span class="phoneticspelling">(.*?)</span>', str(data_uk))
                phoneticspelling_uk = ast.literal_eval("b'" + phoneticspellings_uk[0] + "'").decode('utf-8')
            except IndexError:
                phoneticspelling_uk = '500'

            pronunciation['us'] = [audio_us, phoneticspelling_us]

            pronunciation['uk'] = [audio_uk, phoneticspelling_uk]
        else:
            pronunciation = {'word not find': 'word not find'}
        return pronunciation

    def get_definition(self, data):
        if data != 'word not find':
            pos = re.findall(r'<span class="pos">(.*?)</span>', str(data))
            k = len(re.findall(r'<div class="crossReference">(.*?)<a href="/definition/', str(data)))
            n = len(pos)
            m = len(re.findall(r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                               str(data)))
            l = len(re.findall(r'<p class="derivative_of">(.*?)<a href=".*?">.*?</a></p>', str(data)))
            pos0 = 0
            pos1 = 1
            pos2 = 2
            ind = 0
            cross_reference0 = ''
            important_cross = False
            if k != 0:
                cross_reference0 = re.findall(r'<div class="crossReference">(.*?)<a href="/definition/', str(data))[0]
                if n == 1:
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            0] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
                elif n == 2:
                    pas_c = ''
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[0] + '</span>(.*?)<span class="pos">' + pos[1] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text):
                        pos0 = 1
                        pos2 = 0
                        ind = 1
                        pas_c = 'pass'
                    try:
                        text = re.findall(r'<span class="pos">' + pos[1] + '</span>(.*?)$', str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        pos2 = 1
                        ind = 2
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            pos2] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
                elif n == 3:
                    pas_c = ''
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[0] + '</span>(.*?)<span class="pos">' + pos[1] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text):
                        pos0 = 1
                        pos1 = 2
                        pos2 = 0
                        ind = 1
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[1] + '</span>(.*?)<span class="pos">' + pos[2] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        pos0 = 0
                        pos1 = 2
                        pos2 = 1
                        ind = 2
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[2] + '</span>(.*?)<span class="pos">' + pos[3] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        ind = 3
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            pos2] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
                else:
                    pas_c = ''
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[0] + '</span>(.*?)<span class="pos">' + pos[1] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text):
                        pos0 = 1
                        pos1 = 2
                        pos2 = 0
                        ind = 1
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[1] + '</span>(.*?)<span class="pos">' + pos[2] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        pos0 = 0
                        pos1 = 2
                        pos2 = 1
                        ind = 2
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[2] + '</span>(.*?)<span class="pos">' + pos[3] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        ind = 3
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            pos2] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
            if (m != 0 and k == 0) or (m != 0 and important_cross):
                if n == 1:
                    if m == 1:
                        definition = [ast.literal_eval("b'" + re.findall(
                            r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                            str(data))[0] + "'").decode('utf-8'), '', '']
                    elif m == 2:
                        definition = [ast.literal_eval("b'" + re.findall(
                            r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                            str(data))[0] + "'").decode('utf-8'),
                                      ast.literal_eval("b'" + re.findall(
                                          r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                                          str(data))[1] + "'").decode('utf-8'), '']
                    else:
                        definition = [ast.literal_eval("b'" + re.findall(
                            r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                            str(data))[0] + "'").decode('utf-8'),
                                      ast.literal_eval("b'" + re.findall(
                                          r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                                          str(data))[1] + "'").decode('utf-8'),
                                      ast.literal_eval("b'" + re.findall(
                                          r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                                          str(data))[2] + "'").decode('utf-8')]
                elif n == 2:
                    try:
                        definition1 = ast.literal_eval("b'" + re.findall(r'<span class="pos">' + pos[
                            0] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                                                                         pos[1] + '</span>', str(data))[
                            0] + "'").decode('utf-8')
                    except IndexError:
                        definition1 = ''
                    try:
                        definition2 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?<span class="pos">' + pos[
                                1] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                            str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        definition2 = ''
                    definition = [definition1, definition2, '']
                elif n == 3:
                    try:
                        definition1 = ast.literal_eval("b'" + re.findall(r'<span class="pos">' + pos[
                            0] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                                                                         pos[1] + '</span>.*?<span class="pos">' + pos[
                                                                             2] + '</span>', str(data))[
                            0] + "'").decode('utf-8')
                    except IndexError:
                        definition1 = ''
                    try:
                        definition2 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?<span class="pos">' + pos[
                                1] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                            pos[2] + '</span>', str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        definition2 = ''
                    try:
                        definition3 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[1] + '</span>.*?<span class="pos">' + pos[
                                2] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                            str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        definition3 = ''
                    definition = [definition1, definition2, definition3]
                else:
                    try:
                        definition1 = ast.literal_eval("b'" + re.findall(r'<span class="pos">' + pos[
                            0] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                                                                         pos[1] + '</span>.*?<span class="pos">' + pos[
                                                                             2] + '</span>', str(data))[
                            0] + "'").decode('utf-8')
                    except IndexError:
                        definition1 = ''
                    try:
                        definition2 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?<span class="pos">' + pos[
                                1] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                            pos[2] + '</span>.*?<span class="pos">' + pos[3] + '</span>', str(data))[0] + "'").decode(
                            'utf-8')
                    except IndexError:
                        definition2 = ''
                    try:
                        definition3 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[1] + '</span>.*?<span class="pos">' + pos[
                                2] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                            pos[3] + '</span>', str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        definition3 = ''
                    definition = [definition1, definition2, definition3]
            else:
                if m == 0 and k == 0 and l == 0:
                    definition = ['500']
                    return definition
                if m == 0 and k == 0 and l != 0:
                    return ["definitionWithWordToSearch",
                            [re.findall(r'<p class="derivative_of">(.*?)<a href=".*?">.*?</a></p>', str(data))[0],
                             re.findall(r'<p class="derivative_of">.*?<a href=".*?">(.*?)</a></p>', str(data))[0]],
                            ['', ''], ['', '']]
                definition = [cross_reference0, re.findall(r'<a href="/definition/(.*?)">(.*?)</a>', str(data))[0][1]]
                definition_with_word_to_search = []
                if n == 1:
                    definition_with_word_to_search.append(definition)
                    definition_with_word_to_search.append(['', ''])
                    definition_with_word_to_search.append(['', ''])
                elif n == 2:
                    if m == 0:
                        definition_with_word_to_search.append(['', ''])
                        definition_with_word_to_search.append(['', ''])
                        definition_with_word_to_search.insert(ind - 1, definition)
                    else:
                        try:
                            definition_with_word_to_search.append([ast.literal_eval("b'" + re.findall(
                                r'<span class="pos">' + pos[
                                    pos0] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                                str(data))[0] + "'").decode('utf-8'), ''])
                        except IndexError:
                            return ['500']
                        definition_with_word_to_search.append(['', ''])
                        definition_with_word_to_search.insert(ind - 1, definition)

                    # else:
                    #     definition_with_word_to_search.append(ast.literal_eval("b'"+re.findall(r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>', str(data))[0]+"'").decode('utf-8'))
                    #     definition_with_word_to_search.append(ast.literal_eval("b'"+re.findall(r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>', str(data))[1]+"'").decode('utf-8'))
                    #     definition_with_word_to_search.insert(ind-1, definition)
                elif n == 3:
                    try:
                        definition_with_word_to_search.append([ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[
                                pos0] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                            pos[pos0 + 1] + '</span>', str(data))[0] + "'").decode('utf-8'), ''])
                    except IndexError:
                        return ['500']
                    definition_with_word_to_search.append([ast.literal_eval("b'" + re.findall(
                        r'<span class="pos">' + pos[
                            pos1] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                        str(data))[0] + "'").decode('utf-8'), ''])
                    definition_with_word_to_search.insert(ind - 1, definition)
                else:
                    try:
                        definition_with_word_to_search.append([ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[
                                pos0] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                            pos[pos0 + 1] + '</span>', str(data))[0] + "'").decode('utf-8'), ''])
                    except IndexError:
                        return ['500']
                    definition_with_word_to_search.append([ast.literal_eval("b'" + re.findall(
                        r'<span class="pos">' + pos[
                            pos1] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                        pos[pos1 + 1] + '</span>', str(data))[0] + "'").decode('utf-8'), ''])
                    if ind != 0:
                        definition_with_word_to_search.insert(ind - 1, definition)
                    else:
                        definition_with_word_to_search.pop(0)
                        definition_with_word_to_search.append([ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[
                                2] + '</span>.*?<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>.*?<span class="pos">' +
                            pos[3] + '</span>', str(data))[0] + "'").decode('utf-8'), ''])
                definition_with_word_to_search.insert(0, "definitionWithWordToSearch")
                return definition_with_word_to_search
        else:
            definition = ['word not find']
        return definition

    def get_example(self, data):
        if data != 'word not find':
            pos = re.findall(r'<span class="pos">(.*?)</span>', str(data))
            n = len(pos)
            k = len(re.findall(r'<div class="crossReference">(.*?)<a href="/definition/', str(data)))
            m = len(re.findall(r'&lsquo;(.*?)&rsquo;', str(data)))
            pos0 = 0
            pos1 = 1
            pos2 = 2
            ind = 0
            important_cross = False
            if n == 0:
                return ['500']
            if k != 0:
                cross_reference0 = re.findall(r'<div class="crossReference">(.*?)<a href="/definition/', str(data))[0]
                if n == 1:
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            0] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
                elif n == 2:
                    pas_c = ''
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[0] + '</span>(.*?)<span class="pos">' + pos[1] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text):
                        ind = 1
                        pos0 = 1
                        pos2 = 0
                        pas_c = 'pass'
                    try:
                        text = re.findall(r'<span class="pos">' + pos[1] + '</span>(.*?)$', str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        ind = 2
                        pos2 = 1
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            pos2] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
                elif n == 3:
                    pas_c = ''
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[0] + '</span>(.*?)<span class="pos">' + pos[1] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text):
                        pos0 = 1
                        pos1 = 2
                        pos2 = 0
                        ind = 1
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[1] + '</span>(.*?)<span class="pos">' + pos[2] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        pos0 = 0
                        pos1 = 2
                        pos2 = 1
                        ind = 2
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[2] + '</span>(.*?)<span class="pos">' + pos[3] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        ind = 3
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            pos2] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
                else:
                    pas_c = ''
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[0] + '</span>(.*?)<span class="pos">' + pos[1] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text):
                        pos0 = 1
                        pos1 = 2
                        pos2 = 0
                        ind = 1
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[1] + '</span>(.*?)<span class="pos">' + pos[2] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        pos0 = 0
                        pos1 = 2
                        pos2 = 1
                        ind = 2
                        pas_c = 'pass'
                    try:
                        text = re.findall(
                            r'<span class="pos">' + pos[2] + '</span>(.*?)<span class="pos">' + pos[3] + '</span>',
                            str(data))[0]
                    except IndexError:
                        text = ''
                    if re.search(cross_reference0, text) and pas_c == '':
                        ind = 3
                    try:
                        text_cross = re.findall(r'<span class="pos">' + pos[
                            pos2] + '</span>(.*?)<div class="crossReference">' + cross_reference0 + '<a href="/definition/',
                                                str(data))[0]
                    except IndexError:
                        text_cross = ''
                    if re.search('<span class="ind one-click-content" data-no-definition="\[.*?]".*?>', text_cross):
                        important_cross = True
            if (m != 0 and k == 0) or (m != 0 and important_cross):
                if n == 1:
                    if m == 1:
                        example = [
                            ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[0] + "'").decode(
                                'utf-8'), '', '']
                    elif m == 2:
                        example = [
                            ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[0] + "'").decode(
                                'utf-8'),
                            ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[1] + "'").decode(
                                'utf-8'), '']
                    else:
                        example = [
                            ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[0] + "'").decode(
                                'utf-8'),
                            ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[1] + "'").decode(
                                'utf-8'),
                            ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[2] + "'").decode(
                                'utf-8')]
                elif n == 2:
                    try:
                        example1 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                1] + '</span>', str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        example1 = ''
                    try:
                        example2 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?<span class="pos">' + pos[
                                1] + '</span>.*?&lsquo;(.*?)&rsquo;', str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        example2 = ''
                    example = [example1, example2, '']
                elif n == 3:
                    try:
                        example1 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                1] + '</span>.*?<span class="pos">' + pos[2] + '</span>', str(data))[0] + "'").decode(
                            'utf-8')
                    except IndexError:
                        example1 = ''
                    try:
                        example2 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?<span class="pos">' + pos[
                                1] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[2] + '</span>',
                            str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        example2 = ''
                    try:
                        example3 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[1] + '</span>.*?<span class="pos">' + pos[
                                2] + '</span>.*?&lsquo;(.*?)&rsquo;', str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        example3 = ''
                    example = [example1, example2, example3]
                else:
                    try:
                        example1 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                1] + '</span>.*?<span class="pos">' + pos[2] + '</span>', str(data))[0] + "'").decode(
                            'utf-8')
                    except IndexError:
                        example1 = ''
                    try:
                        example2 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[0] + '</span>.*?<span class="pos">' + pos[
                                1] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                2] + '</span>.*?<span class="pos">' + pos[3] + '</span>', str(data))[0] + "'").decode(
                            'utf-8')
                    except IndexError:
                        example2 = ''
                    try:
                        example3 = ast.literal_eval("b'" + re.findall(
                            r'<span class="pos">' + pos[1] + '</span>.*?<span class="pos">' + pos[
                                2] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[3] + '</span>',
                            str(data))[0] + "'").decode('utf-8')
                    except IndexError:
                        example3 = ''
                    example = [example1, example2, example3]
            else:
                example = []
                if m == 0:
                    example = ['', '', '']
                else:
                    if n == 1:
                        example = ['', '', '']
                    elif n == 2:
                        try:
                            example2 = ast.literal_eval("b'" + re.findall(
                                r'<span class="pos">' + pos[pos0] + '</span>.*?&lsquo;(.*?)&rsquo;', str(data))[
                                0] + "'").decode('utf-8')
                        except IndexError:
                            example2 = ''
                        example.append(example2)
                        example.append('')
                        example.insert(ind - 1, '')
                    elif n == 3:
                        try:
                            example2 = ast.literal_eval("b'" + re.findall(r'<span class="pos">' + pos[
                                pos0] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                                                              pos0 + 1] + '</span>', str(data))[
                                0] + "'").decode('utf-8')
                        except IndexError:
                            example2 = ''
                        try:
                            example3 = ast.literal_eval("b'" + re.findall(
                                r'<span class="pos">' + pos[pos1] + '</span>.*?&lsquo;(.*?)&rsquo;', str(data))[
                                0] + "'").decode('utf-8')
                        except IndexError:
                            example3 = ''
                        example.append(example2)
                        example.append(example3)
                        example.insert(ind - 1, '')
                    else:
                        try:
                            example2 = ast.literal_eval("b'" + re.findall(r'<span class="pos">' + pos[
                                pos0] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                                                              pos0 + 1] + '</span>', str(data))[
                                0] + "'").decode('utf-8')
                        except IndexError:
                            example2 = ''
                        try:
                            example3 = ast.literal_eval("b'" + re.findall(r'<span class="pos">' + pos[
                                pos1] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' + pos[
                                                                              pos1 + 1] + '</span>', str(data))[
                                0] + "'").decode('utf-8')
                        except IndexError:
                            example3 = ''
                        example.append(example2)
                        example.append(example3)
                        if ind != 0:
                            example.insert(ind - 1, '')
                        else:
                            example.pop(0)
                            example.append(ast.literal_eval("b'" + re.findall(
                                r'<span class="pos">' + pos[3] + '</span>.*?&lsquo;(.*?)&rsquo;.*?<span class="pos">' +
                                pos[4] + '</span>', str(data))[0] + "'").decode('utf-8'))
                # if True:
                #     if m == 0:
                #         example = ['', '', '']
                #     else:
                #         if n == 1:
                #             example = ['', '', '']
                #         elif n == 2:
                #             example1 = ''
                #             try:
                #                 example2 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[1]+'</span>.*?&lsquo;(.*?)&rsquo;', str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example2 = ''
                #             example = [example1, example2, '']
                #         elif n == 3:
                #             example1 = ''
                #             try:
                #                 example2 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[1]+'</span>.*?&lsquo;(.*?)&rsquo;.*?'+pos[2], str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example2 = ''
                #             try:
                #                 example3 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[2]+'</span>.*?&lsquo;(.*?)&rsquo;', str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example3 = ''
                #             example = [example1, example2, example3]
                #         else:
                #             example1 = ''
                #             try:
                #                 example2 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[1]+'</span>.*?&lsquo;(.*?)&rsquo;.*?'+pos[2], str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example2 = ''
                #             try:
                #                 example3 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[2]+'</span>.*?&lsquo;(.*?)&rsquo;.*?'+pos[3], str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example3 = ''
                #             example = [example1, example2, example3]
                # elif k == 2:
                #     if m == 0:
                #         example = ['', '', '']
                #     else:
                #         if n == 1 or n == 2:
                #             example = ['', '', '']
                #         elif n == 3:
                #             example1 = ''
                #             example2 = ''
                #             try:
                #                 example3 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[2]+'</span>.*?&lsquo;(.*?)&rsquo;', str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example3 = ''
                #             example = [example1, example2, example3]
                #         else:
                #             example1 = ''
                #             example2 = ''
                #             try:
                #                 example3 = ast.literal_eval("b'"+re.findall(r'<span class="pos">'+pos[2]+'</span>.*?&lsquo;(.*?)&rsquo;.*?'+pos[3], str(data))[0]+"'").decode('utf-8')
                #             except IndexError:
                #                 example3 = ''
                #             example = [example1, example2, example3]
                # else:
                #     example = ['', '', '']
        else:
            example = ['word not find']
        return example

    def get_more_definition(self, data):
        if data != 'word not find':
            m = len(re.findall(r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>',
                               str(data)))
            if m != 0:
                if m > 15:
                    definition = [ast.literal_eval("b'" + re.findall(
                        r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>', str(data))[
                        i] + "'").decode('utf-8') for i in range(15)]
                else:
                    definition = [ast.literal_eval("b'" + re.findall(
                        r'<span class="ind one-click-content" data-no-definition="\[.*?]".*?>(.*?)</span>', str(data))[
                        i] + "'").decode('utf-8') for i in range(m)]
            else:
                definition = ['']
        else:
            definition = ['word not find']
        return definition

    def get_more_example(self, data):
        if data != 'word not find':
            m = len(re.findall(r'&lsquo;(.*?)&rsquo;', str(data)))
            if m != 0:
                if m > 15:
                    example = [
                        ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[i] + "'").decode('utf-8')
                        for i in range(15)]
                else:
                    example = [
                        ast.literal_eval("b'" + re.findall(r'&lsquo;(.*?)&rsquo;', str(data))[i] + "'").decode('utf-8')
                        for i in range(m)]
            else:
                example = ['']
        else:
            example = ['word not find']
        return example

    def get_synonym(self, data):
        if data != 'word not find':
            m = len(re.findall(r'<span class="syn">, (.*?)</span>', str(data)))
            if m != 0:
                if m > 7:
                    synonym = [ast.literal_eval(
                        "b'" + re.findall(r'<span class="syn">, (.*?)</span>', str(data))[i] + "'").decode('utf-8') for
                               i in range(7)]
                else:
                    synonym = [ast.literal_eval(
                        "b'" + re.findall(r'<span class="syn">, (.*?)</span>', str(data))[i] + "'").decode('utf-8') for
                               i in range(m)]
            else:
                synonym = ['']
        else:
            synonym = ['word not find']
        return synonym



if __name__ == "__main__":
    app.run(debug=True)
