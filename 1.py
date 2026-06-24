# import json

# f = open("text.json")
# # 1........................................

# natija = json.load(f)
# for i in natija["branches"]:
#     print(i["name"])

# # 2.........................................

# for i in natija["branches"]:
#     for x in i["teachers"]:
#         if x["subject"]=="Python":
#             print(x["name"],"-",i["name"],"-",x["experience"])

# # 3.........................................

# for i in natija["branches"]:
#     print(i["name"],":",len(i["students"]))


# # 4.........................................

# max = 0
# for i in natija["branches"]:
#     for x in i["students"]:
#         if x["payment"]>max:
#             max = x["payment"]
# print(x["name"],":",i["name"])


# # 5...........................................

# for i in natija["branches"]:
#     sum=0
#     for x in i["students"]:
#         sum+=x["payment"]
#     print(i["name"],":",sum)


# # 6............................................

# for i in natija["branches"]:
#     for x in i["teachers"]:
#         if x["experience"]>5:
#             print(x)



# # 7.............................................

# for i in natija["branches"]:
#     for x in i["students"]:
#         if x["course"]=="Python":
#             print(i["name"])

# f.close()


# uv................................................

# 1................................................

# def last_unique_character(text:str):
#     for i in text[::-1]:
#         if text.count(i)==1:
#             return i
#     return "_"
# print(last_unique_character("Ppython"))


# 2.................................................

def analyze_floats_in_text(text: str) -> dict:
    lst = []
    for i in text.replace(",", " ").split():
        try:
            if "." in i:
                lst.append(float(i))
        except:
            pass

    if len(lst) == 0:
        return {"average": 0, "min": 0, "max": 0}

    return {
        "average": round(sum(lst) / len(lst), 2),
        "min": min(lst),
        "max": max(lst)
    }
text = input("text:")
print(analyze_floats_in_text(text))


            

