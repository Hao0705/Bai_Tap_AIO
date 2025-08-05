from scipy.stats import false_discovery_control


def metric(tp, fp, fn):
    Precision = tp/(tp+fp)
    Recall = tp/(tp+fn)
    F1_score = 2 * Precision * Recall / (Precision + Recall)

    return Precision, Recall, F1_score

def check_input(tp, fp, fn):

    if type(tp) != int or type(fp) != int or type(fn) != int :
        print("value musst be in")
        return False
    if(fp <= 0 or tp <= 0 or fn <= 0):
        print("tp and fp and fn must begreater than zero")
        return False
    return True

tp = int(input("Nhap tp: "))
fp = int(input("Nhap fp: "))
fn = int(input("Nhap fn: "))

key = check_input(tp, fp, fn)

if key == True:
    Precision, Recall, F1_score = metric(tp, fp, fn)
    print("Precision = {} \nRecall = {} \nF1_score = {}".format(Precision, Recall, F1_score))
