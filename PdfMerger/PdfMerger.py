import pypdf
import os

merger = pypdf.PdfMerger()
filelist = []
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "Documents")

for file in os.listdir(downloads_path):
    if file.endswith(".pdf"):
        filelist.append(file)

for cnt in range(len(filelist)):
    print(f"{cnt+1} : {filelist[cnt]}")

file1, file2 = int(input("First file no: ")), int(input("Second file no: "))

merger.append(os.path.join(downloads_path, filelist[file1 - 1]))
merger.append(os.path.join(downloads_path, filelist[file2 - 1]))

save_path = os.path.join(downloads_path, "Merged.pdf")
merger.write(save_path)

print("Merged pdf stored at location: ", save_path)
merger.close()