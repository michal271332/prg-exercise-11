from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, number):
        ret = []
        for i, val in enumerate(self.scores):
            if val == number:
                ret.append(i)
        return ret

    def get_sorted(self):
        scores = self.scores.copy()
        for i in range(len(scores)):
            for j in range(0, len(scores) - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores

def main():
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    results = StudentsGrades(random_numbers(30, 0, 100))
    print(f"Test napsalo: {results.count()}")
    for idx in range(len(results.scores)):
        print(f"Student {idx}: {results.get_by_index(idx)} points - {results.get_grade(idx)}")
    print(f"Plny pocet bodu: {results.find(100)}")
    print(results.get_sorted())


if __name__ == "__main__":
    main()


