config_myfile_path = "./running-config.cfg"
output_myfile = "./config-modified.cfg"
find_ip = "172."
replace_ip = "192."
def main():
    filein = open(config_myfile_path)
    fileout = open(output_myfile,'w')
    for line in filein:
        line_modified = line.replace(find_ip,replace_ip)
        fout.write(line_modified)
    filein.close()
    fileout.close()
if __name__ == '__main__':
    main()
