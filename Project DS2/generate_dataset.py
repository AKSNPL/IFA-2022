import numpy as np
import pandas as pd
import glob

data_path="/media/jacky/data_4tb/Uni/FocusArea/PJ1/data/"

def main():
    image_files=glob.glob(data_path + "/*/*/*/*/*.png")
    label=np.array([],dtype=np.int8)
    for f in image_files:
        subname = f.split("/")
        if ("benign" in subname):
            label=np.append(label, 0)
        else:
            label=np.append(label, 1)
        print(label)
    df = pd.DataFrame(list(zip(image_files,label)),columns=["id","label"])
    df.to_csv(data_path + "cancer_dataset.csv",index=False,header=True)

if __name__=="__main__":
    main()