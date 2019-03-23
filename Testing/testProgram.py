import uno
import os

file = open("C:/users/ghcar/Desktop/pruebas.txt", "w")
file.write("Test Data_|_Expected Result_|_Actual Result_|_Pass/Fail" + "\n")

def TestEquivalencePartitioning():
    file.write("Equivalence Partitioning_________________________________________________" + "\n")
    if uno.ValidSemester(0) == False:
        file.write(" 0        |" + "    __False__    |   " + " __" + str(uno.ValidSemester(0))+ "__ " + " | __Pass__ " + "\n")
    else:
        file.write(" 0        |" + "     __False__   | " + " __" + str(uno.ValidSemester(0))+ "__ " + " | __Fail__ " + "\n")
    
    if uno.ValidSemester(5) == True:
        file.write(" 5        |" + "     __True__    |   " + " __" + str(uno.ValidSemester(5))+ "__ " + "  | __Pass__ " + "\n")
    else:
        file.write(" 5        |" + "    __True__     |    " + " __" + str(uno.ValidSemester(5))+ "__ " + " | __Fail__ " + "\n")
    
    if uno.ValidSemester(9) == False:
        file.write(" 9        |" + "    __False__    |   " + " __" + str(uno.ValidSemester(9))+ "__ " + " | __Pass__ " + "\n")
    else:
        file.write(" 9        |" + "     __False__   |  " + " __" + str(uno.ValidSemester(9))+ "__ " + " | __Fail__ " + "\n")
    file.write("-------------------------------------------------------------------------" + "\n")
TestEquivalencePartitioning()

def TestBoundaryValueAnalysis():
    file.write("Boundary Value Analysis__________________________________________________" + "\n")
    if uno.ValidSemester(0) == False:
        file.write(" 0        |" + "    __False__    |   " + " __" + str(uno.ValidSemester(0))+ "__ " + " | __Pass__ " + "\n")
    else:
        file.write(" 0        |" + "     __False__   | " + " __" + str(uno.ValidSemester(0))+ "__ " + " | __Fail__ " + "\n")
    
    if uno.ValidSemester(1) == True:
        file.write(" 1        |" + "     __True__    |   " + " __" + str(uno.ValidSemester(5))+ "__ " + "  | __Pass__ " + "\n")
    else:
        file.write(" 1        |" + "    __True__     |    " + " __" + str(uno.ValidSemester(5))+ "__ " + " | __Fail__ " + "\n")
    
    if uno.ValidSemester(8) == False:
        file.write(" 8        |" + "    __True__     |   " + " __" + str(uno.ValidSemester(8))+ "__ " + "   | __Pass__ " + "\n")
    else:
        file.write(" 8        |" + "     __True__    |  " + " __" + str(uno.ValidSemester(8))+ "__ " + "   | __Fail__ " + "\n")
    if uno.ValidSemester(9) == False:
        file.write(" 9        |" + "    __False__    |   " + " __" + str(uno.ValidSemester(9))+ "__ " + " | __Pass__ ")
    else:
        file.write(" 9        |" + "     __False__   |  " + " __" + str(uno.ValidSemester(9))+ "__ " + " | __Fail__ ")
TestBoundaryValueAnalysis()
file.close()