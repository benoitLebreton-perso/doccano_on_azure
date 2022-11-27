def scoring(correction, answer):
    if not answer:
        return 0
    true_positive = set(answer).intersection(correction)
    false_positive = set(answer).difference(correction)
    false_negative = set(correction).difference(answer)
    return len(true_positive)/(len(true_positive)+len(false_negative)+len(false_positive))