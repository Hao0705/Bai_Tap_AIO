def edit_Levenshtein(source, taget):
    col = len(taget)
    row = len(source)

    D = [[0 for _ in range(col)] for _ in range(row)]

    # Khởi tạo hàng và cột đầu tiên
    for i in range(row):
        D[i][0] = i
    for j in range(col):
        D[0][j] = j

    for i in range(1, row):
        for j in range(1, col):

            score_up = D[i-1][j] + 1
            score_left = D[i][j-1] + 1
            sub_cost = 1
            if source[i-1] == taget[j-1]:
                sub_cost = 0
            score_diagonal = D[i-1][j-1] + sub_cost


            D[i][j] = min(score_up, score_left, score_diagonal)
    return D[row-1][col-1]

source = input("Nhap source:")
taget = input("Nhap taget:")

score = edit_Levenshtein(source, taget)
print(score)
