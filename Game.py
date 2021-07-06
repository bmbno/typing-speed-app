import time
import random
from math import floor


class Game:

    def choose_sentence(self):
        with open('sentences.txt', 'r', encoding='utf-8') as file:
            sentences = file.read().split('\n')
        return sentences[random.randrange(len(sentences))-1]

    def calculate_score(self, start_time, end_time, sentence, attempt):
        character_count = len(attempt)
        total_time = (end_time - start_time) / 60
        differences = 0
        longer_sentence = max(len(sentence), len(attempt))
        for i in range(longer_sentence):
            try:
                if sentence[i] != attempt[i]:
                    differences += 1
            except IndexError:
                differences += 1
        accuracy = (1 - (differences / len(sentence))) * 100
        net_wpm = abs((character_count / 5) - differences) / total_time
        return accuracy, net_wpm

    def calculate_time(self, start_time, end_time):
        time_seconds = end_time - start_time
        minutes, seconds = divmod(time_seconds, 60)
        return [int(minutes), int(seconds)]

    def run(self):
        sentence = self.choose_sentence()
        # START = 0
        # print(sentence)
        # while not START:
        #     start_key = input("Hit Enter to start: ")
        #     if start_key == "":
        #         START = 1
        start_time = time.time()
        attempt = input("type sentence:")
        end_time = time.time()
        accuracy, wpm = self.calculate_score(
            start_time, end_time, sentence, attempt)
        total_time = self.calculate_time(start_time, end_time)
        return total_time, accuracy, wpm


def main():
    game = Game()
    PLAY = True
    while PLAY:
        total_time, accuracy, wpm = game.run()
        print(f"""
            Your score is:
            Time: {total_time[0]} minutes {total_time[1]} seconds
            Accuracy: {accuracy:.1f}%
            WPM: {wpm:.2f}
            """)
        x = input("Do you want to play again, Y or N?:  ")
        if x.lower() == "n":
            PLAY = False


if __name__ == '__main__':
    main()
