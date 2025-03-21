def e_multiplo(nums: tuple) -> bool:
    # num1, num2 = nums
    # return num2 % num1 == 0

    maior = max(nums)
    menor = min(nums)
    return maior % menor == 0
