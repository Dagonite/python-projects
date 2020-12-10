########################################################################################
# closure_example.py
#
# Demonstrating how closures can be used with this html example.
########################################################################################


def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Test headline!")
print_h1("Another headline!")

print_p = html_tag("p")
print_p("Test paragraph!")