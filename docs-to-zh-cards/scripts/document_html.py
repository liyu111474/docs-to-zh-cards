"""Read safe document fragments without changing code, links, or their order."""
from html import escape
from html.parser import HTMLParser
import re
from urllib.parse import urlparse

TAGS = set('a article aside b blockquote br caption code col colgroup dd details div dl dt em figcaption figure h1 h2 h3 h4 h5 h6 hr i img kbd label li ol p pre s samp section small source span strong sub summary sup table tbody td tfoot th thead time tr tt u ul var video wbr'.split())
VOID = {'br','col','hr','img','source','wbr'}
ATTRS = set('alt class colspan controls height href id name open poster rowspan src start title type width'.split())


class Fragment(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = ['', {}, []]
        self.stack = [self.root]
        self.feed(html)
        self.close()
        if len(self.stack) != 1:
            raise ValueError('Unclosed document HTML tag')

    def handle_starttag(self, tag, attrs):
        if tag not in TAGS:
            raise ValueError('Unsupported document tag: ' + tag)
        attributes = {}
        for name, value in attrs:
            if name not in ATTRS:
                raise ValueError('Unsupported document attribute: ' + name)
            if name in {'href','src','poster'} and value:
                parsed = urlparse(value)
                if parsed.scheme not in {'','http','https','mailto'} or re.search(r'[\x00-\x20\\]', value):
                    raise ValueError('Unsafe document URL')
            attributes[name] = value
        node = [tag, attributes, []]
        self.stack[-1][2].append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if len(self.stack) < 2 or self.stack[-1][0] != tag:
            raise ValueError('Mismatched document HTML tag: ' + tag)
        self.stack.pop()

    def handle_data(self, data):
        self.stack[-1][2].append(data)


def plain(node):
    return node if isinstance(node,str) else ''.join(plain(child) for child in node[2])


def elements(node):
    if not isinstance(node,str):
        yield node
        for child in node[2]:
            yield from elements(child)


def verify_translation(source_html, translated_html):
    source = list(elements(Fragment(source_html).root))
    translated = list(elements(Fragment(translated_html).root))
    def structure(node):
        return (node[0], {k:v for k,v in node[1].items() if k not in {'alt','title'}},
                [structure(child) for child in node[2] if not isinstance(child,str)])
    if structure(source[0]) != structure(translated[0]):
        raise ValueError('Translation changed the document structure, links, or media')
    for original, result in zip(source,translated):
        protected = original[0] in {'pre','code','kbd','samp','tt'} or 'signature' in original[1].get('class','').lower()
        if protected and plain(original) != plain(result):
            raise ValueError('Official code and signatures must remain unchanged')
        if plain(original).strip() and not plain(result).strip():
            raise ValueError('Translation omitted document text')


def html(node, resolve_url=lambda value,kind:value, block_id=None):
    if isinstance(node,str):
        return escape(node,quote=False)
    tag, attributes, children = node
    inner = ''.join(html(child,resolve_url) for child in children)
    if not tag:
        if block_id:
            first = next((n for n in children if not isinstance(n,str)),None)
            if first is not None:
                first[1]['data-block-id'] = block_id
            inner = ''.join(html(child,resolve_url) for child in children)
        return inner
    attrs = []
    for key,value in attributes.items():
        if key in {'href','src','poster'} and value:
            value = resolve_url(value,key)
        attrs.append(key if value is None else key + '="' + escape(value) + '"')
    opening = '<'+tag+(' '+' '.join(attrs) if attrs else '')+'>'
    return opening if tag in VOID else opening+inner+'</'+tag+'>'


def md_text(value):
    return re.sub(r'([\\`*_[\]#|])',r'\\\1',escape(value,quote=False))


def code_fence(code, language=''):
    marker = '`' * (max([2]+[len(s) for s in re.findall(r'`+',code)])+1)
    return '\n\n'+marker+language+'\n'+code+'\n'+marker+'\n\n'


def markdown(node):
    if isinstance(node,str):
        return md_text(node)
    tag,attrs,children = node
    inner = ''.join(markdown(child) for child in children)
    if tag == 'pre':
        language = next((c[1].get('class','').removeprefix('language-') for c in children if not isinstance(c,str) and c[0]=='code' and 'language-' in c[1].get('class','')), '')
        return code_fence(plain(node),language)
    if tag in {'code','kbd','samp'}:
        marker = '`' * (max([0]+[len(s) for s in re.findall(r'`+',plain(node))])+1)
        return marker+plain(node)+marker
    if tag in {'h1','h2','h3','h4','h5','h6'}:
        return '\n\n'+'#'*int(tag[1])+' '+inner.strip()+'\n\n'
    if tag in {'strong','b'}: return '**'+inner+'**'
    if tag in {'em','i'}: return '*'+inner+'*'
    if tag == 'a' and attrs.get('href') and inner.strip(): return '['+inner+'](<'+attrs['href']+'>)'
    if tag == 'img': return '!['+md_text(attrs.get('alt',''))+'](<'+attrs.get('src','')+'>)'
    if tag == 'br': return '<br>\n'
    if tag == 'hr': return '\n\n---\n\n'
    if tag in {'ul','ol'}:
        items = [c for c in children if not isinstance(c,str) and c[0]=='li']
        return '\n\n'+'\n'.join((str(i)+'. ' if tag=='ol' else '- ')+markdown(c).strip().replace('\n','\n  ') for i,c in enumerate(items,int(attrs.get('start','1'))))+'\n\n'
    if tag == 'table':
        rows = [[markdown(c).strip().replace('\n','<br>') for c in row[2] if not isinstance(c,str) and c[0] in {'th','td'}] for row in elements(node) if row[0]=='tr']
        rows = [row for row in rows if row]
        if not rows: return inner
        width = max(map(len,rows))
        rows = [row+['']*(width-len(row)) for row in rows]
        lines = ['| '+' | '.join(row)+' |' for row in rows]
        lines.insert(1,'| '+' | '.join(['---']*width)+' |')
        return '\n\n'+'\n'.join(lines)+'\n\n'
    if tag in {'p','section','article','div','aside','figure','blockquote','dl','details'}:
        return '\n\n'+inner.strip()+'\n\n'
    if tag in {'dt','dd','summary','figcaption'}: return '\n'+inner+'\n'
    return inner
