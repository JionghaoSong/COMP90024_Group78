import json


def filter_data(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = []
            for line in infile:
                try:
                    entry = json.loads(line.strip())
                    if entry['sentiment'] != 0.0:
                        data.append(entry)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON for line: {line.strip()}")
                    print(f"Error message: {e}")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for entry in data:
                outfile.write(json.dumps(entry) + "\n")

        print(f"Filtered data written to {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_file = 'mastodon_social.json'
    output_file = 'filtered_mastodon_social.json'
    filter_data(input_file, output_file)
