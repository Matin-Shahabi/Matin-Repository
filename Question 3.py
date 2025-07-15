raw_scores = [
    "Ali=Math:17,Physics:18.5,Chemistry:15",
    "Sara=Math:20,Physics:19,Chemistry:19.5",
    "Reza=Math:16,Physics:14.5,Chemistry:13",
    "Zahra=Math:18.5,Physics:20,Chemistry:20"
]

def scores_students(lst):
    scores = list(map(lambda row: {s.split(":")[0]: float(s.split(":")[1]) for s in row.split("=")[1].split(",")},lst))
    subject= scores[0].keys()
    averages = {
        sub: sum(map(lambda d: d[sub], scores)) / len(scores)for sub in subject
    }
    new_averages = {i: round(j, 2) for i,j in averages.items()}
    return new_averages



print(scores_students(raw_scores))

