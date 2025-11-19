registers = [0] * 6
memory = [10] * 6

while True:
    instruction = input().strip()
    if not instruction:
        continue

    if instruction == "END":
        break
    
    parts = instruction.replace(',', '').split()
    op = parts[0]

    if op == "add":
        rd = int(parts[1].replace('$', ''))
        rs1 = int(parts[2].replace('$', ''))
        rs2 = int(parts[3].replace('$', ''))
        registers[rd] = registers[rs1] + registers[rs2]

    elif op == "sub":
        rd = int(parts[1].replace('$', ''))
        rs1 = int(parts[2].replace('$', ''))
        rs2 = int(parts[3].replace('$', ''))
        registers[rd] = registers[rs1] - registers[rs2]

    elif op == "load":
        rd = int(parts[1].replace('$', ''))
        mem_addr = int(parts[2])
        registers[rd] = memory[mem_addr]

    elif op == "store":
        rs = int(parts[1].replace('$', ''))
        mem_addr = int(parts[2])
        memory[mem_addr] = registers[rs]

print("Register File :", ",".join(map(str, registers)))
print("Memory :", ",".join(map(str, memory)))

