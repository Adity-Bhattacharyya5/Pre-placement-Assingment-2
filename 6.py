def add_polynomials(poly1, poly2):
    # Determine the larger length
    max_len = max(len(poly1), len(poly2))
    
    # Extend both lists to the same length
    poly1 += [0] * (max_len - len(poly1))
    poly2 += [0] * (max_len - len(poly2))
    
    # Add corresponding coefficients
    result = [poly1[i] + poly2[i] for i in range(max_len)]
    
    return result

# Example: index = power of x, value = coefficient
poly1 = [5, 0, 10, 6]   # 5 + 0x + 10x² + 6x³
poly2 = [1, 2, 4]       # 1 + 2x + 4x²

result = add_polynomials(poly1, poly2)
print(result)  # [6, 2, 14, 6] => 6 + 2x + 14x² + 6x³
