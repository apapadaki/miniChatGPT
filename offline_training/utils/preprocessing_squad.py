import json
import re
import spacy
from collections import Counter

'''
This file is based on the original code from the paper: https://arxiv.org/abs/1606.05250 
and borrows from repo: https://github.com/kushalj001/pytorch-question-answering
'''

def load_json(filename):
    '''
    Input:
     filename: json file location and name

    returns: data from the json file
    '''

    data = json.load(open(filename))
    print('Length of data: ', len(data['data']))
    print('Keys of data: ', data['data'][0].keys())
    print('Title of data: ', data['data'][0]['title'], '\n')

    return data


def add_to_dict(input_list):
    _dict = {}
    _dict['id'] = input_list[0]
    _dict['context'] = input_list[1]
    _dict['question'] = input_list[2]
    _dict['label'] = input_list[3]
    _dict['answer'] = input_list[4]
    return _dict


def parse_data(data_dict):
    '''
    :inputs: data_dict: parse a dictionary

    :return: a list of dictionaries with keys ['context','query','label']
    '''
    data_list = []
    for paragraphs in data_dict:

        for paragraph in paragraphs['paragraphs']:
            context = paragraph['context']

            for question in paragraph['qas']:

                _id = question['id']
                qa = question['question']

                for answer in question['answers']:
                    ans = answer['text']
                    ans_start = answer['answer_start']
                    ans_end = ans_start + len(ans)
                    data_list.append(add_to_dict([_id, context, qa, [ans_start, ans_end], ans]))

    return data_list


def remove_redundant_symbols(input_data):
    '''
    removes extra symbols from context
    :return: filtered context
    '''

    return re.sub(r'\s', ' ', input_data)



def aggregate_text(dataframes):
    '''
    Aggregate the text from context and questions to build a vocabulary
    :param dataframes: list of dataframes
    :return: a list of context and questions
    '''

    text_list = []
    total = 0

    for df in dataframes:
        unique_context, num_unique_context = list(df.context.unique()), df.context.nunique()
        unique_qa, num_unique_qa = list(df.question.unique()), df.question.nunique()
        total += num_unique_qa + num_unique_context
        text_list.extend(unique_context + unique_qa)

    assert len(text_list) == total

    return text_list



def create_word_vocabulary(text_list):
    '''
    Create a world vocabulary from text.
    :param text_list: aggregated list of context and questions
    :return:
        dict word2idx: word to index mapping of words
        dict idx2word: index to word mapping
        list word_vocab: list of words sorted by frequency
    '''
    nlp = spacy.load('en_core_web_sm')
    words_list = []
    for sentence in text_list:
        for word in nlp(sentence, disable=['parser','tagger','ner','lemmatizer']):
            words_list.append(word)

    word_counter = Counter(words_list)

    word_vocab = sorted(word_counter, key=word_counter.get, reverse=True)
    print(f"raw-vocab length: {len(word_vocab)}")
    word_vocab.insert(0, '<unk>')
    word_vocab.insert(1, '<pad>')
    print(f"final vocab length: {len(word_vocab)}")

    # index words
    word2idx = {word: idx for idx, word in enumerate(word_vocab)}
    print(f"word2idx-length: {len(word2idx)}")

    idx2word = {v: k for k, v in word2idx.items()}

    return  word2idx, idx2word, word_vocab




