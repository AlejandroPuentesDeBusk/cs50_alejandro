file= str(input("File name: ").strip().lower())


if file.find(".gif") >=0 :
    print("image/gif")

elif file.find(".jpg") >=0:
    print("image/jpeg")

elif file.find(".jpeg") >=0:
    print("image/jpeg")

elif file.find(".png")>=0:
    print("image/png")

elif file.find(".pdf") >=0:
    print("application/pdf")

elif file.find(".txt") >=0:
    print("text/plain")

elif file.find(".zip") >=0:
    print("application/zip")

else:
    print("application/octet-stream")

