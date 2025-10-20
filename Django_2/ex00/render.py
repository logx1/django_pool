import sys
import settings
import re
def load_template(file_name):
    try:
        with open(file_name, "r") as fd:
            return fd.read()
    except IOError:
        print("Error opening ", file_name)
        return None

def write_in_file(file_name, data):
    try:
        with open(file_name, 'w') as fd:
            fd.write(data)
    except IOError:
        print("Error writing %s" % file_name)

def create(file_name):
    template_content = load_template(file_name)
    if template_content:
        varibles = vars(settings)
        try:
            filled_template = template_content.format(**varibles)
            output_file_name = re.sub(r'\.template$', '.html', file_name)
            write_in_file(output_file_name, filled_template)
        except KeyError as e:
            print(f"Missing variable in settings: {e} or incorrect placeholder in template.")



if __name__ == '__main__':
    if len(sys.argv) == 2:
        if re.search('\.template$', sys.argv[1]) is not None:
            create(sys.argv[1])
        else:
            print("in argument must be a .template file")

