#-*- coding:utf-8
import traceback

INPUT_PATH = "../../../output/co_occurence_matrix/co_occurence_matrix.dat"
OUTPUT_PATH = "../../../output/co-word-network/edge_list.csv"

def get_edge_list( input_path, output_path ):
    try:

        infile = open(input_path,"r")
        mat = []
        for line in infile:
            line = line.rstrip('\n').split(' ')
            mat.append(line)
        infile.close()

        outfile = open(output_path,"w")
        for u, row in enumerate(mat):
            for v, w in enumerate(row):
                if v <= u: continue
                if w < '1': continue
                line = str(u)+','+str(v)+','+str(w)
                #print line
                outfile.write(line+'\n')
        outfile.close()
    except Exception,e:
        print traceback.print_exc()

if __name__ == '__main__':
    get_edge_list(INPUT_PATH, OUTPUT_PATH)