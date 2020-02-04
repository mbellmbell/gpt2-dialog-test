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
    dialog_name = './data/dailydialog/dialogues_text.txt'
    topics_name = './data/dailydialog/dialogues_topic.txt'
    out_name = './data/dailydialog/dd-gpt2-input.csv'
    out_name_with_topic = './data/dailydialog/dd-gpt2-input-with-topic.csv'

    # Load dialog
    data = open(dialog_name, 'r').read()
    data = data.replace("’", "'").replace("‘", "'").replace(" ' ", "'").replace("\\", "").replace(" , ", ", ")
    lines = data.split('\n')

    # Load topics
    data = open(topics_name, 'r').read()
    line_topics = ['__'+topic_map[int(t) if t else 1]+'__' for t in data.split('\n')]

    # Format output data
    outlines, outlines_with_topic = [], []
    for i, line in enumerate(lines):
        newlines = [[l.strip()] for l in line.split('__eou__') if l]
        newlines_with_topic = [[line_topics[i] + ' ' + l] for l in line.split('__eou__') if l]
        outlines.extend(newlines)
        outlines_with_topic.extend(newlines_with_topic)

    # Output single column CSV
    out_file = open(out_name, 'w', newline='\n')
    writer = csv.writer(out_file)
    writer.writerows(outlines)

    out_file = open(out_name_with_topic, 'w', newline='\n')
    writer = csv.writer(out_file)
    writer.writerows(outlines_with_topic)

if __name__ == '__main__':
    transform_daily_dialog()
