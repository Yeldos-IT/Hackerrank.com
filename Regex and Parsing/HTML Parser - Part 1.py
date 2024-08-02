from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        self.print_attrs(attrs)
        
    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        self.print_attrs(attrs)

    def print_attrs(self, attrs):
        for name , value in attrs:
            print(f'-> {name} > {value}')

parser = MyParser()
parser.feed(''.join(input() for _ in range(int(input()))))
