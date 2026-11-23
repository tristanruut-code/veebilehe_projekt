f = open("Andmebaas.csv", "r", encoding="ISO 8859-1")
w = open("output.txt", "w", encoding="ISO 8859-1")

for rida in f:
    con = False
    temp = ["        <tr>\n"]
    for val in rida.strip().split(','):
        if con == True:
            if val[-1] == '"':
                con = False
                temp.append(",".join([temp.pop(), val[:-1]+"</td>\n"]))
            else:
                temp.append(",".join([temp.pop(), val]))
        else:
            if val[0] == '"':
                con = True
                temp.append(f"            <td>{val[1:]}")
            else:
                temp.append(f"            <td>{val}</td>\n")
    temp.append("        </tr>\n")
    for asi in temp:
        w.write(asi)
f.close()
w.close()