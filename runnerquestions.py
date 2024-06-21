

# # def factors_and_distribution(num_candies):
# #     factors = []
# #     for i in range(1, int(num_candies**0.5) + 1):
# #         if num_candies % i == 0:
# #             factors.append(i)
# #             if i != num_candies // i:
# #                 factors.append(num_candies // i)

# #     factors.sort()
# #     distributions = [factor for factor in factors if num_candies % factor == 0]


# #     return distributions

# # def main():
# #     t = int(input("Enter the number of test cases: "))
# #     for _ in range(t):
# #         n = int(input())
# #         result = factors_and_distribution(n)
# #         if result:
# #             print(*result)
# #         else:
# #             print("No valid distributions found.")

# # if __name__ == "__main__":
# #     main()


# # def pfp(n):
# #     def prime_factors(num):
# #         factors = set()
# #         while num % 2 == 0:
# #             factors.add(2)
# #             num //= 2
# #         for i in range(3, int(num**0.5) + 1, 2):
# #             while num % i == 0:
# #                 factors.add(i)
# #                 num //= i
# #         if num > 2:
# #             factors.add(num)
# #         return sorted(list(factors))

# #     def am(factors):
# #         result = 1
# #         for factor in factors:
# #             result = (result * factor) % 1000000007
# #         return result

# #     factors = prime_factors(n)
# #     product = am(factors)

# #     print(*factors)
# #     print(product)

# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     pfp(n)


# # def prime_factors_and_product(n):
# #     MOD = 1000000007

# #     def sieve(n):
# #         is_prime = [True] * (n + 1)
# #         is_prime[0] = is_prime[1] = False
# #         primes = []
# #         for i in range(2, int(n**0.5) + 1):
# #             if is_prime[i]:
# #                 primes.append(i)
# #                 for j in range(i * i, n + 1, i):
# #                     is_prime[j] = False
# #         for i in range(int(n**0.5) + 1, n + 1):
# #             if is_prime[i]:
# #                 primes.append(i)
# #         return primes

# #     def accumulative_multiplication(factors):
# #         result = 1
# #         for factor in factors:
# #             result = (result * factor) % MOD
# #         return result

# #     primes = sieve(n)
# #     factors = set()
# #     for prime in primes:
# #         while n % prime == 0:
# #             factors.add(prime)
# #             n //= prime
# #     if n > 1:
# #         factors.add(n)

# #     sorted_factors = sorted(list(factors))
# #     print(*sorted_factors)
# #     print(accumulative_multiplication(sorted_factors))

# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     prime_factors_and_product(n)


# # def smallest_missing_positive(arr):
# #     n = len(arr)

# #     pos_nums = [num for num in arr if num > 0]

# #     if not pos_nums:
# #         return 1

# #     pos_nums.sort()
    
# #     missing = 1
# #     for num in pos_nums:
# #         if num == missing:
# #             missing += 1
# #         elif num > missing:
# #             break
    
# #     return missing

# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     arr = list(map(int, input().split()))
# #     result = smallest_missing_positive(arr)
# #     print(result)

# def rxcy(coord):
#     if coord[0] == 'R' and 'C' in coord:
#         row, col = map(int, coord[1:].split('C'))
#         col_str = ""
#         while col:
#             col -= 1
#             col_str = chr((col % 26) + ord('A')) + col_str
#             col //= 26
#         return col_str + str(row)
#     else:
#         col_str, row_str = "", ""
#         for i, ch in enumerate(coord):
#             if ch.isalpha():
#                 col_str += ch
#             else:
#                 row_str = coord[i:]
#                 break
#         col = 0
#         for i, ch in enumerate(col_str[::-1]):
#             col += (ord(ch) - ord('A') + 1) * (26 ** i)
#         return "R" + row_str + "C" + str(col)

# n = int(input())
# coordinates = [input().strip() for _ in range(n)]

# for k in coordinates:
#     print(rxcy(k))
