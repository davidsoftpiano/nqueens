# 8 Queen Problem

import sys
import time

import crud


class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()
        # return self.solutions

    def solve(self):
        # If the solutions were previously calculated do not recalculate
        res = crud.getSolutionNumber(self.size)
        print("Calculating, please wait ...: ")
        if res:
            sol_list = crud.getAllSolutions(self.size)
            self.solutions = res.solutions_number
            print(
                (
                    "N previously calculated,\n n: {0}, \n Number of solutions: {1} \n Solutions: \n"
                ).format(self.size, res.solutions_number)
            )
            try:
                self.show_ten_solutions(sol_list)

            except Exception as e:
                print("[NQueens] Solutions were not found in database, \n Error:", e)
            return self.solutions
        else:
            positions = [-1] * self.size
            self.place_queen(positions, 0)
            crud.setSolutionNumber(self.size, self.solutions)
            print("Found", self.solutions, "solutions.")
            sol_list = crud.getAllSolutions(self.size)
            self.show_ten_solutions(sol_list)
            return self.solutions

    def place_queen(self, positions, target_row):

        if target_row == self.size:
            # self.show_full_board(positions)
            cadena = str(positions)
            if self.solutions < 150:
                crud.setSolution(self.size, cadena)
            self.solutions += 1
        else:
            for column in range(self.size):

                if self.check(positions, target_row, column):
                    positions[target_row] = column
                    self.place_queen(positions, target_row + 1)

    def check(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column:
                # print("misma columna: ",i)
                return False
            elif positions[i] + ocuppied_rows - i == column:
                # print("diagonal pos: ",i)
                return False
            elif positions[i] - ocuppied_rows + i == column:
                # print("diagonal neg: ", i)
                return False
        return True

    def show_ten_solutions(self, sol_list):
        i = 0
        for sol in sol_list:
            i = i + 1
            if i < 10:
                # Parsing the data read from database to list of integers to show the board
                sol_list = sol.column_values.replace(" ", "")
                sol_list = sol_list.replace("[", "")
                sol_list = sol_list.replace("]", "")
                sol_list = list(sol_list.split(","))
                sol_list_int = list()
                for num in sol_list:
                    sol_list_int.append(int(num))
                print(sol_list_int)
                self.show_full_board(sol_list_int)
            else:
                break

    def show_full_board(self, positions):
        # Show the full NxN board
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += "* "
            print(line)
        print("\n")


def main(n):

    start = time.time()
    solutions = NQueens(n)
    print(solutions.solutions)
    end = time.time()
    # Agregar la columna exec_time a la tabla solutions_number
    duration = str(end - start)
    print("Time to calculate (seconds): ", duration)
    # crud.setSolution(n, cadena)
    return solutions.solutions


if __name__ == "__main__":

    try:
        n = int(sys.argv[1])
        response = main(n)
        print(("Number of solutions found for n={0} are:{1}").format(n, response))
    except:
        print(
            "[Nqueens]: Number of queens to calculate is required as parameter, please run again: NqueensProblem n"
        )
