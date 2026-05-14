# Shunting-Yard Algorithm Dijkstra (1961)
# Mengkonversi ekspresi infix → postfix menggunakan Stack.
# Kompleksitas: O(n) waktu, O(n) ruang.
#
# Aturan precedence:
# ^ : 4 (pangkat, right-associative)
# * : 3, / : 3 (kiri-asosiatif)
# + : 2, - : 2 (kiri-asosiatif)
# sin/cos/sqrt/log/abs : 5 (unary, right-associative)
#
# Algoritma (pseudocode):
# untuk setiap token t dalam ekspresi:
# jika t adalah angka/variabel: output(t)
# jika t adalah fungsi: push(t) ke operator_stack
# jika t adalah '(': push(t) ke operator_stack
# jika t adalah ')':
# while top != '(': output(pop())
# pop '(' (buang)
# jika top adalah fungsi: output(pop())
# jika t adalah operator:
# while (top adalah operator) dan
# (prec(top) > prec(t)) atau
# (prec(top) == prec(t) dan t left-assoc):
# output(pop())
# push(t)
# while operator_stack tidak kosong: output(pop())