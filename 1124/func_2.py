def tax_included(p,tax=10):
    return str(round(p+p*tax/100))+"円" if tax>0 else "None円"

print("5000の税込み金額は"+tax_included(5000))
print("5000の消費税 8%の税込金額は"+tax_included(5000,8))
print("5000の消費税 -5%の税込金額は"+tax_included(5000,-5))