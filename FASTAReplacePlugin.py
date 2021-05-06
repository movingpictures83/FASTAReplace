
class FASTAReplacePlugin:
    def input(self, filename):
       self.fasta = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        newfasta = open(filename, 'w')

        pos = 0
        for line in self.fasta:
            if (pos % 2 == 0):
                contents = line.strip().split('\t')
                otuname1 = contents[0][1:]
                otuname2 = contents[1][0:contents[1].index('|')]
                newfasta.write(">"+otuname2+"\n")
            else:
                newfasta.write(line)
            pos += 1

