

This contains the data for "daily dialog" and "self dialog" training data
We only care about self dialog data.

# Add submodule with self dialog data
git submodule add https://github.com/jfainberg/self_dialogue_corpus


# python3 format_selfdialog.py 
Reads data/selfdialog/dialogues/*.txt and exports:
- sd-gpt2-input.csv: all training data without explicit topics
- sd-gpt-input-with-topic.csv: all training data with explicit topics

You can use these files to retrain the gpt-2 model using https://github.com/minimaxir/gpt-2-simple

