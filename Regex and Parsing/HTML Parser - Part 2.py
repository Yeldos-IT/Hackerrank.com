from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(f'>>> Multi-line Comment\n{data}')
        else:
            print(f'>>> Single-line Comment\n{data}')
            
    def handle_data(self, data):
        data = data.replace('\n', "")
        if len(data) > 0:
            print(f'>>> Data\n{data}')
           

parser = MyParser()
parser.feed(''.join(input()+'\n' for _ in range(int(input()))))
