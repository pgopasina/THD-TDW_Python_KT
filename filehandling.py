file = open('sample.txt', mode='r')
print(file.read())
file.close()

# file1 = open('sample.txt', mode='w')
# file1.write("jhvcjsfg")
# file1.close()

file2 = open('sample.txt', mode='a')
file2.write(" how are you all")
file2.close()

file3 = open('sample.txt', mode='r+')
print(file3.read())
file3.write(" how are you all")
file3.close()

file4 = open('sample.txt', mode='w+')
file4.write(" how are you all")
file4.seek(0) #due to changing of file points change we use seek method
print(file4.read())
file4.close()