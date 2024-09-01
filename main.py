import src.xmlparser
import src.numbercreation
import src.commonfinder


if __name__ == "__main__":
    src.xmlparser.xmlparser()
    src.numbercreation.numbercreation(start=1,end=9999,target_sum=None,check_lucky=True)
    src.commonfinder.commmonfinder()