import csv

# Each row in daily dialog refers to a specific topic with a integer index. Here is the map.
topic_map = {
    1: 'ORDINARY',
    2: 'SCHOOL',
    3: 'CULTURE/EDUCATION',
    4: 'ATTITUDE/EMOTION',
    5: 'RELATIONSHIP',
    6: 'TOURISM',
    7: 'HEALTH',
    8: 'WORK',
    9: 'POLITICS',
    10: 'FINANCE'
}




def transform_daily_dialog():
    """
    Read daily dialog text
    Make any format changes
    Add any prefix info
    Write out one utterance per line
    :return:
    """
    dialog_name = './data/dailydialog/dialogues_text.txt'
    topics_name = './data/dailydialog/dialogues_topic.txt'
    out_name = './data/dailydialog/dd-gpt2-input.csv'
    input = open(dialog_name, 'r')

    # Load dialog
    data = input.read()
    data = data.replace("’", "'").replace("‘", "'").replace(" ' ", "'").replace("\\", "").replace(" , ", ", ")
    lines = data.split('\n')

    # Load topics
    input = open(topics_name, 'r')
    data = input.read()
    line_topics = ['__'+topic_map[int(t) if t else 1]+'__' for t in data.split('\n')]

    outlines = []
    for i, line in enumerate(lines):
        # TODO: Evaluate sending in topic by uncommenting next row
        # newlines = [line_topics[i] + ' ' + l for l in line.split('__eou__') if l]
        newlines = [[l.strip()] for l in line.split('__eou__') if l]
        outlines.extend(newlines)

    print()

    out_file = open(out_name, 'w', newline='\n')
    writer = csv.writer(out_file)
    writer.writerows(outlines)

    # Done