import os

from lxml.etree import XMLParser, parse

NSS = {
    'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
    'cc': 'http://creativecommons.org/ns#',
    'ccOLD': 'http://web.resource.org/cc/',
    'svg': 'http://www.w3.org/2000/svg',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
    'xlink': 'http://www.w3.org/1999/xlink',
    'xml': 'http://www.w3.org/XML/1998/namespace',
    're': 'http://exslt.org/regular-expressions'
}

class SVGParser(object):
    def __init__(self, inputfile):
        if not os.path.isfile(inputfile):
            raise FileNotFoundError
        # parse svg input file
        try:
            _p = XMLParser(huge_tree=True)
            self.document = parse(inputfile, parser=_p)
        except Exception as e:
            print(e.with_traceback())

    def get_objects_by_id(self, pattern):
        pattern_to_compile = f"//*[re:match(@id,'({pattern})','g')]"
        object_list = self.document.xpath(pattern_to_compile, namespaces=NSS)
        results = [ item.get('id') for item in object_list ]
        return results
