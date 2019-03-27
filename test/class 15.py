temps=[('berlin', 29), ('cairo', 36), ('india', 40), ('sri lanka', 18)]
conver_temp=lambda x:(x[0].captalize(),x[1])
print(list(map(conver_temp, temps)))