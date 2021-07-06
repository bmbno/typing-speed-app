import random
from math import floor


class Game:
    """
    A class to represent game functionality
    """

    def choose_sentence(self):
        """
        Randomly chooses a sentence from a .txt file

        Returns:
            (string): a random sentence
        """
        with open('sentences.txt', 'r', encoding='utf-8') as file:
            sentences = file.read().split('\n')
        return sentences[random.randrange(len(sentences))-1]

    def calculate_score(self, start_time, end_time, sentence, attempt):
        """
        Calculates accuracy and net wpm of the attempt

        Args:
            start_time (float): the start time of the attempt
            end_time (float): the end time of the attempt
            sentence (string): the sentence to be typed
            attempt (string): the typed sentence

        Returns:
            accuracy (float): the accuracy of the attempt compared to the sentence
            net_wpm (float): the net wpm calculated from gross wpm and accuracy
        """
        character_count = len(attempt)
        total_time = (end_time - start_time) / 60
        differences = 0
        attempt_words = attempt.split(" ")
        sentence_words = sentence.split(" ")
        sentence_characters = "".join(sentence_words)
        longer_sentence = max(len(sentence_words), len(attempt_words))

        # Determines differences between each word in the sentence
        for i in range(longer_sentence):
            try:
                for j in range(len(sentence_words[i])):
                    try:
                        if sentence_words[i][j] != attempt_words[i][j]:
                            differences += 1
                    except IndexError:
                        differences += 1
            except IndexError:
                if len(attempt_words) > len(sentence_words):
                    differences += len(attempt_words[i])
                elif len(sentence_words) > len(attempt_words):
                    differences += len(sentence_words[i])

        accuracy = (1 - (differences / len(sentence_characters))) * 100
        net_wpm = abs((character_count / 5) - differences) / total_time
        return accuracy, net_wpm

    def calculate_time(self, start_time, end_time):
        """
        Calculates the total time in minutes and seconds

        Args:
            start_time (float): the start time of the attempt
            end_time (float): the end time of the attempt

        Returns:
            (list): the time represented as list [minutes, seconds]
        """
        time_seconds = end_time - start_time
        minutes, seconds = divmod(time_seconds, 60)
        return [int(minutes), int(seconds)]
