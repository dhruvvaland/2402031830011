import numpy as np

def get_matrix_input(name, shape):
    print(f"\nEnter elements for {name} (shape {shape}):")
    total = np.prod(shape)
    data = []
    while len(data) < total:
        try:
            line = input(f"Enter {total - len(data)} more values (space-separated): ")
            nums = list(map(float, line.strip().split()))
            data.extend(nums)
        except ValueError:
            print("Invalid input! Enter numbers only.")
    return np.array(data).reshape(shape)

def print_menu():
    print("\nMatrix Operations Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrices")
    print("5. Determinant (only 2D square)")
    print("6. Inverse (only 2D square)")
    print("7. Rank")
    print("8. Trace")
    print("9. Exit")

def main():
    dims = int(input("Enter number of dimensions (e.g., 2): "))
    shape = tuple(map(int, input(f"Enter the shape (e.g., 2 2 for 2x2): ").split()))

    A = get_matrix_input("Matrix A", shape)
    B = get_matrix_input("Matrix B", shape)

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            try:
                print("\nA + B:\n", np.add(A, B))
            except:
                print("Addition not possible. Shape mismatch.")
        elif choice == '2':
            try:
                print("\nA - B:\n", np.subtract(A, B))
            except:
                print("Subtraction not possible. Shape mismatch.")
        elif choice == '3':
            try:
                if A.ndim == 2 and B.ndim == 2:
                    print("\nA x B:\n", np.matmul(A, B))
                else:
                    print("\nElement-wise multiplication:\n", A * B)
            except:
                print("Multiplication not possible.")
        elif choice == '4':
            print("\nTranspose of A:\n", A.transpose())
            print("Transpose of B:\n", B.transpose())
        elif choice == '5':
            if A.ndim == 2 and A.shape[0] == A.shape[1]:
                print("\nDeterminant of A:", np.linalg.det(A))
            else:
                print("Determinant only for 2D square matrix.")
        elif choice == '6':
            if A.ndim == 2 and A.shape[0] == A.shape[1]:
                try:
                    print("\nInverse of A:\n", np.linalg.inv(A))
                except np.linalg.LinAlgError:
                    print("Matrix A is not invertible.")
            else:
                print("Inverse only for 2D square matrix.")
        elif choice == '7':
            print("\nRank of A:", np.linalg.matrix_rank(A))
        elif choice == '8':
            if A.ndim == 2:
                print("\nTrace of A:", np.trace(A))
            else:
                print("Trace is only valid for 2D matrices.")
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
