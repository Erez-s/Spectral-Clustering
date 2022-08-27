import random
import os
import time
import subprocess
import filecmp


def compareFilesModule(file1, file2):
    result = filecmp.cmp(file1, file2)
    print(result)
    result = filecmp.cmp(file1, file2, shallow=False)
    print(result)


def compare_file(file1, file2, log_file):
    f = open(log_file, 'a')
    f.write(file1 + "\n" + file2 + "\n")
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    if len(lines1) != len(lines2):
        f.write("error, lines not the same length")

    for i in range(len(lines1)):
        coordinates1 = lines1[i].split(",")
        coordinates2 = lines2[i].split(",")
        if len(coordinates1) != len(coordinates2):
            f.write("error, coordinates not the same length")
        for j in range(len(coordinates1)):
            if abs(float(coordinates1[j]) - float(coordinates2[j])) > 0.0001:
                f.write("The variation is too big")
    f.write("\n")
    f.write("------------------------------------------------------------")
    f.write("\n")
    f1.close()
    f2.close()
    f.close()


def get_ramdom_point(dimension):
    point = [str(format(random.uniform(0, 50), ".4f")) + "," for i in range(dimension)]
    try:
        point[-1] = point[-1][0:-1]
    except:
        return point
    return point


def write_inputfile(path):
    n = random.randint(1, 100)
    dimension = random.randint(1, 5)
    f = open(path, "w")
    f.close()
    f = open(path, "a")
    for i in range(n):
        point = get_ramdom_point(dimension)
        for coordinate in point:
            f.write(coordinate)
        f.write("\n")
    f.close()


def save_output(exe_file_path, input_path, output_path, goal):
    subprocess.Popen([exe_file_path, goal, input_path, output_path])


def create_output_files(num_of_tests, cmp_path, exe_file_tal, exe_file_adam, goal):
    for i in range(num_of_tests):
        print("working on file:" + str(i))
        input_path = cmp_path + "\\" + "input_files" + "\\" + "inputFile_test_" + str(i) + ".txt"
        output_path = cmp_path + "\\" + "output_talc" + "\\" + "OutputFile_test_" + str(i) + ".txt"
        output_adam = cmp_path + "\\" + "output_adamc" + "\\" + "OutputFile_test_" + str(i) + ".txt"
        write_inputfile(cmp_path + "\\" + "input_files" + "\\" + "inputFile_test_" + str(i) + ".txt")
        save_output(exe_file_tal, input_path, output_path, goal)
        save_output(exe_file_adam, input_path, output_adam, goal)
    time.sleep(8)


def compare_all_files(num_of_tests, cmp_path, log_path):
    for i in range(num_of_tests):
        output_tal = cmp_path + "\\" + "output_talc" + "\\" + "OutputFile_test_" + str(i) + ".txt"
        output_adam = cmp_path + "\\" + "output_adamc" + "\\" + "OutputFile_test_" + str(i) + ".txt"
        compareFilesModule(output_tal, output_adam)
        compare_file(output_tal, output_adam, log_path)


num_of_tests = 20  # change to desired number
cmp_path = "C:\\Users\\erezs\\Desktop\\tests"  # change to your computer path
log_path = cmp_path + "\\" + "log.txt"
exe_file_tal = cmp_path + "\\" + "spkmeanstal.exe"
exe_file_adam = cmp_path + "\\" + "spkmeansadam.exe"
goal = "lnorm"

create_output_files(num_of_tests, cmp_path, exe_file_tal, exe_file_adam, goal)
compare_all_files(num_of_tests, cmp_path, log_path)
