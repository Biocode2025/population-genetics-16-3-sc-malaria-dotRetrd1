import os
outputDir = "..\\results"
os.makedirs(outputDir, exist_ok=True)


def SC_malaria(generations=50):
    q_squared_initial = 0.0036
    q = q_squared_initial ** 0.5  # HbS freq
    p = 1.0 - q                   # HbA freq
    
    filename = os.path.join(outputDir, "Sickle_cell_freq_het.csv")
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Generation\tq(HbS)\tp(HbA)\tHbA_HbA(p^2)\tHbA_HbS(2pq)\tHbS_HbS(q^2)\n")
        
        for gen in range(1, generations + 1):
            freq_HbA_HbA = p ** 2
            freq_HbA_HbS = 2 * p * q
            freq_HbS_HbS = q ** 2

            file.write(f"{gen}\t{q:.6f}\t{p:.6f}\t{freq_HbA_HbA:.6f}\t{freq_HbA_HbS:.6f}\t{freq_HbS_HbS:.6f}\n")
            
            # HbS = (pq) / (0.98 * p^2 + 2pq)
            q_next = (p * q) / (0.98 * (p ** 2) + 2 * p * q)
            
            # 1. Updated HbS freq
            q = q_next
            # 2. updated HbA freq
            p = 1.0 - q

    print(f"Simulation complete. Data saved to '{filename}'.")

SC_malaria(50)