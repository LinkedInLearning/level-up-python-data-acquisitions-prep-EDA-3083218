import pandas as pd

painful_strings = {'painful_strings':
                   ['usePython', 'pandasForLife', 'Python is helpful']}

long_strings = pd.DataFrame(data=painful_strings)

long_strings['painful_strings'].str.replace(
    pat='([a-z])([A-Z])',
    repl='\\1 \\2')
