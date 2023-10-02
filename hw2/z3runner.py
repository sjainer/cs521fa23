import z3;
ctx = z3.Context()
s = z3.Solver(ctx=ctx)
f = z3.parse_smt2_file("q5.smt2")
print(f)