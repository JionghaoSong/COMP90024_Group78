import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

# Ensure that NLTK's stopwords are available
nltk.download('stopwords')


# Load JSON data from a file with multiple JSON objects, each on a new line
def load_json_data(filepath):
    data = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data


# Extract text from the JSON data
def extract_text(data):
    text = ""
    for entry in data:
        if 'tokens' in entry:
            text += " ".join(entry['tokens']) + " "
    return text


# Generate a word cloud and print the top 30 word frequencies
def generate_word_cloud(text):
    # Define a set of stopwords to remove
    stop_words = set(stopwords.words('english'))  # Use NLTK's list of stopwords
    additional_stopwords = {
        'the', 'an', 'a', 'for', 'and', 'or', 'on', 'with', 'at', 'from', 'by', 'as',
        'way', 'need', 'would', 'back', 'say', 'also', 'right', 'still', 'see', 'think', 'really', 'even', 'going',
        'look',
        'want', 'much', 'take', 'got', 'could', 'two', 'use', 'long', 'find', 'bit',
        'made', 'thing', 'people', 'today', 'know', 'week', 'time', 'year',
        'i\'m', 'world', 'place', 'show', 'great'
    }  # Expanded list of additional stopwords
    stop_words.update(additional_stopwords)

    # Create the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stop_words)
    wordcloud.generate(text)

    # Print word frequencies
    word_frequencies = wordcloud.process_text(text)
    sorted_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:30]
    for word, freq in sorted_frequencies:
        print(f"{word}: {freq}")

    # Optionally display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    # plt.savefig('word_cloud_output.png')


# Main function to process the data
def main():
    filepath = '../elastic/data/filtered_aus_social.json'
    data = load_json_data(filepath)
    text = extract_text(data)
    generate_word_cloud(text)


if __name__ == '__main__':
    main()
