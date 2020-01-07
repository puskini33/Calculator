from regex_tokens.enum_tokens import TokenName


class RegexRules(object):
    list_regex_rules = [
                ((r"^[0-9]+"),                 TokenName.integer.value),
                ((r"^\+"),                     TokenName.plus.value),
                ((r"-"),                       TokenName.minus.value),
                ((r"\/"),                      TokenName.division_sign.value),
                ((r"\*"),                      TokenName.times_sign.value),
                ((r"%"),                       TokenName.modulo_sign.value),
                ((r"\s"),                      TokenName.space.value),
                ((r"\="),                      TokenName.equal.value),
                ((r"[a-z]"),                   TokenName.variable.value)]

    def add_regex_rule(self, regex: str, token: 'TokenName'):
        list_regex_rules.append(((regex), token))
