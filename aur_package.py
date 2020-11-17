class AUR_Package:
    name = ''
    link = ''
    desc = ''

    def __init__(self, name, ver, link, desc):
        self.name = name
        self.ver  = ver
        self.link = link
        self.desc = desc

    def __str__(self):
        return f'aur/{self.name} {self.ver} <{self.link}> \n\t{self.desc}'

if __name__ == '__main__':
    pass
