import tkinter, tkinter.constants, tkinter.filedialog, textwrap
from tkinter import *
from tkinter.filedialog import askopenfilenames

class MainApp:

        fileNames = []

        def __init__(self, parent):
            self.mainContainer = Frame(parent)
            self.mainContainer.pack_propagate(0)
            self.mainContainer['width'] = 600
            self.mainContainer['height'] = 500
            self.mainContainer.pack()

            self.buttonContainer = Frame(self.mainContainer)
            self.buttonContainer.pack(pady = 10)

            self.descriptionContainer = Frame(self.mainContainer)
            self.descriptionContainer.pack(pady = 10)

            self.bGetFile = Button(master = self.buttonContainer, text = "Open .dlg File(s)", command = self.getFileNames)
            self.bGetFile.pack(padx = 15)

            self.l = tkinter.Label(master = self.descriptionContainer)
            self.l['text'] = "Please upload one or more .dlg files."
            self.l.pack()

            self.output = Text(self.mainContainer)
            self.output.pack()


        def getFileNames(self):
            self.fileNames = askopenfilenames()

            if(len(self.fileNames) > 0):

                results = []

                length = len(self.fileNames)
                for index in range(length):

                    runCount = 0
                    validFile = False

                    fileName = self.fileNames[index]
                    fileNameLength = len(fileName)

                    if(fileName[-4:fileNameLength] == '.dlg'):

                        validFile = True
                        actualFile = open(fileName)
                        value = []
                        lineNumber = []
                        row = 0
                        dockerFile = []


                        lines = actualFile.readlines()
                        newTuple = True
                        for line in lines:
                            if(newTuple):
                                fileAttributes = []
                                newTuple = False

                            row +=1
                            if(line.__contains__("BEGINNING LAMARCKIAN GENETIC ALGORITHM DOCKING")):
                                fileAttributes.append(runCount + 1)
                                fileAttributes.append(row)
                                lineNumber.append(row)


                            if(line.__contains__("Final-Value:")):
                                fValue = line.split()
                                value.append(fValue[1])
                                fileAttributes.append(fValue[1])
                                runCount += 1
                                newTuple = True

                            if(newTuple):
                                dockerFile.append(tuple(fileAttributes))


                        actualFile.close()

                        value.sort(reverse = True)

                        sortme = sorted(dockerFile, key = lambda x: x[2], reverse = True)

                        bestRun = sortme[0]
                        results.append((fileName, bestRun[0], bestRun[1], bestRun[2]))

                    else:
                        l2string = "Only .dlg files are accepted."

                self.output.delete(1.0, END)
                if(validFile):
                    sortedResults = sorted(results, key = lambda x: x[3])
                    for result in sortedResults:
                        outstring = str(result[1]).zfill(2) + "\t" + str(result[3]) + "\t" + str(result[2]) +  "\t" + result[0] + "\n"
                        self.output.insert(1.0, outstring)
                    self.output.insert(1.0, "Run\tEnergy\tLine #\tFile Name\n")
                else:
                    self.output.insert(1.0, l2string)


        def fileNamesToString(self):
            fileString = ""
            length = len(self.fileNames)
            for index in range(length):
                if(index == length-1):
                    if(length-1 > 0):
                        fileString += "and "
                    fileString += self.fileNames[index]
                    fileString += " "
                else:
                    fileString += self.fileNames[index]
                    fileString += ", "
            fileString += "loaded."
            return textwrap.fill(fileString, width = 50)

        def findEnergies(self):
            print("here")



root = Tk()
root.wm_title(string="Waingeh Dockerware 1.1")
k = MainApp(root)
root.mainloop()

