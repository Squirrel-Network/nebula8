#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
# Credits to: https://github.com/stefano-mecocci
from re import compile
from functools import reduce
"""
######################
##  EXAMPLE TO USE  ##
######################
from ArgumentProcesser import ArgumentProcesser

def handler_fn(update, context, args):
    print(args)

def main():
	# fake vars for testing
	command = '/hello @pippo false'
	update = 1
	context = 2

	# list of options
	options = [
		("", [], handler_fn),
		("user bool", [], handler_fn),
		("int", [], handler_fn)
	]

	# effective code call
	ap = ArgumentProcesser(command, update, context)
	valid_command = ap.try_matches_execute(options)

	if not valid_command:
		print("Invalid command!")

main()

"""
class ArgumentProcesser():
    def __init__(self, command, update=None, context=None):
        self.command = command
        self.update = update
        self.context = context
        self.tokens_types = []

    def _tokenize(self, s):
        s = s.strip() + ' '
        tokens = []
        token, inside_str = '', False

        for i in range(len(s)):
            c = s[i]

            if c == '"':
                inside_str = not inside_str
                token += c
            elif c == ' ':
                if inside_str:
                    token += c
                else:
                    tokens.append(token)
                    token = ''
            else:
                token += c

        return tokens

    def _find_type(self, token):
        result = ""

        if len(token) >= 2 and token[0] == '"' and token[-1] == '"':
            result = "str"
        elif token in ["true", "on"] or token in ["false", "off"]:
            result = "bool"
        elif compile("^[a-z]+$").match(token) != None:
            result = "subcmd"
        elif compile("^[0-9]+$").match(token) != None:
            result = "int"
        elif len(token) >= 4 and compile("^[a-z0-9_]+$").match(token[1:]) != None:
            result = "user" if token[0] == '@' else result

        return result

    def _find_types(self, tokens):
        for i in range(len(tokens)):
            t = self._find_type(tokens[i])
            self.tokens_types.append(t)

    def _parse_tokens(self, tokens):
        for i in range(len(tokens)):
            token_type = self.tokens_types[i]

            if token_type == 'int':
                tokens[i] = int(tokens[i])
            elif token_type == 'str':
                tokens[i] = tokens[i][1:-1]
            elif token_type == 'bool':
                tokens[i] = tokens[i] in ['true', 'on']

        return tokens

    def _match_constraint(self, token):
        result = True
        (constraint, value) = token

        if constraint == None:
            return True

        if 'val' in constraint:
            result = value == constraint['val']

        if 'range' in constraint:
            (min, max) = constraint['range']
            result = value >= min and value <= max

        if 'regex' in constraint:
            result = compile(constraint['regex']).match(value) != None

        return result

    def _match_constraints(self, constraints, values):
        fn = lambda acc, token: acc and self._match_constraint(token)

        return reduce(fn, zip(constraints, values), True)

    def try_matches_execute(self, options):
        tokens = self._tokenize(self.command)[1:]
        result, i = False, 0

        self._find_types(tokens)

        while not result and i < len(options):
            (types, filters, fn) = options[i]
            types = types.split()

            if types == self.tokens_types:
                parsed_tokens = self._parse_tokens(tokens)

                if self._match_constraints(filters, parsed_tokens):
                    result = True
                    fn(self.update, self.context, parsed_tokens)

            i += 1

        return result