import xml.etree.ElementTree as ET


class Session:
    def __init__(self, base):
        self.reverts = []
        self.base = base

    def add_revert(self, rev: str):
        self.reverts.append(str(rev))

    def revert_exec(self):
        return 'self.{}'.format(self.reverts.pop())

    def revert(self, count: int = 1):
        for i in range(-1, count - 1, -1):
            exec('{}.{}'.format(self.base.execname, self.reverts[i]))

    def revert_all(self):
        for rev in self.reverts:
            exec('{}.{}'.format(self.base.execname, rev))

    def commit(self, close_this_file: bool = False, del_session: bool = False):
        self.base.write()
        if close_this_file:
            self.base.close()
        if del_session:
            del self
            return
        self.reverts = []


class XML:
    def __init__(self, path, encode='utf-8', use_session=False, varname='1'):
        if type(path) != str or type(encode) != str or type(varname) != str:
            del self
            return
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        self.encoding = encode
        self.execname = varname
        if use_session:
            self.session = Session(self)

    def get_tag(self, tag):
        if str(tag) == 'root' or tag == self.root:
            return self.root.tag
        else:
            to_return = ''
            exec('to_return = self.root.{}.tag'.format(str(tag)))
            return to_return

    def get_attr(self, tag):
        if str(tag) == 'root' or tag == self.root:
            return self.root.attrib
        else:
            to_return = ''
            exec('to_return = self.root.{}.attrib'.format(str(tag)))
            return to_return

    def get_children(self, tag, tags=True, attribs=True):
        children = []
        if str(tag) == 'root' or tag == self.root:
            for child in self.root:
                if tags and attribs:
                    children.append((child.tag, child.attrib))
                elif tags:
                    children.append(child.tag)
                else:
                    children.append(child.attrib)
        return tuple(children)

    def all_elements(self, tags=True, attribs=True):
        if tags and attribs:
            return tuple((elem.tag, elem.attrib) for elem in self.root.iter())
        elif tags:
            return tuple(elem.tag for elem in self.root.iter())
        else:
            return tuple(elem.attrib for elem in self.root.iter())

    def revert(self, count=1):
        if self.execname == '1':
            for i in range(0, 1):
                exec(self.session.revert_exec())
        else:
            try:
                int(self.execname)
                for i in range(0, 1):
                    exec(self.session.revert_exec())
            except ValueError:
                
                self.session.revert(count)


if __name__ == '__main__':
    xml = XML('this.xml')
    print(xml.get_tag(xml.root))
    print(xml.get_attr(xml.root))
    print(xml.get_children('root'))
    print(xml.all_elements(attribs=False))
