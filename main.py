from ortools.algorithms.python import knapsack_solver
import time
import argparse
import os

def read_file(file_path):
    values, weights = [], []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        capacities = int(lines[2])
        for line in lines[4:]:
            value, weight = map(int, line.strip().split())
            values.append(value)
            weights.append(weight)
    return [capacities], values, [weights]

def knapsack(capacities, values, weights, time_limit):
    # Create the solver.
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    # đặt giới hạn thời gian để kết thúc chương trình và trả về lời giải tốt nhất đã tìm thấy tại thời điểm này
    solver.set_time_limit(time_limit)

    start_time = time.time()

    solver.init(values, weights, capacities)

    computed_value = solver.solve()

    time_excution = time.time() - start_time

    packed_items = []
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print("Total weight:", total_weight)
    print("Packed items:", packed_items)
    print("Packed_weights:", packed_weights)
    
    print("time excution", time_excution)
    return computed_value, total_weight, packed_items, packed_weights, time_excution
def main():

    parser = argparse.ArgumentParser(description='Solve knapsack problem with time limit')
    parser.add_argument('time_limit', type=int, help='Time limit in seconds')
    args = parser.parse_args()
    time_limit = args.time_limit

    dir_path = os.getcwd()
    dir_path = os.path.join(dir_path, 'kplib')
    # tạo thư mục chứa output
    output_dir = os.path.join(os.getcwd(), f'output_{time_limit}')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    kplib_list = os.listdir(dir_path)[1:14] # 0->12

    for i in kplib_list:
        print(i)
        dir_path_0 = os.path.join(dir_path, i)
        case_list = os.listdir(dir_path_0)# n00050->n10000
        # print(case_list)
        for case in case_list:
            case_path = os.path.join(dir_path_0, case)
            R_list = os.listdir(case_path)
            for r in R_list:
                kp_filename = 's012'
                s_path = os.path.join(case_path, r, f'{kp_filename}.kp')            
                print(s_path)
                capacities, values, weights = read_file(s_path)

                computed_value, total_weight, packed_items, packed_weights, time_excution = knapsack(capacities, values, weights, time_limit)

                output_file_name = f'{i}_{case}_{r}_{kp_filename}.txt'
                output_path = os.path.join(output_dir, output_file_name)

                # kiểm tra tính optimal: 
                # giả sử: nếu thời gian thực thi nhỏ hơn time_limit thì lời giải optimal
                optimal = time_excution < time_limit
                
                with open(output_path, "w") as f:
                    f.write('Test case name: ' + output_file_name + '\n')
                    f.write('time knapsack caculate: '+str(time_excution)+'\n')
                    f.write('Total value = '+ str(computed_value)+'\n')
                    f.write('Total weight: '+ str(total_weight)+'\n')
                    f.write('Packed items: '+ str(packed_items)+'\n')
                    f.write('packed_weights: '+str (packed_weights))
                with open(os.path.join(os.getcwd(), f'output_{time_limit}.txt'), 'a') as file:
                    file.write(f'{output_file_name}, {computed_value}, {total_weight}, {time_excution}, {optimal}\n')

if __name__ == "__main__":
    main()