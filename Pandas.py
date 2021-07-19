import pandas as pd

array1 = [["홍영석", 90, 80], ["김민태", 70, 95], ["박준현", 80, 90], ["김소철", 70, 80]]
df = pd.DataFrame(array1, columns=["이름", "수학", "영어"], index=["ㄱ", "ㄴ", "ㄷ", "ㄹ"])
print(df)
print("Type of df : " + str(type(df)))