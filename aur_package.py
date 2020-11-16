class AUR_Package:
    name = ''
    link = ''
    desc = ''

    def __init__(self, name, link, desc):
        self.name = name
        self.link = link
        self.desc = desc

    def __str__(self):
        return f'{self.name} <{self.link}>\n\t{self.desc}'

if __name__ == '__main__':
    pass
