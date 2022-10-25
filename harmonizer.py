class harmonizer():
    def __init__(self, voices: int, key: int) -> None:
        self.voices = voices
        self.key = key

    def harmonize(self, note: int) -> list[int]:
        """Given a note, return the constituent notes of the corresponding chord"""
        pass

    def reset(self) -> None:
        pass


class majorCounterPointHarmonizer(harmonizer):
    def __init__(self, voices: int, key: int) -> None:
        super.__init__(voices, key)
        self.transitionProbs = {
            "I" : 1
        }

    def harmonize(self, note: int) -> list[int]:
        pass
