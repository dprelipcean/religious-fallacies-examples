
def compare_names(str1, str2):
    """Compare two strings alphabetically."""
    if str1 == str2:
        return "identical"
    elif not str1 or not str2:
        return False
    else:
        for index in range(min(len(str1), len(str2))):
            if str1[index] == str2[index]:
                continue
            elif str1[index] < str2[index]:
                return "overpassed"
            else:
                return "searching"


def convert_to_number(str_float):
    """Converts a number retrieved as str from the csv file to float.

    Also does curation of inputs.
    """
    if not str_float:
        return False
    elif str_float[-1] is "%":
        return float(str_float[:-1])
    elif str_float[-1] is "+":
        return float(str_float[:-2])
    else:
        return float(str_float)

def extract_name_from_file(filename):
    """Extract a name from the filename."""
    return filename[8:-4]
