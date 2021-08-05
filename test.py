import glob, os

for f in glob.glob("data/student.1.*.jpg"):
    os.remove(f)
    #file_name_path = "data/student." + str(id) + "." + str(img_id) + ".jpg"
