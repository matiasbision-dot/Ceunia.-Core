class Memory:
    def __init__(self):
        self.log = []

    def store(self, inp, out, scores, weights):
        self.log.append({
            "input": inp,
            "output": out,
            "scores": list(scores),
            "weights": list(weights)
        })
