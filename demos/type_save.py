from json import load, dump
from typejson.typing import TypeJsonTyper

def main():
    '''
    
    '''

    typer = TypeJsonTyper()
    with open('assets/1.json', 'r', encoding='utf8') as r:
        v = load(r)
        t = typer.type(v)
        with open('temps/1.t.json', 'w', encoding='utf8') as w:
            dump(t, w, ensure_ascii=False, indent=2)

if '__main__' == __name__:
    main()