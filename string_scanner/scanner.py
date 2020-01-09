import re
from sys import exit
from string_scanner.scanner_string_segment import ScannedStringSegment
from regex_tokens.enum_tokens import TokenName


class Scanner(object):

    def __init__(self, regex_rules: list, text_to_match: list):
        self.rules = regex_rules
        self.text_to_match = text_to_match
        self.list_tokens = []  # list of ScannedStringSegment objects
        self.scan()

    def scan(self):
        """Function traverses the text to match."""
        try:
            assert self.text_to_match
        except AssertionError:
            print('Please introduce an operation to calculate.')
            exit(1)

        for line in self.text_to_match:  # taking each line from the code to match
            i = 0
            while i < len(line):  # looping till the end of the string is reached
                string_segment = self.try_match(i, line)

                try:
                    assert string_segment.token
                    i += string_segment.end_string  # set the new index to take the unmatched string
                    self.list_tokens.append(string_segment)  # append the found goods
                except AssertionError:
                    print(f'SyntaxError: Unmatched Syntax -{line[i]}-  at line:  '
                          f'\n{line}')
                    exit(1)

    def try_match(self, i: int, line: str) -> ScannedStringSegment:
        """Given a a string to match and its index where to start from, the function matches the string element
         with a token and removes it."""
        start = line[i:]  # take the unmatched string
        for regex, token in self.rules:
            compiled_regex = re.compile(regex)  # compile regex
            match = compiled_regex.match(start)  # verify to see if the string matches the regex
            if match:  # if a match is found
                begin, end = match.span()  # take the begin and end index
                return ScannedStringSegment(token, i, start[:end], end)
        return ScannedStringSegment(None, None, start, None)  # if a match if not found

    def match(self, token_id: str) -> ScannedStringSegment:
        """Given a possible token, the function removes and returns the first token that is matched."""
        while token_id == TokenName.space.value:  # lexical analyser eliminates extra spaces
            self.ignore_ws()

        if token_id != TokenName.space.value:  # lexical analyser eliminates one spaces
            self.ignore_ws()

        if self.list_tokens[0].token == token_id:  # if a match is made
            removed = self.list_tokens.pop(0)  # pop element
            return removed

    def peek(self) -> ScannedStringSegment:
        """The function returns the first token in the list."""
        if not self.done():
            self.ignore_ws()
            return self.list_tokens[0]

    def ignore_ws(self):
        """Functions pops the SPACE token. The lexical analyser must remove all spaces."""
        while self.list_tokens[0].token == TokenName.space.value:
            self.list_tokens.pop(0)

    def parse_extra_space(self):
        """Function removes extra multiple spaces until there are no more elements to match."""
        while not self.done():
            if self.list_tokens[0].token == TokenName.space.value:
                self.list_tokens.pop(0)
            else:
                return

    def skip(self, *what: str or tuple) -> bool:
        """Function evaluates if the given element equals the first element
        in the list of tokens. If YES, it returns TRUE, if NOT, it pops the first element and
        tries again, and returns False if also first new element does not match."""
        for x in what:
            if x != TokenName.space.value:
                self.ignore_ws()

            tok = self.list_tokens[0]
            if tok.token != x:
                return False
            else:
                self.list_tokens.pop(0)
                return True

    def push(self, rule_token: list):
        """Pushes a token back on the token stream so that a later peek or match will return it."""
        for i in range(0, len(self.list_tokens)):
            if rule_token[1] == self.list_tokens[i].token:
                continue
            else:
                self.rules.append(rule_token)

    def done(self) -> bool:
        return len(self.list_tokens) == 0
