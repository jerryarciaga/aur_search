class AUR_Package:
    name = ''
    clone_url = ''
    link = ''
    desc = ''

    def __init__(self, name, ver, link, desc):
        self.name = name
        self.clone_url = "https://aur.archlinux.org/" + self.name + ".git"
        self.ver  = ver
        self.link = link
        self.desc = desc

    def __str__(self):
        return f'''aur/{self.name} {self.ver} <{self.link}>
        Clone URL: {self.clone_url}
        {self.desc}'''

if __name__ == '__main__':
    pass
