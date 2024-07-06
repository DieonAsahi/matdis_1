def sum_arithmetic_series(n):
    return n * (n + 1) // 2

# Uji fungsi sum_arithmetic_series
test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected_results = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

for i, value in enumerate(test_values):
    result = sum_arithmetic_series(value)
    expected = expected_results[i]
    assert result == expected, f"Test gagal untuk n = {value}. Dapatkan {result}, tapi diharapkan {expected}."
    print(f"sum_arithmetic_series({value}) = {result} (sesuai)")

print("Semua tes berhasil.")
