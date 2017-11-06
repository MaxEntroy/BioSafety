#DATA_PATH = "/home/kang/tmp/co_occurence_matrix.dat"
DATA_PATH = "/home/kang/tmp/co_occurence_matrix_ochiai.dat"
ROW = 67
#NAMES = c("A","B","C","D","E","F")
NAMES = c("Protein Engineering","Recombinant Proteins","Genetically Modified","Escherichia coli","Genetic","Saccharomyces cerevisiae","Bacterial","Gene Expression Regulation","Genetic Engineering","Species Specificity","Signal Transduction","Escherichia coli Proteins","Molecular","Morals","Cloning","Ethanol","Glucose","Models","Cell Proliferation","Bacterial Proteins","Transfection","Metabolic Engineering","Biomedical Enhancement","Mutagenesis","Plant Proteins","Genetic Vectors","Moral Obligations","Biotechnology","Cell Culture Techniques","Up-Regulation","Computer Simulation","Mutation","Cells","Biological","Cultured","Medical","Bioreactors","Saccharomyces cerevisiae Proteins","Bioethical Issues","Genome","Eugenics","Promoter Regions","Site-Directed","Fermentation","Ethical Theory","Genetic Therapy","Physiological","Xylose","Genes","Enzyme Activation","Cricetinae","Ethical Analysis","Oryza","Transcription Factors","Arabidopsis","Recombination","Cell Survival","Personal Autonomy","Cricetulus","DNA","Social Justice","Cell Line","CHO Cells","Glycerol","Fatty Acids","Reproductive Behavior","Doping in Sports")

newdata = scan(DATA_PATH)
dataset = matrix(newdata, nrow=ROW, byrow=T)
row.names(dataset) = NAMES
newdist = dist(dataset)
hc = hclust(d = newdist, method="complete")
plot(hc, hang = -1, main = "Cluster Dendrogram")
