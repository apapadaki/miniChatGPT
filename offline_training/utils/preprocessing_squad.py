import json
import re
import spacy
from collections import Counter

'''
This file is based on the original code from the paper: https://arxiv.org/abs/1606.05250 
and borrows from repo: https://github.com/kushalj001/pytorch-question-answering
'''

nlp = spacy.load('en_core_web_sm')


def load_json(filename):
    """
    Input:
     filename: json file location and name

    returns: data from the json file
    """

    data = json.load(open(filename))
    print('Length of data: ', len(data['data']))
    print('Keys of data: ', data['data'][0].keys())
    print('Title of data: ', data['data'][0]['title'], '\n')

    return data


def add_to_dict(input_list):
    """
    List to dictionary converter.

    :param input_list: add to a dictionary a list of the form [_id, context, qa, [ans_start, ans_end], ans]
    :return:
    """
    _dict = {'id': input_list[0], 'context': input_list[1], 'question': input_list[2], 'label': input_list[3],
             'answer': input_list[4]}
    return _dict


def parse_data(data_dict):
    """
    :inputs: data_dict: parse a dictionary

    :return: a list of dictionaries with keys ['context','query','label']
    """
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
    """
    removes extra symbols from context
    :return: filtered data
    """

    return re.sub(r'\s', ' ', input_data)


def aggregate_text(dataframes):
    """
    Aggregate the text from context and questions to build a vocabulary
    :param dataframes: list of dataframes
    :return: a list of context and questions
    """

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
    """
    Create a world vocabulary from text.
    :param text_list: aggregated list of context and questions
    :return:
        dict word2idx: word to index mapping of words
        dict idx2word: index to word mapping
        list word_vocab: list of words sorted by frequency
    """
    words_list = []
    for sentence in text_list:
        for word in nlp(sentence, disable=['parser', 'tagger', 'ner', 'lemmatizer']):
            words_list.append(word.text)

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

    return word2idx, idx2word, word_vocab


def cq_to_id_converter(text, word2idx):
    """
    Converts context and questions text to their respective ids by mapping each word
    using word2idx. Input text is tokenized using spacy tokenizer first.

    :param str text: context or question text to be converted
    :param dict word2idx: word to id mapping
    :returns list text_ids: list of mapped ids

    :raises assertion error: sanity check

    """

    text_tokens = [w.text for w in nlp(text, disable=['parser', 'tagger', 'ner', 'lemmatizer'])]
    text_ids = [word2idx[word] for word in text_tokens]

    assert len(text_ids) == len(text_tokens)
    return text_ids


def get_error_indices(df, idx2word):
    """
    Finds and returns the indices with tokenization errors.
    :param df: dataframe w/ training or testing data
    :param idx2word: mapping of ids to words
    :return:
        err_idx: indices with tokenization errors
    """

    start_value_error = []
    end_value_error = []
    assert_error = []
    # Iterate over DataFrame rows
    for index, row in df.iterrows():

        answer_tokens = [w.text for w in nlp(row['answer'], disable=['parser', 'tagger', 'ner', 'lemmatizer'])]

        context_span = [(word.idx, word.idx + len(word.text))
                        for word in nlp(row['context'], disable=['parser', 'tagger', 'ner', 'lemmatizer'])]

        starts, ends = zip(*context_span)

        answer_start, answer_end = row['label']

        try:
            start_idx = starts.index(answer_start)
        except:
            start_value_error.append(index)
        try:
            end_idx = ends.index(answer_end)
        except:
            end_value_error.append(index)

        try:
            assert idx2word[row['context_ids'][start_idx]] == answer_tokens[0]
            assert idx2word[row['context_ids'][end_idx]] == answer_tokens[-1]
        except:
            assert_error.append(index)
    err_idx = set(start_value_error + end_value_error + assert_error)
    print(f"Number of error indices: {len(err_idx)}")
    return err_idx


def index_answer(row, idx2word):
    """

    :param row: row of the dataframe or one training example
    :param idx2word:
    :return: tuple of start and end positions of answer by calculating
    spans.
    """

    context_span = [(word.idx, word.idx + len(word.text)) for word in
                    nlp(row.context, disable=['parser', 'tagger', 'ner', 'lemmatizer'])]
    starts, ends = zip(*context_span)

    answer_start, answer_end = row.label
    start_idx = starts.index(answer_start)

    end_idx = ends.index(answer_end)

    ans_toks = [w.text for w in nlp(row.answer, disable=['parser', 'tagger', 'ner', 'lemmatizer'])]

    assert idx2word[row.context_ids[start_idx]] == ans_toks[0]
    assert idx2word[row.context_ids[end_idx]] == ans_toks[-1]

    return [start_idx, end_idx]
