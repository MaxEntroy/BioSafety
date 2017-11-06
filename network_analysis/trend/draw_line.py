from matplotlib import pyplot as plt
import traceback

def draw_ling(X, Y):
    try:

        plt.subplot(1,1,1)
        plt.plot(X,Y, 'bo-', label="2006-2015", markersize=10)

        plt.xlim([2005,2016])
        plt.xticks(X)
        plt.xlabel("year")
        #plt.ylabel("percentage_of_coauthored_papers")
        plt.ylabel("average_number_of_authors_per_paper")

        plt.legend(loc=1)

        plt.show()

    except Exception,e:
        print traceback.print_exc()



def get_data( file_path ):
    try:
        data = []
        infile = open(file_path,"r")
        for line in infile:
            line = line.rstrip('\n')
            data.append(float(line))
        infile.close()
        return data
    except Exception:
        print traceback.print_exc()


if __name__ == '__main__':
    RATIO_PATH = "../../output/nums_per_article/nums_per_article.dat"
    X = [ x for x in range(2006,2016) ]
    Y = get_data(RATIO_PATH)
    draw_ling(X,Y)