class Elem:
    class ValidationError(Exception):
        pass

    def __init__(self, tag, attr=None, content=None, tag_type='double'):
        if tag_type not in ('double', 'simple'):
            raise Elem.ValidationError("Invalid tag type")
        self.tag = tag
        self.attr = attr if attr else {}
        self.content = []
        if content:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        attr_str = ''.join(f' {key}="{value}"' for key, value in self.attr.items())
        if self.tag_type == 'simple':
            return f"<{self.tag}{attr_str} />"
        content_str = ''.join(str(c) for c in self.content)
        return f"<{self.tag}{attr_str}>{content_str}</{self.tag}>"

    def add_content(self, content):
        if not isinstance(content, (str, Elem, list)):
            raise Elem.ValidationError("Invalid content type")
        if isinstance(content, list):
            for item in content:
                self.add_content(item)
        else:
            self.content.append(content)

if __name__ == "__main__":
    html = Elem('html', content=[
        Elem('head', content=[
            Elem('title', content="Hello ground!")
        ]),
        Elem('body', content=[
            Elem('h1', content="Oh no, not again!"),
            Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)