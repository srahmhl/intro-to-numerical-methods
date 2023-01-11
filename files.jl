using DelimitedFiles

WDataFile=open("W.out","r")
W=readdlm(WDataFile,'\t',Float64,'\n')
close(WDataFile)

pDataFile=open("p.out","r")
p=readdlm(pDataFile,'\t',Float64,'\n')
close(pDataFile)

using LinearAlgebra
L,U,P = lu(W)
print(lu(W))