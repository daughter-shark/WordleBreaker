from english_words import english_words_lower_alpha_set
import re


class WordleBreaker:
    def __init__(self):
        self.exists = dict()
        self.usable = "abcdefghijklmnopqrstuvwxyz"
        self.regex = [self.usable] * 5

    def add_guess(self, word: str, result: str):
        word = word.lower()
        result = result.lower()
        mapped = list(zip(list(word), list(result)))
        idx = 0
        for k, v in mapped:
            if v == "x":
                if k in self.usable:
                    self.regex = [i.replace(k, "") if len(i) > 1 else i for i in self.regex]
                    self.usable = self.usable.replace(k, "")
            elif v == "e":
                if not self.exists.get(k):
                    self.exists[k] = {idx}
                else:
                    self.exists[k].add(idx)
            elif v == "c":
                self.regex[idx] = k
            idx += 1
        for k, v in self.exists.items():
            for i in v:
                if len(self.regex[i]) > 1:
                    self.regex[i] = self.regex[i].replace(k, "")
        re_compile = re.compile(f'^{"".join([f"[{i}]" for i in self.regex])}$')
        ret_list = list(filter(re_compile.match, english_words_lower_alpha_set))
        for i in self.exists.keys():
            ret_list = list(filter(re.compile(r"^.*Q{1,}.*$".replace("Q", i)).match, ret_list))
        return ret_list
