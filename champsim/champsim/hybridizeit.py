from pathlib import Path
path_of_champsim = str(Path(__file__).parents[2])
def hybridizing_two(pred1, pred2):
    pred11 = pred1
    pred22 = pred2
    pred1 = pred1+"first"
    pred2 = pred2+"first"
    file1 = open(path_of_champsim+"/ChampSim-master/branch/{}".format(pred11+".bpred"),"r")
    code_of_1 = file1.readlines()
    donehere = 0
    whole_code = []
    p = 0
    for i in code_of_1:
        p+=1
        if(p==2):
            whole_code.append("uint8_t {},{};".format(pred1,pred2))
        if(i.find("O3_CPU::")!=-1):
            i=i.replace("O3_CPU::",pred1+"_")
            print(i)
            whole_code.append(i)
            donehere = 1
        else:
            whole_code.append(i)
        if(donehere == 1 and i.find("{")!=-1):
            whole_code.append("    int cpu = 0;\n")
            donehere=0
    file2 = open(path_of_champsim+"/ChampSim-master/branch/{}".format(pred22+".bpred"),"r")
    code_of_2 = file2.readlines()
    donehere = 0
    for i in code_of_2:
        if(i.find('#include "ooo_cpu.h"')==-1):
            if(i.find("O3_CPU::")!=-1):
                i=i.replace("O3_CPU::",pred2+"_")
                print(i)
                whole_code.append(i)
                donehere = 1
            else:
                whole_code.append(i)
            if(donehere == 1 and i.find("{")!=-1):
                whole_code.append("    int cpu = 0;\n")
                donehere=0

    file = open(path_of_champsim+"/champsim/champsim/hybrid","r")
    code_lines = file.readlines()
    for i in code_lines:
        if(i.find("{0}")!=-1):
            i=i.replace("{0}",pred1)
        if(i.find("{1}")!=-1):
            i=i.replace("{1}",pred2)
        whole_code.append(i)
    codefile="".join(whole_code)
    file = open(path_of_champsim+"/ChampSim-master/branch/"+"hybrid_{}_{}.bpred".format(pred1[:-5],pred2[:-5]),"w")
    file.write(codefile)
    return 1
