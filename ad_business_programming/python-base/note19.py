# 텍스트 파일을 읽어서 단어를 분리하여 출력파일로 생성
infile = open('gisa.txt', "r", encoding='UTF8')
outfile = open('gisa_outfile.txt', "w")
for line  in infile:
	line = line.rstrip()
	word_list = line.split()
	for word in word_list:
		outfile.write(word)
		outfile.write("\n")
infile.close()
outfile.close()

# 단어 단위로 분리된 출력 파일 확인 
infile = open('gisa.txt', "r") 
line = infile.readline()
while line != "":
	print(line);
	line = infile.readline()
infile.close() 