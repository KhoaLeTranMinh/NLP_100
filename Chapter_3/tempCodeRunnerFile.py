pattern_contents = re.compile(
    r' ^\{\{Infobox\scountry .*?$ (.*?) ^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)  # re.DOTALL forces . to represent any character, 