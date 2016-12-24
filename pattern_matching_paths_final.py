"""Patter_matching_paths_final is a program that, given a set of patterns and
paths, returns the best matching pattern for each path, if any.
"""
# SUBMITTED VERSION

import fileinput
from itertools import islice, izip


def process_input():
    """Processes input and returns iterables for patterns and paths"""

    user_input = (line.rstrip('\n').strip() for line in fileinput.input())

    pattern_count = user_input.next()
    patterns = [pattern for pattern in islice(user_input, int(pattern_count))]

    path_count = user_input.next()
    paths = (path.strip('/') for path in islice(user_input, int(path_count)))

    return patterns, paths


def seed_pattern_dictionary(patterns):
    """Creates nested dictionary patterndict:
    patterndict[pattern_field_count][wild_count] = list of patterns
    """

    pattern_dict = {}

    for pattern in patterns:
        pattern_field_count = pattern.count(',') + 1
        wild_count = pattern.count("*")

        inner_key = pattern_dict.setdefault(pattern_field_count, dict())
        value = inner_key.setdefault(wild_count, list())
        value.append(pattern)

    return pattern_dict


def sort_dictionary(dictionary):
    """Sort the list of values for the inner key of a nested dictionary by
    earliest occurring wild first.  This way, the first matching pattern will
    be the best matching pattern.
    """

    for key, inner_key in dictionary:
        for k, v in inner_key.iteritems():
            inner_key[k] = sorted(v, reverse=True)
    return dictionary


def all_fields_match(zipped_fields):
    """Fail-fast method returns False if a non-wild pattern field does not match
    the corresponding path field.
    """

    for path_field, pattern_field in zipped_fields:
        if pattern_field != "*":
            if path_field != pattern_field:
                return False
    return True


def get_best_match(dictionary, path_fields):
    """Searches dictionary for matching pattern, preferring patterns with least
    number of wilds.  Returns first matching pattern.
    """

    for wild_count_key, pattern_list in dictionary:
        for pattern in pattern_list:
            pattern_fields = pattern.split(',')
            # zip path and pattern fields, so we can iterate over both to
            # compare them
            if all_fields_match(izip(path_fields, pattern_fields)):
                return pattern


def search_patterns(path, pattern_dict):
    """Given a path, prints best matching pattern, else prints NO MATCH"""

    path_field_count = path.count('/') + 1
    patterns_with_same_field_count = pattern_dict.setdefault(path_field_count, None)

    if patterns_with_same_field_count:
        path_fields = path.split('/')
        best_matching_pattern = get_best_match(patterns_with_same_field_count.iteritems(), path_fields)

        print best_matching_pattern if best_matching_pattern else "NO MATCH"
    else:
        print "NO MATCH"


def run():
    patterns, paths = process_input()

    pattern_dict = seed_pattern_dictionary(patterns)
    sort_dictionary(pattern_dict.iteritems())

    for path in paths:
        search_patterns(path, pattern_dict)

run()
