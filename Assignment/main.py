""" asd """
import re

def get_words_from_file(filename):
    """ asd """
    file = open(filename)
    script = file.readlines()
    start_index = start_of_script(script)
    script = script[start_index:-1]
    end_index = end_of_script(script)
    script = script[0:end_index]
    new_script = filter_script(script)
    return(new_script)

def start_of_script(script):
    """ index of start of script """
    for i in range(len(script)):
        if "*** START OF" in script[i]:
            if list(script[i].split(" "))[0] == "***":
                start_index = i+1
                break
    return start_index

def end_of_script(script):
    """ Index of end of script """
    for i in range(len(script)):
        if "*** END" in script[i]:
            if list(script[i].split(" "))[0] == "***":
                end_index = i
                break
    return end_index


def filter_script(script):
    """ Filter script """
    new_script = []
    for line in script:
        words_on_line = re.findall("[a-z]+[-'][a-z]+|[a-z]+[']?|[a-z]+", line.lower())
        if words_on_line != "":
            for word in words_on_line:
                new_script.append(word)
    return new_script

def average_word_length(words):
    """ Get average word length """
    count = 0
    for word in words:
        count += len(word)
    average = count/len(words)
    return average

def max_length_word(words):
    """ Find longest word """
    longest_word = max(words, key=len)
    return len(longest_word)

def most_frequent(words):
    """ find most frequent word """
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    most_frequent_word = max(word_count, key=word_count.get)
    most_frequent_word = word_count[most_frequent_word]
    return most_frequent_word

def length_frequency(words):
    """ find the frequency of different word lengths """
    word_lengths = {}
    longest_word = max(words, key=len)
    for i in range(len(longest_word)-1):
        word_lengths[i+1] = 0
    for word in words:
        if len(word) not in word_lengths:
            word_lengths[len(word)] = 1
        else:
            word_lengths[len(word)] += 1

    return word_lengths

def print_graph(word_length, sorted_keys, frequency, list_words):
    """ print the graph of frequencies """
    print("\n% frequency")
    word_length_percentages = convert_percentage(word_length, list_words, sorted_keys)
    frequency = max(word_length_percentages, key=word_length_percentages.get)
    frequency = (int(word_length_percentages[frequency]/10) + 1) * 10

    for i in range(frequency):
        words_with_frequency = []
        for j in range(len(word_length_percentages)):
            if word_length_percentages[sorted_keys[j]] >= frequency - i:
                words_with_frequency.append(sorted_keys[j])
        string = ""
        default = 0
        # print(f"words with freq {words_with_frequency}{frequency - i}")



        for k in range(len(words_with_frequency)):
            # print((words_with_frequency[k] - default))
            missing_numbers = words_with_frequency[k] - default - 1
            string += "  " * (words_with_frequency[k] - default + missing_numbers) + "**"
            default = words_with_frequency[k]
        print(f" {frequency - i:>2} {string}")

    string = "    "
    for key in sorted_keys:
        if key < 10:
            string += "  " + "0" + str(key)
        else:
            string += "  " + str(key)
    align = int(4 * max(sorted_keys) + 4)-11
    print(f"{string}")
    print(f"{' '*align:<5}word length")
    # print(f"{string}"
    # f"\n{align:<0}{'word length':>0}")
    # multiplier = (int(sorted_keys[-1]) - 1)
    # number_of_spaces = "    " * multiplier + "word length"
    # print(number_of_spaces[3:])
    # print(f" {frequency - i} {string}")
    # print(sorted_keys, longest_word)

def convert_percentage(word_lengths, list_words, sorted_keys):
    """ Convert frequencies to percantages """
    word_length_precentages = {}
    for key in sorted_keys:
        relative_freq = int(word_lengths[key] / len(list_words) * 100)
        word_length_precentages[key] = int(word_lengths[key] / len(list_words) * 100)
    return(word_length_precentages)

def main():
    """ main function """
    file_name = input("Please enter filename: ")
    list_words = get_words_from_file(file_name)
    average_length = average_word_length(list_words)
    longest_word = max_length_word(list_words)
    frequency = most_frequent(list_words)
    word_lengths = length_frequency(list_words)

    print("\nWord summary (all words):")
    print(f" Number of words = {len(list_words)}")
    print(f" Average word length = {average_length:.2f}")
    print(f" Maximum word length = {longest_word}")
    print(f" Maximum frequency = {frequency}")

    sorted_keys = sorted(word_lengths)
    print("\n Len  Freq")
    for key in sorted_keys:
        print(f"{key:>4}{word_lengths[key]:>6}")

    print("\n Len  Freq Graph")
    for key in sorted_keys:
        relative_freq = int(word_lengths[key] / len(list_words) * 100)
        graph = "=" * relative_freq
        print(f"{key:>4}{relative_freq:>5}% {graph}")

    print_graph(word_lengths, sorted_keys, frequency, list_words)

main()
