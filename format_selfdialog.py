import re
import glob

def transform_daily_dialog():
    dir_name = './data/selfdialog'
    out_name = './data/selfdialog/sd-gpt2-input.csv'
    out_name_with_topic = './data/selfdialog/sd-gpt2-input-with-topic.csv'

    out_file = open(out_name, 'a')
    out_file_with_topic = open(out_name_with_topic, 'a')
    files = glob.glob(dir_name+'/dialogues/*.txt')
    files.sort(key=lambda s: int(re.search(r'\d+', s).group(0)))

    for filename in files:
        data = open(filename).read()
        out_file_with_topic.write(data)

        data = re.sub('__.+__ ', '', data)
        out_file.write(data)

    out_file.close()
    out_file_with_topic.close()


if __name__ == '__main__':
    transform_daily_dialog()
